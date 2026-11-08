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
    counters.forEach(el => {
      if(el.dataset.done === '1') return;
      el.dataset.done = '1';
      const target = parseInt(el.getAttribute('data-count'), 10) || 0;
      const sup = el.querySelector('sup') ? el.querySelector('sup').outerHTML : '';
      el.innerHTML = target + sup;
    });
  }catch(e){}

  /* КНОПКА НАВЕРХ */
  try{
    const toTop = document.getElementById('toTop');
    if(toTop){
      let ticking = false;
      const updateToTop = () => {
        const y = window.scrollY;
        toTop.classList.toggle('visible', y > 500);
        ticking = false;
      };
      window.addEventListener('scroll', () => {
        if (!ticking) {
          requestAnimationFrame(updateToTop);
          ticking = true;
        }
      }, { passive: true });
      updateToTop();
      toTop.addEventListener('click', () => {
        toTop.classList.remove('visible');
        window.scrollTo({ top: 0, behavior: prefersReduced ? 'auto' : 'smooth' });
      });
    }
  }catch(e){}

  /* КАРУСЕЛЬ ОТЗЫВОВ (бесконечная, без прыжков) */
  try{
    const slider = document.querySelector('.reviews__slider');
    const prevBtn = document.querySelector('.slider-btn--prev');
    const nextBtn = document.querySelector('.slider-btn--next');
    if(slider && prevBtn && nextBtn){
      const cards = Array.from(slider.children);
      if(cards.length > 1){
        const firstClone = cards[0].cloneNode(true);
        const lastClone = cards[cards.length-1].cloneNode(true);
        slider.appendChild(firstClone);
        slider.insertBefore(lastClone, cards[0]);
        // Start at first real card (after clone)
        slider.scrollLeft = lastClone.offsetWidth;
      }
      let isScrolling = false;
      const cardWidth = () => { const c = slider.querySelector('.review-card'); return c ? c.offsetWidth + 24 : slider.offsetWidth; };
      function resetIfNeeded() {
        const maxScroll = slider.scrollWidth - slider.clientWidth;
        // If at the last clone, jump to first real (no animation)
        if (slider.scrollLeft >= maxScroll - 5) {
          slider.scrollLeft = slider.clientWidth + 10 - (maxScroll - slider.scrollLeft);
          // simpler: jump to first real card
          const lc = slider.querySelector('.review-card');
          if(lc) slider.scrollLeft = lc.offsetWidth;
        }
        // If at the first clone, jump to last real
        if (slider.scrollLeft <= 5) {
          const cards2 = slider.querySelectorAll('.review-card');
          if(cards2.length > 2) slider.scrollLeft = slider.scrollWidth - slider.clientWidth - cards2[0].offsetWidth - 24;
        }
      }
      prevBtn.addEventListener('click', () => {
        if(isScrolling) return;
        isScrolling = true;
        slider.scrollBy({ left: -cardWidth(), behavior: 'smooth' });
        setTimeout(() => { resetIfNeeded(); isScrolling = false; }, 450);
      });
      nextBtn.addEventListener('click', () => {
        if(isScrolling) return;
        isScrolling = true;
        slider.scrollBy({ left: cardWidth(), behavior: 'smooth' });
        setTimeout(() => { resetIfNeeded(); isScrolling = false; }, 450);
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
      if(typeof window.ymGoal === 'function'){ window.ymGoal('quiz_complete'); }
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
        else { level='Критично'; cls='red'; text='Давайте посмотрим, где именно. Разбор 15 минут — 0 ₽.'; }

        qBody.innerHTML = `
          <div class="quiz__step active">
            <div class="quiz__result-header">
              <div style="font-size:12px;color:var(--muted);margin-bottom:4px;">Ваш уровень зрелости</div>
              <span class="quiz__level quiz__level--${cls}">${level}</span>
              <p style="font-size:14px;color:var(--text-2);margin:10px 0 0;">${text}</p>
            </div>
            <div class="quiz__loss-box">
              <div class="quiz__loss-title">Стоимость бездействия</div>
              <div class="quiz__loss-val" id="lossVal">65 000 ₽ <small style="font-size:14px;color:var(--muted);font-family:Inter">за инцидент *</small></div>
               <div style="font-size:11px;color:var(--muted);margin-top:6px;text-align:center;">* без учёта потерянной прибыли</div>
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
              <label for="qAgree" style="font-size:12px;color:var(--text-2)">Я согласен на обработку персональных данных в соответствии с <a href="privacy.html" style="color:var(--gold-light)">политикой конфиденциальности</a></label>
            </div>
            <div class="quiz__actions">
              <button class="btn btn--primary" onclick="submitQuiz(event)">Прислать разбор</button>
              <a href="services.html#estimate" class="btn btn--ghost">Рассчитать стоимость</a>
              <a href="tel:+79012655252" class="btn btn--ghost">+7 (901) 265-52-52</a>
            </div>
            <p style="font-size:12px;color:var(--muted);text-align:center;margin-top:8px;">Можно ничего не оставлять и просто позвонить</p>
          </div>
        `;
        const calcLoss = () => {
          const e = parseInt(document.getElementById('lossEmp').value)||0;
          const h = parseInt(document.getElementById('lossHours').value)||0;
          const r = parseInt(document.getElementById('lossRate').value)||0;
          document.getElementById('lossVal').innerHTML = (e*h*r).toLocaleString('ru-RU') + ' ₽ <small style="font-size:14px;color:var(--muted);font-family:Inter">за инцидент</small>';
        };
        ['lossEmp','lossHours','lossRate'].forEach(id => document.getElementById(id).addEventListener('input', calcLoss));

        if(tgBtn){ tgBtn.href = 'https://t.me/FathFed?text=' + encodeURIComponent('Результат квиза F&F: уровень «' + level + '», баллы: ' + qScore + '. Потери за инцидент: ' + (parseInt(document.getElementById('lossEmp').value)||0)*(parseInt(document.getElementById('lossHours').value)||0)*(parseInt(document.getElementById('lossRate').value)||0) + ' ₽'); }
      }

      window.submitQuiz = async function(ev){
        const btn = ev.target.closest('button');
        const name = document.getElementById('qName').value.trim();
        const contact = document.getElementById('qContact').value.trim();
        const agree = document.getElementById('qAgree').checked;
        const loss = document.getElementById('lossVal').innerText;

        if(!name) return showToast(btn, 'Укажите имя', 'error');
        if(!contact) return showToast(btn, 'Укажите контакт', 'error');
        if(!agree) return showToast(btn, 'Подтвердите согласие', 'error');

        btn.textContent = 'Отправляем...'; btn.disabled = true;

        try {
          const resp = await fetch('https://formspree.io/f/YOUR_FORM_ID', {
            method: 'POST', headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
            body: JSON.stringify({ name, contact_way: contact, message: `Пройден квиз. Потери: ${loss}`, service: 'Квиз', agree: true })
          });
          const res = await resp.json();
          if(resp.ok){
            qBody.innerHTML = `<div style="text-align:center;padding:40px 0;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--neon)" stroke-width="2" style="margin:0 auto 16px;"><polyline points="20 6 9 17 4 12"/></svg><h3 style="font-size:20px;margin-bottom:8px;">Спасибо, ${name}!</h3><p style="color:var(--text-2);margin-bottom:20px;">Мы уже изучаем вашу ситуацию. Заявка получена.</p><a href="services.html#calculator" class="btn btn--primary">Получить детальный разбор бесплатно</a></div>`;
          } else {
            showToast(btn, res.message || 'Ошибка', 'error'); btn.disabled = false; btn.textContent = 'Обсудить задачу';
          }
        } catch(e) {
          showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error'); btn.disabled = false; btn.textContent = 'Обсудить задачу';
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
      'audit-express':4000,'audit-full':12000,
      'training':4000,
      'visit-engineer':3000,'work-hour':2500,'ats-setup':25000,'vpn-wireguard':8000,'mail-migration':12000,'ai-pilot':80000
    }, names: {
      'server-select':'Подбор серверного оборудования','server-file':'Файловый сервер','server-domain':'Доменный сервер (AD)','server-dns':'DNS-сервер','server-rdp':'Терминальный сервер (RDS)','server-backup':'Сервер резервного копирования','server-custom':'Настройка под другие задачи',
      'mnt-file':'Обслуживание файлового сервера','mnt-domain':'Обслуживание доменного сервера','mnt-dns':'Обслуживание DNS-сервера','mnt-rdp':'Обслуживание терминального сервера','mnt-backup':'Обслуживание сервера бэкапов',
      'crypto-license':'КриптоПро: продажа лицензии','crypto-install':'КриптоПро: установка','crypto-setup':'КриптоПро: настройка','crypto-ecp':'Клонирование ЭЦП','vipnet-install':'ViPNet: установка','encrypt-full':'Шифрование данных (VeraCrypt)',
      'audit-express':'Экспресс IT-аудит','audit-full':'Полный IT-аудит',
      'training':'Обучение сотрудников (час)',
      'visit-engineer':'Выезд инженера','work-hour':'Час работ','ats-setup':'Настройка АТС до 15 абонентов','vpn-wireguard':'VPN WireGuard для офиса','mail-migration':'Перенос почты на свой сервер','ai-pilot':'Пилот бота в Telegram'
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
        }).catch(()=>{ showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } });
      } catch(e){ showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } }
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
    }
  }catch(e){}

  /* ====== FORMS (generic) ====== */
  try{
    const FORM_ENDPOINT = 'https://formspree.io/f/YOUR_FORM_ID'; // TODO: Заменить на реальный ID
    document.querySelectorAll('form').forEach(function(form){
      if(form.dataset.ffBound) return;
      form.dataset.ffBound = '1';
      form.addEventListener('submit', async function(ev){
        ev.preventDefault();
        const btn = form.querySelector('button[type="submit"]');
        if(btn && !btn.dataset.originalText){ btn.dataset.originalText = btn.textContent; }
        const hp = form.querySelector('input[name="website"]');
        if(hp && hp.value){ return; } // honeypot
        const agree = form.querySelector('input[name="agree"]');
        if(agree && !agree.checked){ showToast(btn, 'Подтвердите согласие', 'error'); return; }
        const required = Array.from(form.querySelectorAll('[required]'));
        for(const el of required){
          if(!String(el.value || '').trim()){ showToast(btn, 'Заполните обязательные поля', 'error'); el.focus(); return; }
        }
        const emails = Array.from(form.querySelectorAll('input[type="email"]'));
        for(const el of emails){
          if(el.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value)){ showToast(btn, 'Укажите корректный email', 'error'); el.focus(); return; }
        }
        const data = {};
        form.querySelectorAll('input,textarea,select').forEach(function(el){
          if(!el.name) return;
          if(el.type === 'checkbox'){ data[el.name] = el.checked; }
          else { data[el.name] = String(el.value || '').trim(); }
        });
        if(!data.service){ data.service = form.getAttribute('name') || 'Форма'; }
        if(btn){ btn.textContent = 'Отправляем...'; btn.disabled = true; }
        try{
          const resp = await fetch(FORM_ENDPOINT, { method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'}, body: JSON.stringify(data) });
          const res = await resp.json().catch(function(){ return {}; });
          if(resp.ok){
            let successEl = form.querySelector('.form-success');
            if(!successEl){
              const nm = form.getAttribute('name');
              if(nm === 'contact-form') successEl = document.getElementById('contactSuccess');
              else if(nm === 'lead-magnet-form') successEl = document.getElementById('leadSuccess');
              else if(nm === 'course-subscriber') successEl = document.getElementById('courseSuccess');
            }
            if(successEl){ successEl.style.display = 'block'; successEl.textContent = 'Заявка ушла. Ответим в течение 15 минут.'; }
            if(typeof window.ymGoal === 'function'){ window.ymGoal('form_submit'); }
            form.reset();
            const fileLink = document.getElementById('fileLink');
            if(fileLink){ fileLink.style.display = 'block'; }
          } else {
            showToast(btn, (res && res.message) || 'Ошибка', 'error');
            if(btn){ btn.disabled = false; btn.textContent = btn.dataset.originalText || 'Отправить'; }
          }
        } catch(e){
          showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error');
          if(btn){ btn.disabled = false; btn.textContent = btn.dataset.originalText || 'Отправить'; }
        }
      });
    });
  }catch(e){}

  /* ====== TOAST HELPER ====== */
  window.showToast = function(btn, msg, type){
    try{
      let toast = document.getElementById('ff-toast');
      if(!toast){ toast = document.createElement('div'); toast.id='ff-toast'; toast.style.cssText='position:absolute;padding:10px 16px;border-radius:10px;font-size:13px;font-weight:600;z-index:9999;transition:opacity .3s;box-shadow:0 4px 16px rgba(0,0,0,0.3);white-space:nowrap;'; document.body.appendChild(toast); }
      toast.textContent = msg;
      toast.style.background = type === 'error' ? '#ff4d4d' : '#00FF88';
      toast.style.color = type === 'error' ? '#fff' : '#000';
      toast.style.opacity = '1';
      // Position near btn if provided
      if(btn && btn.getBoundingClientRect){
        const r = btn.getBoundingClientRect();
        const scrollY = window.scrollY || window.pageYOffset;
        const scrollX = window.scrollX || window.pageXOffset;
        toast.style.top = (r.bottom + scrollY + 8) + 'px';
        toast.style.left = (r.left + scrollX) + 'px';
        toast.style.transform = 'none';
        toast.style.position = 'absolute';
      } else {
        toast.style.position = 'fixed';
        toast.style.bottom = '24px';
        toast.style.left = '50%';
        toast.style.transform = 'translateX(-50%)';
        toast.style.top = '';
      }
      clearTimeout(window._toastTimer);
      window._toastTimer = setTimeout(() => { toast.style.opacity = '0'; }, 6000);
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
    // Close mobile nav when resizing to desktop
    window.addEventListener('resize', function(){ if(window.innerWidth >= 1100 && drawer.classList.contains('is-open')){ drawer.classList.remove('is-open'); burger.classList.remove('active'); drawer.setAttribute('aria-hidden','true'); burger.setAttribute('aria-expanded','false'); document.body.classList.remove('menu-open'); } });
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
  if(root){var rates={basic:900,optimal:1200,extended:1500},plan='basic',pc=root.querySelector('#subComputers'),srv=root.querySelector('#subServers'),printer=root.querySelector('#subPrinters'),fmt=new Intl.NumberFormat('ru-RU');function update(){if(!pc||!srv||!printer)return;var pcs=Number(pc.value),servers=Number(srv.value),printers=Number(printer.value),pcTotal=pcs*rates[plan],serverTotal=servers*3200,printerTotal=printers*300,extras=0;root.querySelectorAll('[data-sub-extra]:checked').forEach(function(el){extras+=Number(el.dataset.price)||0;});var total=pcTotal+serverTotal+printerTotal+extras;root.querySelector('#subComputersValue').textContent=pcs;root.querySelector('#subServersValue').textContent=servers;root.querySelector('#subPrintersValue').textContent=printers;root.querySelector('#subPcLine').textContent=fmt.format(pcTotal)+' ₽';root.querySelector('#subServerLine').textContent=fmt.format(serverTotal)+' ₽';root.querySelector('#subPrinterLine').textContent=fmt.format(printerTotal)+' ₽';root.querySelector('#subExtrasLine').textContent=fmt.format(extras)+' ₽';if(total < 10000) total = 10000; root.querySelector('#subTotal').textContent=fmt.format(total)+' ₽/мес';
    if(total === 10000 && (pcTotal+serverTotal+printerTotal+extras) < 10000) { root.querySelector('#subTotal').textContent=fmt.format(total)+' ₽/мес (минимум по договору)'; } var link=root.querySelector('#subCalcContact');var p=new URLSearchParams({source:'subscription',plan:plan,computers:pcs,servers:servers,printers:printers,monthly:total});link.href='contacts.html?'+p.toString();}
    root.querySelectorAll('[data-sub-plan]').forEach(function(button){button.addEventListener('click',function(){plan=button.dataset.subPlan;root.querySelectorAll('[data-sub-plan]').forEach(function(item){var selected=item===button;item.classList.toggle('is-selected',selected);item.setAttribute('aria-pressed',String(selected));});update();});});[pc,srv,printer].forEach(function(input){if(input)input.addEventListener('input',update);});root.querySelectorAll('[data-sub-extra]').forEach(function(input){input.addEventListener('change',update);});update();}
  var estimator=document.querySelector('#calculator .calc');
  if(estimator){estimator.querySelectorAll('.calc__service').forEach(function(button){button.setAttribute('aria-pressed',String(button.classList.contains('active')));});}
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
      { t: '[ OK ] Мониторинг 24/7 · SLA 99,5%', cls: 'ok2' },
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
      el.textContent = target + suffix;
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
function initTerminalLoading() {
  try {
    const termBody = document.getElementById('terminalBody');
    if (termBody) {
      const items = Array.from(termBody.children);
      items.forEach(el => { el.style.opacity = '0'; el.style.transform = 'translateY(6px)'; el.style.transition = 'opacity 0.35s ease, transform 0.35s ease'; });
      let delay = 100;
      items.forEach((el, i) => {
        setTimeout(() => {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, delay);
        delay += 320;
      });
    }
  } catch(e) {}
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTerminalLoading);
} else {
  initTerminalLoading();
}




/* ====== SATURDAY SCENARIOS (10, random, no repeat) ====== */
(function(){
  const scenarios = [
    [
      {t:'00:00 — Сервер ушёл в ребут. Офис спит.', d:'Ничего не предвещало.', c:'danger'},
      {t:'00:15 — F&F получил алерт. Инженер уже с ноутбуком.', d:'Реакция от 15 минут — норма.', c:'gold'},
      {t:'00:40 — Причина найдена. Перезапуск сервиса.', d:'Сервис работает. Проверяем логи.', c:'gold'},
      {t:'01:10 — Сервис работает. Логи чисты.', d:'Всё под контролем.', c:'gold'},
      {t:'08:00 — Офис приходит. Никто ничего не заметил.', d:'IT-контур для бизнеса. Казань.', c:'neon'}
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
    if (line) container.appendChild(line);
    // reveal one by one with effects
    let delay = 100;
    scen.forEach((s, i) => {
      setTimeout(() => {
        const div = document.createElement('div');
        div.className = 'sat-line ' + s.c;
        const dotColor = s.c === 'danger' ? '#ff4d4d' : (s.c === 'neon' ? 'var(--neon)' : 'var(--gold-light)');
        div.innerHTML = '<span class="sat-dot" style="background:'+dotColor+';color:'+dotColor+';"></span>'
          + '<div class="sat-time">' + s.t + '</div>'
          + '<div class="sat-desc">' + s.d + '</div>';
        container.appendChild(div);
        requestAnimationFrame(() => { div.classList.add('visible'); });
      }, delay);
      delay += 500;
    });
  };
  // Show a random scenario on first visit
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function(){ setTimeout(runSaturdayScenario, 800); });
  } else {
    setTimeout(runSaturdayScenario, 800);
  }
})();


/* ====== INFRA SCHEME 3D CAROUSEL ====== */
document.addEventListener('DOMContentLoaded', () => {
  const stage = document.querySelector('.scheme-stage');
  const carousel = document.querySelector('.scheme-carousel');
  const cards = document.querySelectorAll('.scheme-card');
  const tags = document.querySelectorAll('.scheme-tag');
  const btnPrev = document.getElementById('schemePrev');
  const btnNext = document.getElementById('schemeNext');
  if(!stage || !carousel || !cards.length) return;

  let currentIndex = 0;
  const totalCards = cards.length;
  const angleStep = 360 / totalCards;
  const radius = 220;

  cards.forEach((card, index) => {
    const angle = index * angleStep;
    card.style.transform = 'rotateY(' + angle + 'deg) translateZ(' + radius + 'px)';
  });

  function updateCarousel() {
    const rotateAngle = currentIndex * -angleStep;
    carousel.style.transform = 'rotateY(' + rotateAngle + 'deg)';
    tags.forEach((tag, i) => { tag.classList.toggle('active', i === currentIndex); });
  }

  if(btnNext) btnNext.addEventListener('click', () => { currentIndex = (currentIndex + 1) % totalCards; updateCarousel(); });
  if(btnPrev) btnPrev.addEventListener('click', () => { currentIndex = (currentIndex - 1 + totalCards) % totalCards; updateCarousel(); });

  tags.forEach((tag, index) => {
    tag.addEventListener('click', () => { currentIndex = index; updateCarousel(); });
  });

  stage.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' && btnNext) btnNext.click();
    if (e.key === 'ArrowLeft' && btnPrev) btnPrev.click();
  });

  let startX = 0, isDragging = false;
  stage.addEventListener('pointerdown', (e) => { startX = e.clientX; isDragging = true; });
  stage.addEventListener('pointermove', (e) => {
    if (!isDragging) return;
    const deltaX = e.clientX - startX;
    if (deltaX > 50) { if(btnPrev) btnPrev.click(); isDragging = false; }
    if (deltaX < -50) { if(btnNext) btnNext.click(); isDragging = false; }
  });
  stage.addEventListener('pointerup', () => { isDragging = false; });
  stage.addEventListener('pointerleave', () => { isDragging = false; });

  cards.forEach(card => {
    const btn = card.querySelector('.scheme-card__btn');
    const calcKey = card.getAttribute('data-calc-key');
    if (btn && calcKey) {
      btn.addEventListener('click', () => {
        const calcCheckbox = document.querySelector('.calc__service[data-key="' + calcKey + '"]');
        if (calcCheckbox) {
          const isActive = calcCheckbox.classList.contains('active');
          calcCheckbox.click();
          if (!isActive) { btn.textContent = '✓ В смете'; btn.classList.add('added'); }
          else { btn.textContent = 'Добавить в смету'; btn.classList.remove('added'); }
        } else {
          btn.textContent = '✓ Выбрано';
          btn.classList.add('added');
        }
      });
    }
  });

  updateCarousel();
});


