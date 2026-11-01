(function(){
  'use strict';

  /* ====== SANITIZE HELPER ====== */
  window.sanitize = function(str){
    if(!str) return '';
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  };

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ТЕМА */
  try{
    const saved = localStorage.getItem('ff_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
    window.toggleTheme = function(){
      const cur = document.documentElement.getAttribute('data-theme');
      const next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try{ localStorage.setItem('ff_theme', next); }catch(e){}
      updateThemeIcon(next);
    };
    const themeBtn = document.getElementById('themeToggle');
    if(themeBtn){ themeBtn.addEventListener('click', window.toggleTheme); }
    function updateThemeIcon(theme){
      const btn = document.getElementById('themeToggle');
      if(!btn) return;
      btn.innerHTML = theme === 'dark'
        ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>'
        : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    }
    updateThemeIcon(saved);
  }catch(e){}

  /* АНИМАЦИИ И СКРОЛЛ */
  try{
    const fadeEls = document.querySelectorAll('.fade-up');
    if('IntersectionObserver' in window){
      const io = new IntersectionObserver((entries) => {
        entries.forEach(en => { if(en.isIntersecting){ en.target.classList.add('visible'); io.unobserve(en.target); } });
      }, { threshold: .08, rootMargin: '0px 0px -40px 0px' });
      fadeEls.forEach(el => io.observe(el));
    } else { fadeEls.forEach(el => el.classList.add('visible')); }
  }catch(e){}

  /* СЧЕТЧИКИ */
  try{
    const counters = document.querySelectorAll('[data-count]');
    const runCounter = (el) => {
      if(el.dataset.done === '1') return;
      el.dataset.done = '1';
      const target = parseInt(el.getAttribute('data-count'), 10) || 0;
      const sup = el.querySelector('sup') ? el.querySelector('sup').outerHTML : '';
      const start = performance.now(), dur = 1100;
      const tick = (now) => {
        const p = Math.min((now - start) / dur, 1);
        el.innerHTML = Math.round(target * (1 - Math.pow(1 - p, 3))) + sup;
        if(p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if(counters.length && 'IntersectionObserver' in window){
      const cObs = new IntersectionObserver((entries) => {
        entries.forEach(en => { if(en.isIntersecting){ runCounter(en.target); cObs.unobserve(en.target); } });
      }, { threshold: .05 });
      counters.forEach(c => cObs.observe(c));
    } else { counters.forEach(runCounter); }
  }catch(e){}

  /* КНОПКА НАВЕРХ */
  try{
    const toTop = document.getElementById('toTop');
    if(toTop){
      let lastY = window.scrollY;
      const updateToTop = () => {
        const y = window.scrollY;
        const show = y > 500 && y < lastY; // show only when scrolling up and not at top
        // Actually show when scrolled down enough, hide at top
        const shouldShow = y > 600;
        toTop.classList.toggle('visible', shouldShow);
        lastY = y;
      };
      window.addEventListener('scroll', updateToTop, { passive: true });
      updateToTop();
      toTop.addEventListener('click', () => {
        toTop.classList.remove('visible');
        window.scrollTo({ top: 0, behavior: prefersReduced ? 'auto' : 'smooth' });
      });
    }
  }catch(e){}

  /* КАРУСЕЛЬ ОТЗЫВОВ (бесконечная) */
  try{
    const slider = document.querySelector('.reviews__slider');
    const prevBtn = document.querySelector('.slider-btn--prev');
    const nextBtn = document.querySelector('.slider-btn--next');
    if(slider && prevBtn && nextBtn){
      // Clone first and last cards for infinite loop
      const cards = Array.from(slider.children);
      if(cards.length > 1){
        const firstClone = cards[0].cloneNode(true);
        const lastClone = cards[cards.length-1].cloneNode(true);
        slider.appendChild(firstClone);
        slider.insertBefore(lastClone, cards[0]);
        slider.scrollLeft = lastClone.offsetWidth;
      }
      let isScrolling = false;
      const cardWidth = () => slider.querySelector('.review-card') ? slider.querySelector('.review-card').offsetWidth + 24 : slider.offsetWidth;
      prevBtn.addEventListener('click', () => {
        if(isScrolling) return;
        isScrolling = true;
        slider.scrollBy({ left: -cardWidth(), behavior: 'smooth' });
        setTimeout(() => { isScrolling = false; }, 400);
      });
      nextBtn.addEventListener('click', () => {
        if(isScrolling) return;
        isScrolling = true;
        slider.scrollBy({ left: cardWidth(), behavior: 'smooth' });
        setTimeout(() => { isScrolling = false; }, 400);
      });
      // Reset scroll position for infinite loop
      slider.addEventListener('scroll', () => {
        const maxScroll = slider.scrollWidth - slider.clientWidth;
        if(slider.scrollLeft <= 10){
          slider.scrollLeft = maxScroll - slider.clientWidth - 10;
        } else if(slider.scrollLeft >= maxScroll - 10){
          slider.scrollLeft = slider.clientWidth + 10;
        }
      });
    }
  }catch(e){}


  /* QUIZ + ПОТЕРИ */
  try{
    const quiz = document.getElementById('quiz');
    if(quiz){
      const Q = [
        { q:'Сколько раз за последний год сервер «просто перезагружался»?', a:[{t:'Ни разу',s:0},{t:'1–2 раза',s:1},{t:'Больше',s:2},{t:'Не знаю — это же не моя проблема',s:3}] },
        { q:'Когда вы последний раз проверяли, что бэкап реально восстанавливается?', a:[{t:'На этой неделе',s:0},{t:'В прошлом квартале',s:1},{t:'Помню, что «делали»',s:2},{t:'Бэкап — это когда файлы лежат рядом',s:3}] },
        { q:'Кто отвечает за инфраструктуру, если админ уходит в отпуск?', a:[{t:'Команда',s:0},{t:'Другой сотрудник',s:1},{t:'Никто, но мы надеемся',s:2},{t:'Отпуск? У нас так не принято',s:3}] },
        { q:'Сколько сотрудников могут подписать документ ЭЦП прямо сейчас?', a:[{t:'Все, кому нужно',s:0},{t:'Половина',s:1},{t:'Один — и он в отпуске',s:2},{t:'Мы ещё не считали',s:3}] },
        { q:'Что будет, если завтра отключится электричество на 2 часа?', a:[{t:'ИБП + генератор',s:0},{t:'ИБП на 20 минут',s:1},{t:'Сервер выключится',s:2},{t:'Начнётся «день без интернета»',s:3}] }
      ];
      let qi = 0, qScore = 0;
      const qBody = quiz.querySelector('.quiz__body');
      const qDots = quiz.querySelectorAll('.quiz__dot');
      
      function renderQuiz(){
        qDots.forEach((d, i) => { d.classList.remove('active','done'); if(i<qi) d.classList.add('done'); if(i===qi) d.classList.add('active'); });
        if(qi >= Q.length){ showQuizResult(); return; }
        const item = Q[qi];
        qBody.innerHTML = `<div class="quiz__step active"><div class="quiz__q">${item.q}</div><div class="quiz__opts">${item.a.map((opt,i) => `<button type="button" class="quiz__opt" data-i="${i}">${opt.t}</button>`).join('')}</div></div>`;
        qBody.querySelectorAll('.quiz__opt').forEach(btn => {
          btn.addEventListener('click', () => { qScore += item.a[parseInt(btn.getAttribute('data-i'),10)].s; qi++; renderQuiz(); });
        });
      }
      
      function showQuizResult(){
        qDots.forEach(d => d.classList.add('done'));
        // Show "thinking" state for 1.5s
        qBody.innerHTML = '<div style="text-align:center;padding:40px 0;"><div style="font-size:14px;color:var(--muted);margin-bottom:16px;">Анализируем ваши ответы...</div><div style="width:60px;height:4px;background:var(--border);border-radius:2px;margin:0 auto;overflow:hidden;"><div style="width:0;height:100%;background:var(--gold-light);animation:quizLoad 1.5s ease forwards;"></div></div></div>';
        setTimeout(() => { renderQuizResult(); }, 1500);
        return;
      }
      function renderQuizResult(){
        let level, cls, text;
        if(qScore <= 3){ level='Всё отлично'; cls='green'; text='Вы молодцы. Инфраструктура под контролем. Но профилактика не помешает.'; }
        else if(qScore <= 8){ level='Крепко, но есть нюансы'; cls='yellow'; text='Инфраструктура держится на честном слове. Мы можем это исправить до того, как оно исправит вас.'; }
        else if(qScore <= 12){ level='Пора задуматься'; cls='orange'; text='Риски высоки. Пора навести порядок, пока не случилась беда.'; }
        else { level='Критично'; cls='red'; text='Мы не говорим «всё плохо». Мы говорим: давайте посмотрим, где именно. Бесплатный аудит.'; }

        qBody.innerHTML = `
          <div class="quiz__step active">
            <div class="quiz__result-header">
              <span class="quiz__level quiz__level--${cls}">${level}</span>
              <p style="font-size:14px;color:var(--text-2);margin:10px 0 0;">${text}</p>
            </div>
            <div style="text-align:center;margin:16px 0;padding:12px;border-radius:12px;background:var(--card);border:1px solid var(--border);">
              <div style="font-size:12px;color:var(--muted);margin-bottom:4px;">Ваш уровень зрелости</div>
              <div style="font-size:20px;font-weight:800;color:var(--gold-light);">${level}</div>
            </div>
            <div class="quiz__loss-box">
              <div class="quiz__loss-title">Стоимость бездействия</div>
              <div class="quiz__loss-val" id="lossVal">65 000 ₽ <small style="font-size:14px;color:var(--muted);font-family:Inter">за инцидент</small></div>
               <div style="font-size:11px;color:var(--muted);margin-top:6px;text-align:center;">Средняя зарплата сотрудника: 650 ₽/час · без учёта потерянной выручки</div>
              <div class="quiz__loss-controls">
                <div class="quiz__input-group"><label>Сотрудников</label><input type="number" id="lossEmp" value="25" min="1"></div>
                <div class="quiz__input-group"><label>Часов простоя</label><input type="number" id="lossHours" value="4" min="1"></div>
                <div class="quiz__input-group"><label>Ср. зарплата (₽/час)</label><input type="number" id="lossRate" value="650" min="1"></div>
              </div>
            </div>
            <div class="quiz__contacts">
              <input type="text" class="quiz__input" id="qName" placeholder="Ваше имя">
              <input type="text" class="quiz__input" id="qContact" placeholder="Telegram, MAX или телефон">
            </div>
            <div class="form-group form-group--checkbox" style="margin-bottom:16px;">
              <input type="checkbox" id="qAgree">
              <label for="qAgree" style="font-size:12px;color:var(--text-2)">Согласен с <a href="privacy.html" style="color:var(--gold-light)">политикой конфиденциальности</a></label>
            </div>
            <div class="quiz__actions">
              <button class="btn btn--primary" onclick="submitQuiz(event)">Обсудить задачу</button>
              <button class="btn btn--ghost" onclick="window.print()" style="margin-top:8px;">Скачать PDF-чеклист</button>
              <a class="btn btn--ghost" id="quizTgBtn" style="margin-top:8px;display:inline-block;text-align:center;" target="_blank" rel="noopener">Отправить результат в Telegram</a>
            </div>
          </div>
        `;
        const calcLoss = () => {
          const e = parseInt(document.getElementById('lossEmp').value)||0;
          const h = parseInt(document.getElementById('lossHours').value)||0;
          const r = parseInt(document.getElementById('lossRate').value)||0;
          document.getElementById('lossVal').innerHTML = (e*h*r).toLocaleString('ru-RU') + ' ₽ <small style="font-size:14px;color:var(--muted);font-family:Inter">за инцидент</small>';
        };
        ['lossEmp','lossHours','lossRate'].forEach(id => document.getElementById(id).addEventListener('input', calcLoss));
        const tgBtn = document.getElementById('quizTgBtn');
        const maxBtn = document.getElementById('quizMaxBtn');
        if(maxBtn){ maxBtn.href = 'https://max.ru/FathFed?text=' + encodeURIComponent('Результат квиза F&F: уровень «' + level + '», баллы: ' + qScore + '.'); }
        if(tgBtn){ tgBtn.href = 'https://t.me/FathFed?text=' + encodeURIComponent('Результат квиза F&F: уровень «' + level + '», баллы: ' + qScore + '. Потери за инцидент: ' + (parseInt(document.getElementById('lossEmp').value)||0)*(parseInt(document.getElementById('lossHours').value)||0)*(parseInt(document.getElementById('lossRate').value)||0) + ' ₽'); }
      }

      window.submitQuiz = async function(ev){
        const btn = ev.target.closest('button');
        const name = document.getElementById('qName').value.trim();
        const contact = document.getElementById('qContact').value.trim();
        const agree = document.getElementById('qAgree').checked;
        const loss = document.getElementById('lossVal').innerText;

        let hasErr = false;
        if(!name){ showFieldError(document.getElementById('qName'), 'Укажите имя'); hasErr = true; }
        if(!contact){ showFieldError(document.getElementById('qContact'), 'Укажите контакт'); hasErr = true; }
        if(!agree){ showFieldError(document.getElementById('qAgree'), 'Подтвердите согласие'); hasErr = true; }
        if(hasErr) return;

        btn.textContent = 'Отправляем...'; btn.disabled = true;

        try {
          const resp = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
            method: 'POST', headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
            body: JSON.stringify({ name, contact_way: contact, message: `Пройден квиз. Потери: ${loss}`, service: 'Квиз', agree: true })
          });
          const res = await resp.json();
          if(resp.ok){
            qBody.innerHTML = `<div style="text-align:center;padding:40px 0;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--neon)" stroke-width="2" style="margin:0 auto 16px;"><polyline points="20 6 9 17 4 12"/></svg><h3 style="font-size:20px;margin-bottom:8px;">Спасибо, ${name}!</h3><p style="color:var(--text-2);margin-bottom:20px;">Мы уже изучаем вашу ситуацию. Свяжемся в течение 15 минут.</p><a href="services.html#calculator" class="btn btn--primary">Пока посмотреть цены</a></div>`;
          } else {
            showToast(btn, res.message || 'Ошибка', 'error'); btn.disabled = false; btn.textContent = 'Обсудить задачу';
          }
        } catch(e) {
          showToast(btn, 'Ошибка соединения', 'error'); btn.disabled = false; btn.textContent = 'Обсудить задачу';
        }
      };
      renderQuiz();
    }
  }catch(e){ console.error('Quiz', e); }


  /* ====== CALCULATOR (services.html) ====== */
  try{
    const calcState = { step: 1, selected: new Set(), qty: {}, prices: {
      'server-select':4000,'server-file':2800,'server-domain':4000,'server-dns':2000,'server-rdp':4400,'server-backup':4800,'server-custom':4000,
      'mnt-file':2400,'mnt-domain':4000,'mnt-dns':2000,'mnt-rdp':3600,'mnt-backup':3200,
      'crypto-license':1200,'crypto-install':1200,'crypto-setup':1600,'crypto-ecp':1200,'vipnet-install':1200,'encrypt-full':1600,
      'audit-express':4000,'audit-full':12000
    }, names: {
      'server-select':'Подбор серверного оборудования','server-file':'Файловый сервер','server-domain':'Доменный сервер (AD)','server-dns':'DNS-сервер','server-rdp':'Терминальный сервер (RDS)','server-backup':'Сервер резервного копирования','server-custom':'Настройка под другие задачи',
      'mnt-file':'Обслуживание файлового сервера','mnt-domain':'Обслуживание доменного сервера','mnt-dns':'Обслуживание DNS-сервера','mnt-rdp':'Обслуживание терминального сервера','mnt-backup':'Обслуживание сервера бэкапов',
      'crypto-license':'КриптоПро: продажа лицензии','crypto-install':'КриптоПро: установка','crypto-setup':'КриптоПро: настройка','crypto-ecp':'Клонирование ЭЦП','vipnet-install':'ViPNet: установка','encrypt-full':'Шифрование данных (VeraCrypt)',
      'audit-express':'Экспресс IT-аудит','audit-full':'Полный IT-аудит'
    } };
    const calcDots = document.querySelectorAll('.calc__dot');
    const calcSteps = document.querySelectorAll('.calc__step');
    const money = new Intl.NumberFormat('ru-RU');
    function calcUpdateMobile(){
      const mobile = document.getElementById('calcMobileTotal');
      const value = document.getElementById('calcMobileValue');
      if(!mobile || !value) return;
      let total = 0;
      calcState.selected.forEach(key => { total += (calcState.prices[key] || 0) * (calcState.qty[key] || 1); });
      const discount = calcState.selected.size >= 10 ? 0.2 : (calcState.selected.size >= 5 ? 0.1 : 0);
      value.textContent = money.format(Math.round(total * (1 - discount))) + ' ₽';
      mobile.classList.toggle('is-visible', calcState.selected.size > 0);
    }
    function calcRenderStep(n){
      calcState.step = n;
      calcSteps.forEach(s => s.classList.toggle('active', parseInt(s.getAttribute('data-step'),10) === n));
      calcDots.forEach((d,i) => { d.classList.remove('active','done'); if(i+1 < n) d.classList.add('done'); if(i+1 === n) d.classList.add('active'); });
      if(n === 2){ calcRenderQty(); }
      if(n === 3){ calcRenderSummary(); }
    }
    window.calcToggle = function(el){
      const key = el.getAttribute('data-key');
      if(!key) return;
      const selected = !calcState.selected.has(key);
      if(selected) calcState.selected.add(key); else calcState.selected.delete(key);
      el.classList.toggle('active', selected);
      el.setAttribute('aria-pressed', String(selected));
      calcState.qty[key] = calcState.qty[key] || 1;
      calcUpdateMobile();
    };
    window.calcNext = function(ev){
      if(ev && ev.preventDefault) ev.preventDefault();
      if(calcState.step === 1){
        if(calcState.selected.size === 0){ showToast(ev && ev.target, 'Отметьте хотя бы одну услугу', 'error'); return; }
        calcRenderStep(2);
      } else if(calcState.step === 2){
        calcRenderStep(3);
      }
    };
    window.calcPrev = function(){
      if(calcState.step > 1) calcRenderStep(calcState.step - 1);
    };
    function calcRenderQty(){
      const list = document.getElementById('calcQtyList');
      if(!list) return;
      list.innerHTML = '';
      calcState.selected.forEach(key => {
        const q = calcState.qty[key] || 1;
        const div = document.createElement('div');
        div.className = 'calc__qty-item';
        const label = document.createElement('label');
        const input = document.createElement('input');
        const inputId = 'calcQty-' + key;
        label.htmlFor = inputId;
        label.textContent = calcState.names[key] || key;
        input.id = inputId;
        input.type = 'number';
        input.min = '1';
        input.step = '1';
        input.inputMode = 'numeric';
        input.value = String(q);
        input.dataset.key = key;
        input.addEventListener('input', () => {
          calcState.qty[key] = Math.max(1, parseInt(input.value,10)||1);
          calcUpdateMobile();
        });
        div.append(label, input);
        list.appendChild(div);
      });
    }
    function calcRenderSummary(){
      const summary = document.getElementById('calcSummary');
      const totalEl = document.getElementById('calcTotalValue');
      if(!summary || !totalEl) return;
      let oneTime = 0, monthly = 0, html = '';
      calcState.selected.forEach(key => {
        const q = calcState.qty[key] || 1;
        const price = (calcState.prices[key] || 0) * q;
        const isMonthly = key.indexOf('mnt-') === 0;
        if(isMonthly) monthly += price; else oneTime += price;
        html += `<div class="calc__summary-row"><span>${calcState.names[key] || key} × ${q}<small>${isMonthly ? 'ежемесячно' : 'разовая услуга'}</small></span><span>${price.toLocaleString('ru-RU')} ₽${isMonthly ? '/мес' : ''}</span></div>`;
      });
      const discount = calcState.selected.size >= 10 ? 0.2 : (calcState.selected.size >= 5 ? 0.1 : 0);
      oneTime = Math.round(oneTime * (1 - discount));
      monthly = Math.round(monthly * (1 - discount));
      summary.innerHTML = html || '<p style="color:var(--muted);">Ничего не выбрано</p>';
      totalEl.textContent = monthly && oneTime
        ? oneTime.toLocaleString('ru-RU') + ' ₽ разово + ' + monthly.toLocaleString('ru-RU') + ' ₽/мес'
        : monthly ? monthly.toLocaleString('ru-RU') + ' ₽/мес' : oneTime.toLocaleString('ru-RU') + ' ₽ разово';
      if(discount) totalEl.textContent += ' · скидка ' + Math.round(discount*100) + '%';
      calcUpdateMobile();
    }
    window.calcSubmit = function(ev){
      const btn = ev && ev.target ? ev.target.closest('button') : null;
      const name = (document.getElementById('calcName')||{}).value || '';
      const contact = (document.getElementById('calcContact')||{}).value || '';
      const agree = (document.getElementById('calcAgree')||{}).checked;
      if(!name.trim()) return showToast(btn, 'Укажите имя', 'error');
      if(!contact.trim()) return showToast(btn, 'Укажите контакт', 'error');
      if(!agree) return showToast(btn, 'Подтвердите согласие', 'error');
      if(btn){ btn.textContent = 'Отправляем...'; btn.disabled = true; }
      try {
        fetch('https://formspree.io/f/YOUR_FORM_ID', { method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'},
          body: JSON.stringify({ name: name.trim(), contact_way: contact.trim(), message: 'Расчёт сметы с сайта', service: 'Калькулятор', agree: true })
        }).then(r=>r.json()).then(res=>{
          const succ = document.getElementById('calcSuccess');
          if(res && res.ok === true){
            if(succ){ succ.style.display='block'; succ.textContent = 'Спасибо, ' + name.trim() + '! Вышлем смету в ближайшее время.'; }
          } else {
            showToast(btn, (res && res.message) || 'Ошибка', 'error');
            if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; }
          }
        }).catch(()=>{ showToast(btn, 'Ошибка соединения', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } });
      } catch(e){ showToast(btn, 'Ошибка', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } }
    };
  }catch(e){ console.error('Calc', e); }


  /* ====== COOKIE BANNER ====== */
  window.acceptCookie = function(){
    try{ localStorage.setItem('ff_cookie', 'accepted'); }catch(e){}
    const b = document.getElementById('cookie');
    if(b){ b.style.display = 'none'; }
  };
  window.rejectCookie = function(){
    try{ localStorage.setItem('ff_cookie', 'rejected'); }catch(e){}
    const b = document.getElementById('cookie');
    if(b){ b.style.display = 'none'; }
  };
  try{
    const cookieBanner = document.getElementById('cookie');
    if(cookieBanner){
      let choice = null;
      try{ choice = localStorage.getItem('ff_cookie'); }catch(e){}
      if(choice){ cookieBanner.style.display = 'none'; }
      else { cookieBanner.style.display = ''; }
    }
  }catch(e){}

  /* ====== CONTACT FORM ====== */
  try{
    const contactForm = document.querySelector('form[name="contact-form"]');
    if(contactForm){
      contactForm.addEventListener('submit', function(ev){
        ev.preventDefault();
        const btn = contactForm.querySelector('button[type="submit"]');
        const name = (contactForm.querySelector('#name')||{}).value || '';
        const contact = (contactForm.querySelector('#contact-way')||{}).value || '';
        const message = (contactForm.querySelector('#problem')||{}).value || '';
        const agree = (contactForm.querySelector('#agree')||{}).checked;
        let hasErr = false;
        if(!name.trim()){ showFieldError(contactForm.querySelector('#name'), 'Укажите имя'); hasErr = true; }
        if(!contact.trim()){ showFieldError(contactForm.querySelector('#contact-way'), 'Укажите контакт'); hasErr = true; }
        const hp = (contactForm.querySelector('input[name="website"]')||{}).value || '';
        if(hp) return; // honeypot
        if(!agree){ showFieldError(contactForm.querySelector('#agree'), 'Подтвердите согласие с политикой'); hasErr = true; }
        if(hasErr) return;
        if(btn){ btn.textContent = 'Отправляем...'; btn.disabled = true; }
        fetch('https://formspree.io/f/YOUR_FORM_ID', { method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'},
          body: JSON.stringify({ name: name.trim(), contact_way: contact.trim(), message: message.trim(), service: 'Главная страница', agree: true })
        }).then(r=>r.json()).then(res=>{
          const succ = document.getElementById('contactSuccess');
          if(res && res.ok === true){
            if(succ){ succ.style.display='block'; succ.textContent = 'Спасибо, ' + name.trim() + '! Свяжемся в течение 15 минут.'; }
            contactForm.reset();
          } else {
            showToast(btn, (res && res.message) || 'Ошибка', 'error');
            if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; }
          }
        }).catch(()=>{ showToast(btn, 'Ошибка соединения', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } });
      });
    }
  }catch(e){}

  /* ====== TOAST HELPER ====== */
  window.showToast = function(btn, msg, type){
    try{
      let toast = document.getElementById('ff-toast');
      if(!toast){ toast = document.createElement('div'); toast.id='ff-toast'; toast.style.cssText='position:fixed;bottom:24px;left:50%;transform:translateX(-50%);padding:12px 20px;border-radius:10px;font-size:14px;font-weight:600;z-index:9999;transition:opacity .3s;'; document.body.appendChild(toast); }
      toast.textContent = msg;
      toast.style.background = type === 'error' ? '#ff4d4d' : '#00FF88';
      toast.style.color = type === 'error' ? '#fff' : '#000';
      toast.style.opacity = '1';
      clearTimeout(window._toastTimer);
      window._toastTimer = setTimeout(() => { toast.style.opacity = '0'; }, 3000);
    }catch(e){}
  };


  /* ====== EASTER EGG: KONAMI CODE ====== */
  try{
    const konami = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];
    let ki = 0;
    document.addEventListener('keydown', function(e){
      if(e.target && e.target.closest('input,textarea,select,[contenteditable="true"]')){ ki=0; return; }
      if(e.repeat) return;
      if(e.key === konami[ki]){ ki++; if(ki === konami.length){ ki = 0; showEasterEgg(); } }
      else { ki = 0; }
    });
    function showEasterEgg(){
      const el = document.createElement('div');
      el.setAttribute('role','dialog');
      el.setAttribute('aria-modal','true');
      el.setAttribute('aria-label','Пасхалка F&F');
      el.tabIndex = -1;
      el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:99999;display:flex;align-items:center;justify-content:center;flex-direction:column;color:#00FF88;font-family:ui-monospace,monospace;font-size:14px;text-align:center;padding:20px;';
      el.innerHTML = '<pre style="margin:0;">'
        + '  ███████╗██╗  ██╗██╗████████╗\n'
        + '  ██╔════╝██║  ██║██║╚══██╔══╝\n'
        + '  ███████╗███████║██║   ██║   \n'
        + '  ╚════██║██╔══██║██║   ██║   \n'
        + '  ███████║██║  ██║██║   ██║   \n'
        + '  ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   \n'
        + '</pre>'
        + '<p style="margin-top:20px;color:#9aa0a6;">Вы нашли пасхалку. Булат знает, что вы это сделали.</p>'
        + '<button onclick="this.parentElement.remove()" style="margin-top:16px;padding:8px 20px;border-radius:8px;border:1px solid #00FF88;background:transparent;color:#00FF88;cursor:pointer;">Закрыть</button>';
      document.body.appendChild(el);
      const closeButton=el.querySelector('button');
      if(closeButton) closeButton.focus();
      el.addEventListener('keydown',function(e){
        if(e.key==='Escape'){el.remove();return;}
        if(e.key==='Tab'&&closeButton){e.preventDefault();closeButton.focus();}
      });
    }
  }catch(e){}

  /* ====== EASTER EGG: MATRIX MODE ====== */
  try{
    let mCount = 0, mTimer = null;
    document.addEventListener('keydown', function(e){
      if(e.target && e.target.closest('input,textarea,select,[contenteditable="true"]')){mCount=0;return;}
      if(e.repeat) return;
      if(e.key === 'm' || e.key === 'M'){
        mCount++;
        clearTimeout(mTimer);
        mTimer = setTimeout(() => { mCount = 0; }, 1000);
        if(mCount >= 3){
          mCount = 0;
          toggleMatrix();
        }
      }
    });
    function toggleMatrix(){
      const existing = document.getElementById('ff-matrix');
      if(existing){ clearInterval(existing._matrixTimer); clearTimeout(existing._matrixCleanup); existing.remove(); return; }
      const canvas = document.createElement('canvas');
      canvas.id = 'ff-matrix';
      canvas.style.cssText = 'position:fixed;inset:0;z-index:9990;pointer-events:none;opacity:.15;';
      document.body.appendChild(canvas);
      const ctx = canvas.getContext('2d');
      if(!ctx){canvas.remove();return;}
      const resize=()=>{canvas.width=window.innerWidth;canvas.height=window.innerHeight;};
      resize();
      window.addEventListener('resize',resize,{passive:true});
      const chars = 'F&F01アイウエオカキクケコサシスセソ';
      const fontSize = 14;
      const cols = Math.floor(canvas.width / fontSize);
      const drops = Array(cols).fill(1);
      const iv = setInterval(() => {
        ctx.fillStyle = 'rgba(0,0,0,.05)';
        ctx.fillRect(0,0,canvas.width,canvas.height);
        ctx.fillStyle = '#00FF88';
        ctx.font = fontSize + 'px monospace';
        for(let i=0;i<drops.length;i++){
          const text = chars[Math.floor(Math.random()*chars.length)];
          ctx.fillText(text, i*fontSize, drops[i]*fontSize);
          if(drops[i]*fontSize > canvas.height && Math.random() > .975) drops[i] = 0;
          drops[i]++;
        }
      }, 33);
      canvas._matrixTimer=iv;
      canvas._matrixCleanup=setTimeout(() => { clearInterval(iv);window.removeEventListener('resize',resize);canvas.remove(); }, 10000);
    }
  }catch(e){}



  /* ====== SECRET THEMES ====== */
  try{
    const secretThemes = { 'matrix': 'matrix', 'retro': 'retro', 'cyberpunk': 'cyberpunk', 'neon': 'neon', 'ocean': 'ocean', 'sunset': 'sunset', 'mono': 'mono' };
    let themeBuffer = '';
    document.addEventListener('keydown', function(e){
      if(e.target && e.target.closest('input,textarea,select,[contenteditable="true"]')){themeBuffer='';return;}
      if(e.repeat) return;
      if(e.key.length === 1){
        themeBuffer += e.key.toLowerCase();
        if(themeBuffer.length > 10) themeBuffer = themeBuffer.slice(-10);
        for(const name in secretThemes){
          if(themeBuffer.endsWith(name)){
            document.documentElement.setAttribute('data-theme', secretThemes[name]);
            try{ localStorage.setItem('ff_theme', secretThemes[name]); }catch(e){}
            themeBuffer = '';
            if(typeof showToast === 'function') showToast(null, 'Тема: ' + name, 'success');
          }
        }
      }
    });
  }catch(e){}


  /* ====== PERSONALIZATION REMOVED ====== */

  /* ФУТЕР - НРАВИТСЯ САЙТ */
  try{
    const sigBtn = document.querySelector('.footer__brand-signature');
    if(sigBtn){
      sigBtn.addEventListener('click', function(){
        this.classList.toggle('active');
      });
    }
  }catch(e){}

})();










  /* ====== INLINE FIELD ERROR HELPER ====== */
  window.showFieldError = function(input, msg){
    if(!input) return;
    let err = input.parentElement.querySelector('.field-error');
    if(!err){ err = document.createElement('div'); err.className = 'field-error'; err.style.cssText = 'color:#ff4d4d;font-size:11px;margin-top:4px;'; input.parentElement.appendChild(err); }
    err.textContent = msg;
    input.style.borderColor = '#ff4d4d';
  };
  window.clearFieldError = function(input){
    if(!input) return;
    const err = input.parentElement.querySelector('.field-error');
    if(err) err.remove();
    input.style.borderColor = '';
  };
  // Clear errors on input
  document.addEventListener('input', function(e){
    if(e.target && (e.target.id === 'name' || e.target.id === 'contact-way' || e.target.id === 'problem' || e.target.id === 'qName' || e.target.id === 'qContact')) {
      clearFieldError(e.target);
    }
  });

