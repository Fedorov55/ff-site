# Эталонная страница — services.html

> Этот документ фиксирует визуальный и структурный эталон для всех страниц сайта F&F.
> Эталонная страница: `services.html`. Все новые и перерабатываемые страницы должны соответствовать этому стандарту.

---

## 1. Общие принципы

- **Тема:** Dark Tech, премиальный. Тёмный фон `#0A0D14`, золото `#D4AF37`, неон `#00FF88`.
- **Светлая тема:** обязательна, переключается кнопкой в хедере, переменные переопределяются в `components.css`.
- **Шрифты:** `Inter` (sans), `JetBrains Mono` (mono/акценты).
- **Адаптивность:** mobile-first, брейкпоинты 480/680/900/1099/1180.
- **Доступность:** WCAG AA, focus-visible, skip-link, reduced-motion.
- **Никаких «100%», «дёшево», «лучшие в мире» в текстах.**

---

## 2. Цветовые токены (`css/tokens.css`)

```css
:root {
  --bg: #0A0D14;
  --bg-2: #11151F;
  --bg-3: #171C29;
  --card: #141926;
  --text: #F2F5FA;
  --text-2: #B6BFCF;
  --muted: #9AA4B2;
  --gold: #D4AF37;
  --gold-light: #E8C44D;
  --gold-bright: #FFF4C4;
  --gold-soft: rgba(212,175,55,.1);
  --neon: #00FF88;
  --border: rgba(130,140,158,.14);
  --border-gold: rgba(212,175,55,.35);
  --shadow: 0 30px 60px -20px rgba(0,0,0,.75);
  --radius: 16px;
  --radius-btn: 12px;
  --radius-sm: 12px;
}
```

Светлая тема переопределяется в `components.css` через `[data-theme="light"]`.

---

## 3. Хедер

### Разметка
```html
<header class="header">
  <div class="container header__inner">
    <a href="index.html" class="logo" aria-label="F&F — IT-контур для бизнеса">
      <img src="img/logo-44.webp?v=128" alt="F&F" class="logo__img" width="44" height="44" fetchpriority="high" loading="eager" decoding="async">
      <span class="logo__text-wrap">
        <span class="logo__brand">F&amp;F-IT</span>
      </span>
    </a>
    <nav class="nav" aria-label="Основная навигация">
      <a href="services.html" class="nav__direct">Услуги</a>
      <a href="cases.html" class="nav__direct">Кейсы</a>
      <a href="incidents/incident.html" class="nav__direct" style="color:var(--danger);font-weight:700;">Авария</a>
      <a href="company/about.html" class="nav__direct">О компании</a>
      <div class="nav__item">
        <button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" data-nav-trigger>Ресурсы<svg viewBox="0 0 20 20" aria-hidden="true"><path d="m5 7 5 5 5-5"/></svg></button>
        <div class="dropdown" id="menu-resources">
          <a href="blog.html" class="dropdown__link">Блог</a>
          <a href="articles.html" class="dropdown__link">Статьи</a>
          <a href="resources/research.html" class="dropdown__link">Исследования</a>
        </div>
      </div>
      <a href="prices.html" class="nav__direct">Цены</a>
      <a href="contacts.html" class="nav__direct">Контакты</a>
    </nav>
    <div class="header__actions">
      <a href="tel:+79012655252" class="header__phone">+7 (901) 265-52-52</a>
      <button class="theme-toggle" id="themeToggle" type="button" aria-label="Переключить тему">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      </button>
      <button class="burger" id="burgerBtn" aria-label="Открыть меню" type="button" aria-expanded="false" aria-controls="mobileNav">...</button>
    </div>
  </div>
</header>
```

### Правила
- Бренд: `F&F-IT` — крупный (20px), золотой с переливом `goldShimmer`, без подчёркивания.
- Зелёная точка `.dot-live` — только в `section__label` рядом с `F&F · IT для бизнеса`.
- Выпадающее меню «Ресурсы» открывается при наведении (hover) и закрывается при уходе мыши.
- Навигация при наведении: цвет текста `#E8C44D`, выезжающая золотая линия снизу с `box-shadow: 0 0 8px rgba(212,175,55,.6)`.