/* ====== AUDIT FORM ====== */
try {
  const auditForm = document.getElementById('audit-form');
  if (auditForm) {
    auditForm.addEventListener('submit', function(ev) {
      ev.preventDefault();
      const btn = auditForm.querySelector('button[type="submit"]');
      const name = (auditForm.querySelector('#audit-name')||{}).value || '';
      const phone = (auditForm.querySelector('#audit-phone')||{}).value || '';
      const agree = (auditForm.querySelector('#audit-agree')||{}).checked;
      // Validation
      let hasErr = false;
      if (!name.trim()) { showToast(btn, 'Укажите имя', 'error'); hasErr = true; }
      const phoneClean = phone.replace(/\D/g, '');
      if (phoneClean.length < 10) {
        const phoneInput = auditForm.querySelector('#audit-phone');
        if (phoneInput) { phoneInput.classList.add('border-error'); phoneInput.style.borderColor = '#D32F2F'; }
        showToast(btn, 'Неверный телефон', 'error');
        hasErr = true;
      }
      if (!agree) { showToast(btn, 'Подтвердите согласие', 'error'); hasErr = true; }
      if (hasErr) return;
      // Submit
      if (btn) { btn.textContent = 'Отправляем...'; btn.disabled = true; }
      fetch('https://formspree.io/f/YOUR_FORM_ID', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ name: name.trim(), phone: phone.trim(), service: auditForm.querySelector('#audit-service').value, source: auditForm.querySelector('input[name="source"]').value, agree: true })
      }).then(r => r.json()).then(res => {
        if (res && res.ok === true) {
          showToast(btn, 'Заявка отправлена! Заявка получена.', 'success');
          auditForm.reset();
        } else {
          showToast(btn, (res && res.message) || 'Ошибка отправки', 'error');
        }
        if (btn) { btn.disabled = false; btn.textContent = 'Получить расчёт'; }
      }).catch(() => {
        showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error');
        if (btn) { btn.disabled = false; btn.textContent = 'Получить расчёт'; }
      });
    });
    // Clear red border on input
    const phoneInput = auditForm.querySelector('#audit-phone');
    if (phoneInput) {
      phoneInput.addEventListener('input', function() { this.classList.remove('border-error'); this.style.borderColor = ''; });
    }
  }
} catch(e) {}