/* Shared navigation and restored calculators */
(function(){
  'use strict';
  var nav=document.querySelector('.nav');
  if(nav){
    var triggers=Array.from(nav.querySelectorAll('[data-nav-trigger]'));
    function closeMenus(except){triggers.forEach(function(t){if(t!==except){t.setAttribute('aria-expanded','false');t.parentElement.classList.remove('is-open');}});}
    triggers.forEach(function(trigger){
      trigger.addEventListener('click',function(e){e.stopPropagation();var open=trigger.getAttribute('aria-expanded')==='true';closeMenus(trigger);trigger.setAttribute('aria-expanded',String(!open));trigger.parentElement.classList.toggle('is-open',!open);});
      trigger.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='Enter'||e.key===' '){e.preventDefault();trigger.click();var first=trigger.parentElement.querySelector('.dropdown a');if(first)first.focus();}});
      trigger.parentElement.addEventListener('keydown',function(e){if(e.key==='Escape'){closeMenus();trigger.focus();}});
      trigger.parentElement.addEventListener('focusout',function(){window.setTimeout(function(){if(!trigger.parentElement.contains(document.activeElement)&&!trigger.parentElement.matches(':hover'))closeMenus();},0);});
    });
    document.addEventListener('click',function(e){if(!nav.contains(e.target))closeMenus();});
  }
  var burger=document.getElementById('burgerBtn'),drawer=document.getElementById('mobileNav');
  if(burger&&drawer){
    var panel=drawer.querySelector('.mobile-nav__panel');
    var closeButtons=drawer.querySelectorAll('[data-mobile-close]');
    var previousFocus=null;
    function closeDrawer(restore){drawer.classList.remove('is-open');burger.classList.remove('active');drawer.setAttribute('aria-hidden','true');burger.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open');if(restore&&previousFocus)previousFocus.focus();}
    function openDrawer(){previousFocus=document.activeElement;drawer.classList.add('is-open');burger.classList.add('active');drawer.setAttribute('aria-hidden','false');burger.setAttribute('aria-expanded','true');document.body.classList.add('menu-open');var first=drawer.querySelector('.mobile-nav__close');if(first)first.focus();}
    burger.addEventListener('click',function(){drawer.classList.contains('is-open')?closeDrawer(true):openDrawer();});
    closeButtons.forEach(function(button){button.addEventListener('click',function(){closeDrawer(true);});});
    drawer.querySelectorAll('a[href]').forEach(function(link){link.addEventListener('click',function(){if(link.closest('.mobile-nav__panel'))closeDrawer(false);});});
    drawer.addEventListener('click',function(e){if(e.target===drawer)closeDrawer(true);});
    document.addEventListener('keydown',function(e){
      if(!drawer.classList.contains('is-open'))return;
      if(e.key==='Escape'){e.preventDefault();closeDrawer(true);return;}
      if(e.key==='Tab'&&panel){var items=Array.from(panel.querySelectorAll('a[href],button:not([disabled]),summary')).filter(function(el){return el.offsetParent!==null;});if(!items.length)return;var first=items[0],last=items[items.length-1];if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}}
    });
  }
  var form=document.querySelector('form[name="contact-form"]');
  if(form){var params=new URLSearchParams(location.search);var msg=form.querySelector('#problem');if(msg&&params.get('source')==='subscription'){msg.value='Предварительный расчёт абонентского обслуживания: тариф '+(params.get('plan')||'')+', компьютеры '+(params.get('computers')||'')+', серверы '+(params.get('servers')||'')+', принтеры/МФУ '+(params.get('printers')||'')+'. Ориентир '+(params.get('monthly')||'')+' ₽/мес.';}}
  var root=document.getElementById('subscriptionCalculator');
  if(root){var rates={basic:900,optimal:1200,extended:1500},plan='basic',pc=root.querySelector('#subComputers'),srv=root.querySelector('#subServers'),printer=root.querySelector('#subPrinters'),fmt=new Intl.NumberFormat('ru-RU');function update(){if(!pc||!srv||!printer)return;var pcs=Number(pc.value),servers=Number(srv.value),printers=Number(printer.value),pcTotal=pcs*rates[plan],serverTotal=servers*3200,printerTotal=printers*300,extras=0;root.querySelectorAll('[data-sub-extra]:checked').forEach(function(el){extras+=Number(el.dataset.price)||0;});var total=pcTotal+serverTotal+printerTotal+extras;root.querySelector('#subComputersValue').textContent=pcs;root.querySelector('#subServersValue').textContent=servers;root.querySelector('#subPrintersValue').textContent=printers;root.querySelector('#subPcLine').textContent=fmt.format(pcTotal)+' ₽';root.querySelector('#subServerLine').textContent=fmt.format(serverTotal)+' ₽';root.querySelector('#subPrinterLine').textContent=fmt.format(printerTotal)+' ₽';root.querySelector('#subExtrasLine').textContent=fmt.format(extras)+' ₽';root.querySelector('#subTotal').textContent=fmt.format(total)+' ₽/мес';var link=root.querySelector('#subCalcContact');var p=new URLSearchParams({source:'subscription',plan:plan,computers:pcs,servers:servers,printers:printers,monthly:total});link.href='contacts.html?'+p.toString();}
    root.querySelectorAll('[data-sub-plan]').forEach(function(button){button.addEventListener('click',function(){plan=button.dataset.subPlan;root.querySelectorAll('[data-sub-plan]').forEach(function(item){var selected=item===button;item.classList.toggle('is-selected',selected);item.setAttribute('aria-pressed',String(selected));});update();});});[pc,srv,printer].forEach(function(input){if(input)input.addEventListener('input',update);});root.querySelectorAll('[data-sub-extra]').forEach(function(input){input.addEventListener('change',update);});update();}
  var estimator=document.querySelector('#calculator .calc');
  if(estimator){estimator.querySelectorAll('.calc__service').forEach(function(button){button.setAttribute('aria-pressed',String(button.classList.contains('active')));});}
})();