```css
.nav__direct, .nav__link { position: relative; transition: color .3s ease; }
.nav__direct::after, .nav__link::after { content: ''; position: absolute; bottom: -6px; left: 0; width: 100%; height: 2px; background-color: #D4AF37; border-radius: 2px; transform: scaleX(0); transform-origin: right; transition: transform .3s ease, box-shadow .3s ease; }
.nav__direct:hover, .nav__link:hover { color: #E8C44D; }
.nav__direct:hover::after, .nav__link:hover::after { transform: scaleX(1); transform-origin: left; box-shadow: 0 0 8px rgba(212,175,55,.6); }
```

---

## 4. Футер

### Разметка
```html
<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__col footer__brand">
      <div class="footer__brand-row">
        <a href="index.html" class="logo" aria-label="F&F — IT-контур для бизнеса">
          <img src="img/logo-44.webp?v=128" alt="F&F" class="logo__img" width="44" height="44" loading="lazy" decoding="async">
        </a>
        <span class="logo__brand">F&amp;F-IT</span>
      </div>
      <p class="footer__slogan">Ваш IT-контур под контролем. Серверы, инфраструктура, безопасность, криптография. Казань и вся Россия.</p>
    </div>
    <div class="footer__col">
      <a href="services.html" class="footer__heading footer__heading--link">Услуги</a>
      <div class="footer__links-grid">
        <div class="footer__subcol">
          <a href="servers.html">Серверы под ключ</a>
          <a href="infrastructure/infrastructure.html">IT-инфраструктура</a>
          <a href="security/security.html">Безопасность</a>
          <a href="support.html">Обслуживание</a>
        </div>
        <div class="footer__subcol">
          <a href="cases.html">Кейсы</a>
          <a href="blog.html">Блог</a>
          <a href="company/about.html">О компании</a>
          <a href="incidents/incident.html">Авария</a>
          <a href="contacts.html">Контакты</a>
        </div>
      </div>
    </div>
    <div class="footer__col">
      <h4 class="footer__heading">Контакты</h4>
      <a href="tel:+79012655252">+7 (901) 265-52-52</a>
      <a href="mailto:FathFed@yandex.ru">FathFed@yandex.ru</a>
      <a href="https://t.me/FathFed" target="_blank" rel="noopener">Telegram @FathFed</a>
      <a href="https://max.ru/FathFed" target="_blank" rel="noopener">MAX: FathFed</a>
    </div>
  </div>
  <div class="container">
    <div class="footer__bottom">
      <div class="footer__legal">Самозанятый: Фатхутдинов Булат Ильмирович · ИНН: 165506822661<br>Деятельность: услуги по установке и настройке ПО · ОКВЭД 62.09</div>
      <div class="footer__copy">© 2026 F&F. Все права защищены.</div>
      <div class="footer__region">Работаем по Казани и всей России · Удалённо и с выездом</div>
      <div class="footer__links">
        <a href="legal/privacy.html" class="btn btn--ghost btn--sm">Политика ПДн</a>
        <a href="legal/cookie.html" class="btn btn--ghost btn--sm">Cookie</a>
        <a href="legal/terms.html" class="btn btn--ghost btn--sm">Условия пользования</a>
      </div>
    </div>
  </div>
</footer>
```

### Правила
- Слоган: JetBrains Mono, 400, по центру под лого/брендом.
- «Услуги» — ссылка-заголовок (21px, золотой), над левым столбцом ссылок.
- Ссылки в 2 колонки, по центру.
- Контакты — правая колонка.
- Нижний блок: центрирован, без подчёркиваний, кнопки маленькие (34px высота).

```css
.footer__inner { display: grid; grid-template-columns: 1.4fr repeat(2, 1fr); gap: 32px; align-items: start; }
.footer__col { display: flex; flex-direction: column; gap: 8px; align-items: center; text-align: center; }
.footer__brand-row { display: flex; align-items: center; gap: 12px; justify-content: center; }
.footer__slogan { font-family: 'JetBrains Mono', monospace; font-weight: 400; text-align: center; }
.footer__links-wrap { display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px 24px; justify-items: center; }
.footer__subcol { display: flex; flex-direction: column; gap: 6px; align-items: center; }
.footer__heading--link { font-size: 21px; font-weight: 800; color: var(--gold-light); text-decoration: none; }
.footer__bottom { display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center; }
.footer a { text-decoration: none !important; }
.footer__links .btn--sm { min-height: 34px; padding: 6px 12px; font-size: 12px; }
```