/* ====== YANDEX METRIKA (placeholder) ====== */
// Замените XXXXXX на реальный номер счётчика после регистрации.
// (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
// m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
// (window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");
// ym(XXXXXX,"init",{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});

window.ffTrack = function(eventName, params){
  try {
    if(typeof ym === 'function' && window.YM_COUNTER_ID){
      ym(window.YM_COUNTER_ID, 'reachGoal', eventName, params || {});
    }
  } catch(e){}
};

window.trackPhoneClick = function(){ window.ffTrack('phone_click'); };
window.trackTelegramClick = function(){ window.ffTrack('telegram_click'); };
window.trackFormSuccess = function(formName){ window.ffTrack('form_success', { form: formName || 'unknown' }); };
window.trackCalculatorOpen = function(){ window.ffTrack('calculator_open'); };
window.trackQuizComplete = function(){ window.ffTrack('quiz_complete'); };

// Wire tracking to phone/telegram links
document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('a[href^="tel:"]').forEach(function(a){
    a.addEventListener('click', function(){ window.trackPhoneClick(); });
  });
  document.querySelectorAll('a[href*="t.me"]').forEach(function(a){
    a.addEventListener('click', function(){ window.trackTelegramClick(); });
  });
});


/* SECURITY CHECKLIST */
try {
  const checklist = document.getElementById('securityChecklist');
  if (checklist) {
    const countEl = document.getElementById('securityChecklistCount');
    const checkboxes = checklist.querySelectorAll('input[data-security-check]');
    function updateCount() {
      const checked = checklist.querySelectorAll('input[data-security-check]:checked').length;
      if (countEl) countEl.textContent = checked + ' / ' + checkboxes.length;
    }
    checkboxes.forEach(cb => {
      cb.addEventListener('change', updateCount);
    });
    updateCount();
  }
} catch(e) { console.error('Security checklist', e); }


  /* ====== EXIT-INTENT POPUP (desktop) ====== */
  try{
    if(!sessionStorage.getItem('ff_exit_shown')){
      let shown = false;
      document.addEventListener('mouseleave', function(ev){
        if(shown) return;
        if(ev.clientY > 10) return;
        shown = true;
        try{ sessionStorage.setItem('ff_exit_shown','1'); }catch(e){}
        const prefix = (location.pathname.indexOf('/blog/')>-1 || location.pathname.indexOf('/services/')>-1 || location.pathname.indexOf('/cases/')>-1) ? '../' : '';
        const modal = document.createElement('div');
        modal.id = 'ff-exit-modal';
        modal.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:9999;display:flex;align-items:center;justify-content:center;';
        modal.innerHTML = '<div style="background:#141925;border:1px solid #D4AF37;border-radius:16px;padding:24px;max-width:400px;width:90%;text-align:center;position:relative;">' +
          '<button id="ff-exit-close" type="button" aria-label="Закрыть" style="position:absolute;top:8px;right:12px;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;line-height:1;">×</button>' +
          '<h3 style="color:#D4AF37;margin:0 0 8px;font-size:18px;">Уходите? Заберите чек-лист</h3>' +
          '<p style="color:#9AA4B2;font-size:14px;margin:0 0 16px;">7 признаков, что ваши бэкапы не работают. Проверьте за 10 минут.</p>' +
          '<a href="' + prefix + 'backup-checklist.html" class="btn btn--primary" style="display:inline-block;margin-bottom:8px;">Скачать чек-лист</a>' +
          '<br><a href="' + prefix + 'contacts.html" style="color:#D4AF37;font-size:13px;">Или получите расчёт стоимости за 15 минут →</a>' +
        '</div>';
        document.body.appendChild(modal);
        const closeBtn = document.getElementById('ff-exit-close');
        if(closeBtn){ closeBtn.addEventListener('click', function(){ modal.remove(); }); }
        modal.addEventListener('click', function(e){ if(e.target === modal){ modal.remove(); } });
      });
    }
  }catch(e){}


  /* ====== ANALYTICS GOALS (Yandex.Metrika) ====== */
  try{
    window.YM_COUNTER_ID = window.YM_COUNTER_ID || null;
    window.ymGoal = function(goal){
      try{
        if(typeof ym === 'function' && window.YM_COUNTER_ID){
          ym(window.YM_COUNTER_ID, 'reachGoal', goal);
        }
      }catch(e){}
    };
    // phone click tracking
    document.querySelectorAll('a[href^="tel:"]').forEach(function(a){
      a.addEventListener('click', function(){ window.ymGoal('phone_click'); });
    });
    // calculate button tracking
    document.querySelectorAll('a,button').forEach(function(el){
      if(/Рассчитать/.test(el.textContent || '')){
        el.addEventListener('click', function(){ window.ymGoal('calculate_click'); });
      }
    });
  }catch(e){}


  /* ====== STICKY TELEGRAM BUTTON ====== */
  try{
    const sticky = document.createElement('a');
    sticky.href = 'https://t.me/FathFed';
    sticky.target = '_blank';
    sticky.rel = 'noopener noreferrer';
    sticky.textContent = 'Написать в Telegram';
    sticky.style.cssText = 'position:fixed;bottom:20px;right:20px;z-index:9997;background:#D4AF37;color:#0A0D14;padding:12px 18px;border-radius:999px;font-weight:700;font-size:14px;text-decoration:none;box-shadow:0 4px 12px rgba(0,0,0,.35);';
    function adjustSticky(){ sticky.style.bottom = (window.innerWidth < 1100) ? '72px' : '20px'; }
    adjustSticky();
    window.addEventListener('resize', adjustSticky);
    document.body.appendChild(sticky);
  }catch(e){}

  /* ====== MOBILE BOTTOM BAR VISIBILITY ====== */
  try{
    const mbar = document.getElementById('mobileBottomBar');
    if(mbar){
      function updateMbar(){
        if(window.innerWidth >= 1100){ mbar.classList.remove('is-visible'); return; }
        const total = document.documentElement.scrollHeight || document.body.scrollHeight;
        const scrolled = (window.scrollY + window.innerHeight) / total;
        if(scrolled > 0.45){ mbar.classList.add('is-visible'); } else { mbar.classList.remove('is-visible'); }
      }
      window.addEventListener('scroll', updateMbar, {passive:true});
      window.addEventListener('resize', updateMbar);
      updateMbar();
    }
  }catch(e){}