/* ====== EXIT-INTENT POPUP ====== */
(function(){
  try {
    const popup = document.getElementById('exitPopup');
    if(!popup) return;
    const closeBtn = document.getElementById('exitPopupClose');
    const backdrop = document.getElementById('exitPopupBackdrop');
    const form = document.getElementById('exitPopupForm');
    const success = document.getElementById('exitPopupSuccess');
    let shown = false;
    function show(){ if(shown) return; shown = true; popup.classList.add('is-open'); popup.setAttribute('aria-hidden','false'); }
    function hide(){ popup.classList.remove('is-open'); popup.setAttribute('aria-hidden','true'); }
    closeBtn && closeBtn.addEventListener('click', hide);
    backdrop && backdrop.addEventListener('click', hide);
    document.addEventListener('mouseleave', function(e){ if(e.clientY <= 0) show(); });
    let scrolled = false;
    window.addEventListener('scroll', function(){ if(scrolled) return; const pct = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight; if(pct >= 0.5){ scrolled = true; setTimeout(show, 30000); } });
    setTimeout(show, 60000);
    if(form){
      form.addEventListener('submit', function(ev){
        ev.preventDefault();
        const hp = form.querySelector('input[name="website"]');
        if(hp && hp.value) return; // honeypot
        const email = (form.querySelector('input[name="email"]')||{}).value || '';
        if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return;
        if(success){ success.style.display = 'block'; success.textContent = 'Спасибо! Проверьте почту.'; }
        form.style.display = 'none';
        try { fetch('https://formspree.io/f/YOUR_FORM_ID', { method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'}, body: JSON.stringify({ email: email, service: 'Exit-popup чек-лист', agree: true }) }); } catch(e){}
      });
    }
  } catch(e) {}
})();

/* HERO TERMINAL REMOVED */

/* ====== LIVE METRICS ====== */
(function(){
  try {
    fetch('data.json').then(r=>r.json()).then(d=>{
      const r = document.getElementById('metric-response');
      const q = document.getElementById('metric-requests');
      const i = document.getElementById('metric-incidents');
      if(r && d.response) r.textContent = d.response;
      if(q && d.requests) q.textContent = d.requests;
      if(i && d.incidents) i.textContent = d.incidents;
    }).catch(()=>{});
  } catch(e) {}
})();

/* ====== CYBER HERO TERMINAL ====== */
(function(){
  try {
    const body = document.getElementById('heroTermBody');
    if(!body) return;
    const lines = [
      { t: 'root@ff-it:~# ./ff-it --status --verbose', cls: 'prompt' },
      { t: '# Инициализация защитного ядра F&F v4.0', cls: 'comment' },
      { t: '# Хаб: Казань · Узлы: 128 · Статус: OK', cls: 'comment' },
      { t: '[✓] RAID-массив · NVMe SSD  ', cls: 'ok', bar: true },
      { t: '[✓] Шифрование AES-256      ', cls: 'ok', bar: true },
      { t: '[✓] Бэкап · 3-2-1 · оффлайн ', cls: 'ok', bar: true },
      { t: '[✓] Защитный контур · EDR   ', cls: 'ok', bar: true },
      { t: '', cls: '' },
      { t: '[ OK ] Мониторинг 24/7 · SLA 99.5%', cls: 'ok2' },
      { t: '[ OK ] Готовы помочь вашему бизнесу.', cls: 'ok2' },
    ];
    let li = 0;
    function showLine() {
      if (li >= lines.length) return;
      const l = lines[li];
      const div = document.createElement('div');
      div.className = 'term-win__line';
      if (l.cls === 'prompt') div.style.color = '#00E5FF';
      else if (l.cls === 'comment') div.style.color = '#9AA0A6';
      else if (l.cls === 'ok2') div.style.color = '#00E5FF';
      else div.style.color = '#00FF88';
      if (l.bar) {
        div.innerHTML = l.t + '<span class="term-win__progress"><span class="term-win__progress-fill"></span></span> 100%';
      } else {
        div.textContent = l.t;
      }
      body.appendChild(div);
      // animate progress bar
      if (l.bar) {
        const fill = div.querySelector('.term-win__progress-fill');
        if (fill) setTimeout(() => { fill.style.width = '100%'; }, 50);
      }
      li++;
      const delay = l.t.length > 0 ? Math.min(800, 200 + l.t.length * 8) : 200;
      setTimeout(showLine, delay);
    }
    setTimeout(showLine, 400);
  } catch(e) {}
})();

/* ====== BRANDbar COUNTERS ====== */
(function(){
  try {
    const nums = document.querySelectorAll('.brandbar-cyber__num[data-target]');
    if(!nums.length) return;
    const animate = (el) => {
      const target = parseInt(el.getAttribute('data-target'), 10);
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 1200;
      const start = performance.now();
      function step(now) {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + (p < 1 ? '' : suffix);
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      }
      requestAnimationFrame(step);
    };
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { animate(e.target); obs.unobserve(e.target); } });
    }, { threshold: 0.1 });
    nums.forEach(n => {
      const rect = n.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        animate(n);
      } else {
        obs.observe(n);
      }
    });
  } catch(e) {}
})();


  /* ====== FAQ SMOOTH ANIMATION ====== */
  try{
    document.querySelectorAll('.faq__item').forEach(details => {
      const summary = details.querySelector('.faq__question');
      if(!summary) return;
      summary.addEventListener('click', (e) => {
        if(details.open) return; // let default close happen
        // animate open
        details.style.overflow = 'hidden';
      });
    });
  }catch(e){}