---

## 5. Карточки (Проблемы и Услуги)

### Разметка карточки
```html
<a href="..." class="service-card fade-up" style="text-decoration:none;">
  <div class="service-card__header">
    <div class="why-card__icon-box">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">...</svg>
    </div>
    <span class="why-card__bg-num">01</span>
  </div>
  <h3 class="service-card__title">Заголовок</h3>
  <p class="service-card__text">Описание с цифрами.</p>
</a>
```

### Правила
- Заголовок карточки: золотой (`var(--gold-light)`).
- Текст карточки: белый (`var(--text)`).
- Иконка: 44×44px, скругление 10px, градиентный фон `linear-gradient(135deg, rgba(0,255,136,0.1), rgba(212,175,55,0.1))`, рамка `1px solid rgba(212,175,55,0.4)`, иконка `#D4AF37`.
- Фоновая цифра: `position: absolute; top: 16px; right: 20px; font-size: 48px; font-weight: 800; color: rgba(255,255,255,0.03)`.
- При наведении: рамка `rgba(212,175,55,0.3)`, `box-shadow: 0 0 20px rgba(212,175,55,0.15)`, `transform: translateY(-2px)`.
- Активная карточка: рамка `#D4AF37`, свечение, фон `#161A23`.

```css
.service-card { position: relative; }
.service-card__header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
.why-card__icon-box { width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, rgba(0,255,136,0.1), rgba(212,175,55,0.1)); border: 1px solid rgba(212,175,55,0.4); }
.why-card__icon-box svg { width: 20px; height: 20px; color: #D4AF37; stroke-width: 2; }
.why-card__bg-num { position: absolute; top: 16px; right: 20px; font-size: 48px; font-weight: 800; color: rgba(255,255,255,0.03); line-height: 1; }
.service-card__title { color: var(--gold-light); font-size: 22px; font-weight: 700; margin: 0 0 8px; }
.service-card__text { color: var(--text); font-size: 15px; line-height: 1.6; margin: 0 0 16px; flex: 1; }
```

---

## 6. Кнопки

- Основная (`.btn--primary`): золотой фон `#D4AF37`, текст `#0A0D14`, при наведении — пересвет `goldShimmer`.
- Вторичная (`.btn--ghost`): прозрачная, рамка `var(--border)`, при наведении — золотая рамка.
- Маленькая (`.btn--sm`): высота 34px, padding 6px 12px, шрифт 12px.

```css
.btn--primary, .header__cta { position: relative; overflow: hidden; }
.btn--primary:hover, .header__cta:hover { background: linear-gradient(120deg, var(--gold) 0%, var(--gold-light) 50%, var(--gold) 100%); background-size: 200% 100%; animation: goldShimmer 1.2s ease-in-out; }
@keyframes goldShimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
```

---

## 7. Блок «Смотрите также»

- Заголовок: 28px, жирный, по центру.
- Кнопки: 15px, padding 14px 24px.
- Отступы: сверху 0, снизу 32px.
- Контейнер по центру.

```css
.section.u-pt-0 { padding-top: 0 !important; padding-bottom: 32px; }
.u-title-16 { font-size: 28px !important; font-weight: 800 !important; color: var(--text) !important; text-align: center; }
.u-max-760 { margin: 0 auto; text-align: center; }
.u-flex { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
```

---

## 8. FAQ

- Классы: `faq__list`, `faq__item`, `faq__question`, `faq__answer`.
- Вопрос: золотой `+` справа, поворачивается на 45° при открытии.
- Ответ: анимация `faqSlide 0.35s ease-out`.

---

## 9. Чек-лист для новой страницы

1. Подключить `tokens.css` → `critical.css` → `style.css` → `components.css`.
2. Использовать стандартный хедер и футер из этого документа.
3. Карточки — с иконками, фоновыми цифрами, золотыми заголовками, белым текстом.
4. FAQ — стандартные классы.
5. Кнопки — с золотым пересветом при наведении.
6. Проверить светлую тему.
7. Запустить `check-site.py`.
8. Закоммитить и запушить.

---

*Эталон зафиксирован: 2026-11-19. Страница-эталон: `services.html`.*
PY