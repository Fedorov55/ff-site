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
        fetch('', { method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'},
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
      } catch{ showToast(btn, 'Не отправилось. Позвоните +7 (901) 265-52-52 или напишите в Telegram', 'error'); if(btn){ btn.disabled=false; btn.textContent='Расчёт стоимости под вашу задачу'; } }
    };
  }catch(e){ console.error('Calc', e); }