/* ====== TERMINAL PROGRESSIVE LOADING ====== */
try {
  const termBody = document.getElementById('terminalBody');
  if (termBody) {
    const items = Array.from(termBody.children);
    items.forEach(el => { el.style.opacity = '0'; el.style.transform = 'translateY(6px)'; el.style.transition = 'opacity 0.35s ease, transform 0.35s ease'; });
    let delay = 200;
    items.forEach((el, i) => {
      setTimeout(() => {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }, delay);
      delay += 320;
    });
  }
} catch(e) {}


  window.openQuizPDF = function(){
    const name = (document.getElementById('qName')||{}).value || '';
    const level = document.querySelector('.quiz__level') ? document.querySelector('.quiz__level').textContent : '';
    const loss = document.getElementById('lossVal') ? document.getElementById('lossVal').innerText : '';
    const html = '<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8"><title>Чек-лист F&F</title><style>body{font-family:Inter,sans-serif;padding:40px;color:#1E1913;}h1{color:#B8932E;}ul{line-height:1.8;}</style></head><body><h1>Чек-лист инфраструктуры F&F</h1><p>Имя: ' + (name||'Клиент') + '</p><p>Уровень: ' + level + '</p><p>Стоимость бездействия: ' + loss + '</p><h2>Что проверить:</h2><ul><li>Бэкапы: проверка восстановления раз в месяц</li><li>Мониторинг 24/7 с алертами</li><li>SLA с фиксированным временем реакции</li><li>Документация: схемы, пароли, процедуры</li><li>ЭЦП и криптография: токены, сертификаты</li><li>Сетевая инфраструктура: VLAN, VPN, Wi-Fi</li></ul><p style="margin-top:40px;color:#7D7266;font-size:12px;">F&F — Ваш IT-контур под контролем. Даже в субботу.</p></body></html>';
    const w = window.open('', '_blank');
    if(w){ w.document.write(html); w.document.close(); }
  };


/* ====== SATURDAY SCENARIOS (10, random, no repeat) ====== */
(function(){
  const scenarios = [
    [
      {t:'00:00 — Сервер ушёл в ребут. Офис спит.', d:'Ничего не предвещало.', c:'danger'},
      {t:'00:15 — F&F получил алерт. Инженер уже с ноутбуком.', d:'Реакция от 15 минут — норма.', c:'gold'},
      {t:'00:40 — Причина найдена. Перезапуск сервиса.', d:'Сервис работает. Проверяем логи.', c:'gold'},
      {t:'01:10 — Сервис работает. Логи чисты.', d:'Всё под контролем.', c:'gold'},
      {t:'08:00 — Офис приходит. Никто ничего не заметил.', d:'Ваш IT-контур под контролем. Даже в субботу.', c:'neon'}
    ],
    [
      {t:'02:30 — Диск умирает. SMART-алерт.', d:'F&F замечает деградацию.', c:'danger'},
      {t:'02:45 — F&F поднимает RAID-массив из бэкапа.', d:'Данные не потеряны.', c:'gold'},
      {t:'03:20 — Миграция на новый диск завершена.', d:'Проверка целостности.', c:'gold'},
      {t:'04:00 — Всё работает. Уведомление клиенту.', d:'Утром — отчёт.', c:'gold'},
      {t:'09:00 — Офис работает. Диск заменён.', d:'Плановая замена в понедельник.', c:'neon'}
    ],
    [
      {t:'23:45 — Отключили свет в офисе.', d:'ИБП включился.', c:'danger'},
      {t:'23:50 — F&F получил алерт об отключении питания.', d:'Инженер на связи.', c:'gold'},
      {t:'00:05 — ИБП держит 15 минут. Запуск генератора.', d:'Сервер жив.', c:'gold'},
      {t:'00:20 — Электричество восстановлено.', d:'Переход на основное питание.', c:'gold'},
      {t:'08:00 — Офис приходит. Сервер работает.', d:'Ни минуты простоя.', c:'neon'}
    ],
    [
      {t:'01:00 — Бэкап не прошёл. Алерт.', d:'F&F проверяет.', c:'danger'},
      {t:'01:20 — Найдена причина: переполнен диск бэкапов.', d:'Очистка + новый план.', c:'gold'},
      {t:'02:00 — Тестовый контур развёрнут.', d:'Восстановление проверено.', c:'gold'},
      {t:'02:30 — Бэкап работает. Отчёт клиенту.', d:'Всё под контролем.', c:'gold'},
      {t:'08:00 — Офис работает. Бэкапы в норме.', d:'Без потерь.', c:'neon'}
    ],
    [
      {t:'03:00 — Шифровальщик обнаружен.', d:'F&F блокирует сеть.', c:'danger'},
      {t:'03:15 — Изоляция заражённого сегмента.', d:'Угроза локализована.', c:'gold'},
      {t:'03:45 — Восстановление из оффлайн-бэкапа.', d:'Данные целы.', c:'gold'},
      {t:'04:30 — Система чиста. Отчёт.', d:'Инцидент закрыт.', c:'gold'},
      {t:'09:00 — Офис работает. Всё восстановлено.', d:'Защитный контур усилен.', c:'neon'}
    ],
    [
      {t:'00:30 — Админ уволился. Пароли не переданы.', d:'Риск утечки.', c:'danger'},
      {t:'00:45 — F&F проверяет реестр доступов.', d:'Аудит прав.', c:'gold'},
      {t:'01:30 — Все пароли сброшены. Права переписаны.', d:'Доступы убраны.', c:'gold'},
      {t:'02:00 — Документация обновлена.', d:'Новый админ получит доступы.', c:'gold'},
      {t:'08:00 — Офис работает. Безопасность восстановлена.', d:'Контур под контролем.', c:'neon'}
    ],
    [
      {t:'01:00 — Сетевой сбой. VPN отвалился.', d:'Удалённые сотрудники без доступа.', c:'danger'},
      {t:'01:20 — F&F переключает на резервный канал.', d:'Связь восстановлена.', c:'gold'},
      {t:'01:45 — Диагностика провайдера.', d:'Проблема на стороне провайдера.', c:'gold'},
      {t:'02:10 — Резервный канал стабилен.', d:'Всё работает.', c:'gold'},
      {t:'08:00 — Офис работает. VPN поднят.', d:'Без простоев.', c:'neon'}
    ],
    [
      {t:'00:00 — 1С упала. База не отвечает.', d:'Бухгалтерия встала.', c:'danger'},
      {t:'00:20 — F&F перезапускает сервис 1С.', d:'Проверка базы.', c:'gold'},
      {t:'00:45 — База восстановлена из бэкапа.', d:'Потеряно 15 минут данных.', c:'gold'},
      {t:'01:10 — 1С работает. Проверка целостности.', d:'Всё в норме.', c:'gold'},
      {t:'08:00 — Офис работает. 1С доступна.', d:'Без простоя.', c:'neon'}
    ],
    [
      {t:'02:00 — Wi-Fi сеть упала. Клиенты без интернета.', d:'Розница встала.', c:'danger'},
      {t:'02:15 — F&F перезагружает точки доступа.', d:'Диагностика.', c:'gold'},
      {t:'02:40 — Найдена причина: перегрев точки.', d:'Замена точки.', c:'gold'},
      {t:'03:00 — Wi-Fi работает. Сеть стабильна.', d:'Всё под контролем.', c:'gold'},
      {t:'08:00 — Офис работает. Wi-Fi в норме.', d:'Без потерь.', c:'neon'}
    ],
    [
      {t:'00:00 — Пожарная сигнализация. Серверная в дыму.', d:'Критическая ситуация.', c:'danger'},
      {t:'00:05 — F&F получает алерт. Инженер выезжает.', d:'Аварийный выезд.', c:'gold'},
      {t:'00:40 — Сервер эвакуирован. Данные спасены.', d:'Бэкап в облаке.', c:'gold'},
      {t:'01:30 — Сервер поднят в резервном ЦОД.', d:'Работа восстановлена.', c:'gold'},
      {t:'08:00 — Офис работает. Без потерь данных.', d:'Контур под контролем.', c:'neon'}
    ]
  ];
  let used = [];
  window.runSaturdayScenario = function(){
    const container = document.getElementById('saturdayTimeline');
    if(!container) return;
    // pick random unused
    let available = scenarios.map((_,i)=>i).filter(i=>!used.includes(i));
    if(available.length === 0){ used = []; available = scenarios.map((_,i)=>i); }
    const idx = available[Math.floor(Math.random()*available.length)];
    used.push(idx);
    const scen = scenarios[idx];
    // clear
    const line = container.querySelector('div[style*="position:absolute;left:8px"]');
    container.innerHTML = '';
    container.appendChild(line);
    // reveal one by one
    let delay = 100;
    scen.forEach((s, i) => {
      setTimeout(() => {
        const div = document.createElement('div');
        div.style.cssText = 'margin-bottom:20px;position:relative;opacity:0;transform:translateY(8px);transition:opacity 0.4s ease,transform 0.4s ease;';
        const dotColor = s.c === 'danger' ? 'var(--danger,#ff4d4d)' : (s.c === 'neon' ? 'var(--neon)' : 'var(--gold-light)');
        div.innerHTML = '<span style="position:absolute;left:-20px;top:4px;width:12px;height:12px;border-radius:50%;background:'+dotColor+';box-shadow:0 0 8px '+dotColor+';"></span>'
          + '<div style="font-size:13px;font-weight:700;margin-bottom:4px;">' + s.t + '</div>'
          + '<div style="font-size:12px;color:var(--muted);">' + s.d + '</div>';
        container.appendChild(div);
        requestAnimationFrame(() => { div.style.opacity = '1'; div.style.transform = 'translateY(0)'; });
      }, delay);
      delay += 600;
    });
  };
})();
