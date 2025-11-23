class PortfolioHeader extends HTMLElement {
  connectedCallback() {
    // خواندن وضعیت لاگین از attributeها
    const isAuth = this.getAttribute('data-is-auth') === 'true';
    const avatarUrl = this.getAttribute('data-avatar') || '';
    const profileUrl = this.getAttribute('data-profile-url') || '/profile/';
    const loginUrl = this.getAttribute('data-login-url') || '/login/';

    // بخش ورود/پروفایل برای گوشه راست (کنار دکمه تم)
    const authButton = isAuth
      ? `
        <a href="${profileUrl}" class="auth-button profile-button">
          <img src="${avatarUrl}" alt="Profile" class="auth-avatar">
        </a>
      `
      : `
        <a href="${loginUrl}" class="auth-button login-button">
          <i data-feather="log-in"></i>
          <span>ورود</span>
        </a>
      `;

    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
        }
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        .header-container {
          background-color: #1a1a1a;
          border-bottom: 1px solid #333;
          position: sticky;
          top: 0;
          z-index: 1000;
          transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        :host-context(body.light-theme) .header-container {
          background-color: #ffffff;
          border-bottom: 1px solid #e0e0e0;
        }
        .container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 2rem;
        }
        nav {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 1.5rem 0;
        }
        .logo {
          font-size: 1.25rem;
          font-weight: 600;
          color: #ffffff;
          text-decoration: none;
          transition: color 0.3s ease;
        }
        .logo:hover {
          color: #888;
        }
        :host-context(body.light-theme) .logo {
          color: #1a1a1a;
        }
        :host-context(body.light-theme) .logo:hover {
          color: #666;
        }
        .nav-links {
          display: flex;
          list-style: none;
          align-items: center;
          gap: 0;
        }
        .nav-link {
          position: relative;
          padding: 0.5rem 1rem;
          color: #cccccc;
          font-weight: 400;
          transition: color 0.3s ease;
          text-decoration: none;
          font-size: 0.95rem;
        }
        .nav-link:hover {
          color: #ffffff;
        }
        :host-context(body.light-theme) .nav-link {
          color: #666;
        }
        :host-context(body.light-theme) .nav-link:hover {
          color: #1a1a1a;
        }
        :host-context(body.light-theme) .nav-link.active {
          color: #1a1a1a;
        }
        .nav-link::after {
          content: '|';
          position: absolute;
          left: 0;
          color: #444;
          font-weight: 300;
        }
        .nav-link:first-child::after {
          display: none;
        }
        .nav-link.active {
          color: #ffffff;
        }


        .header-right {
          display: flex;
          align-items: center;
          gap: 0.75rem;
        }
        .theme-toggle {
          background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
          border: 1px solid #333;
          border-radius: 50%;
          color: #cccccc;
          cursor: pointer;
          padding: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.3s ease;
          position: relative;
          overflow: hidden;
          width: 36px;
          height: 36px;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        .theme-toggle::before {
          content: '';
          position: absolute;
          top: 0;
          left: -100%;
          width: 100%;
          height: 100%;
          background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
          transition: left 0.5s ease;
        }
        .theme-toggle:hover::before {
          left: 100%;
        }
        .theme-toggle:hover {
          color: #ffffff;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
          border-color: #444;
        }
        .theme-toggle:active {
          transform: translateY(0);
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        }
        :host-context(body.light-theme) .theme-toggle {
          background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
          border: 1px solid #e0e0e0;
          color: #666;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        :host-context(body.light-theme) .theme-toggle:hover {
          color: #1a1a1a;
          border-color: #ccc;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        .theme-toggle svg {
          width: 18px;
          height: 18px;
          transition: transform 0.3s ease;
        }
        .theme-toggle:hover svg {
          transform: rotate(15deg) scale(1.1);
        }
        .theme-toggle-text {
          display: none;
        }
        .auth-button {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 0.5rem;
          padding: 0.5rem 1rem;
          border-radius: 50px;
          text-decoration: none;
          transition: all 0.3s ease;
          font-size: 0.9rem;
          font-weight: 500;
          border: 1px solid #333;
          background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
          color: #cccccc;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        .auth-button:hover {
          color: #ffffff;
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
          border-color: #444;
        }
        .auth-button:active {
          transform: translateY(0);
        }
        .auth-button svg {
          width: 16px;
          height: 16px;
        }
        .auth-button span {
          user-select: none;
        }
        .profile-button {
          padding: 0;
          border-radius: 50%;
          width: 36px;
          height: 36px;
          background: transparent;
          border: 2px solid #cccccc;
        }
        .auth-avatar {
          width: 100%;
          height: 100%;
          border-radius: 50%;
          object-fit: cover;
        }
        .profile-button:hover {
          border-color: #ffffff;
          transform: scale(1.08);
        }
        :host-context(body.light-theme) .auth-button {
          background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
          border-color: #e0e0e0;
          color: #666;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        :host-context(body.light-theme) .auth-button:hover {
          color: #1a1a1a;
          border-color: #ccc;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        :host-context(body.light-theme) .profile-button {
          border-color: #999999;
        }
        :host-context(body.light-theme) .profile-button:hover {
          border-color: #333333;
        }
        @media (max-width: 768px) {
          .theme-toggle {
            width: 32px;
            height: 32px;
          }
          .auth-button {
            padding: 0.4rem 0.8rem;
            font-size: 0.85rem;
          }
          .profile-button {
            width: 32px;
            height: 32px;
          }
        }
        .mobile-toggle {
          display: none;
          flex-direction: column;
          cursor: pointer;
          gap: 4px;
        }
        .bar {
          width: 25px;
          height: 2px;
          background-color: #cccccc;
          transition: 0.3s;
        }
        :host-context(body.light-theme) .bar {
          background-color: #666;
        }
        :host-context(body.light-theme) .nav-links {
          background-color: #ffffff;
        }
        @media (max-width: 768px) {
          .container {
            padding: 0 1rem;
          }
          .nav-links {
            position: fixed;
            left: -100%;
            top: 70px;
            flex-direction: column;
            background-color: #1a1a1a;
            width: 100%;
            text-align: center;
            transition: 0.3s;
            box-shadow: 0 10px 27px rgba(0, 0, 0, 0.3);
            padding: 2rem 0;
            gap: 0;
          }
          .nav-links.active {
            left: 0;
          }
          .nav-link {
            margin: 1rem 0;
            padding: 1rem;
          }
          .nav-link::after {
            display: none;
          }
          .mobile-toggle {
            display: flex;
          }
          .mobile-toggle.active .bar:nth-child(2) {
            opacity: 0;
          }
          .mobile-toggle.active .bar:nth-child(1) {
            transform: translateY(6px) rotate(45deg);
          }
          .mobile-toggle.active .bar:nth-child(3) {
            transform: translateY(-6px) rotate(-45deg);
          }
        }
      </style>
      <header class="header-container">
        <div class="container">
          <nav>
            <a href="#home" class="logo">Ali Bahrami</a>
            <ul class="nav-links">
              <li><a href="#home" class="nav-link active">خانه</a></li>
              <li><a href="#about" class="nav-link">بیوگرافی</a></li>
              <li><a href="#education" class="nav-link">تحصیلات</a></li>
              <li><a href="#languages" class="nav-link">زبان‌ها</a></li>
              <li><a href="#skills" class="nav-link">توانایی‌ها</a></li>
              <li><a href="#projects" class="nav-link">پروژه‌ها</a></li>
              <li><a href="/blog/" class="nav-link">وبلاگ</a></li>
              <li><a href="#contact" class="nav-link">تماس</a></li>
            </ul>
            <div class="header-right">
              <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
                <i data-feather="moon"></i>
              </button>
              ${authButton}
            </div>
            <div class="mobile-toggle">
              <span class="bar"></span>
              <span class="bar"></span>
              <span class="bar"></span>
            </div>
          </nav>
        </div>
      </header>
    `;

    // Mobile menu toggle
    const mobileToggle = this.shadowRoot.querySelector('.mobile-toggle');
    const navLinks = this.shadowRoot.querySelector('.nav-links');

    mobileToggle.addEventListener('click', () => {
      mobileToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    const links = this.shadowRoot.querySelectorAll('.nav-link');
    links.forEach(link => {
      link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        navLinks.classList.remove('active');

        // Update active class
        links.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      });
    });

    // Theme toggle functionality
    const themeToggle = this.shadowRoot.querySelector('#themeToggle');
    const isDarkMode = localStorage.getItem('theme') !== 'light';

    const updateTheme = (isDark) => {
      const body = document.body;
      const icon = themeToggle.querySelector('i');

      body.style.transition = 'background-color 0.3s ease, color 0.3s ease';

      if (isDark) {
        body.classList.add('dark-theme');
        body.classList.remove('light-theme');
        icon.setAttribute('data-feather', 'sun');
        localStorage.setItem('theme', 'dark');
      } else {
        body.classList.add('light-theme');
        body.classList.remove('dark-theme');
        icon.setAttribute('data-feather', 'moon');
        localStorage.setItem('theme', 'light');
      }

      window.dispatchEvent(new CustomEvent('themechange', {
        detail: { theme: isDark ? 'dark' : 'light' }
      }));

      setTimeout(() => {
        if (typeof feather !== 'undefined') {
          feather.replace();
        }
      }, 50);
    };

    updateTheme(isDarkMode);

    themeToggle.addEventListener('click', () => {
      const currentIsDark = document.body.classList.contains('dark-theme');
      updateTheme(!currentIsDark);
    });

    // Update active link based on scroll position
    const updateActiveLink = () => {
      const sections = document.querySelectorAll('section[id]');
      const scrollPos = window.scrollY + 100;

      sections.forEach(section => {
        const top = section.offsetTop;
        const bottom = top + section.offsetHeight;
        const id = section.getAttribute('id');

        if (scrollPos >= top && scrollPos < bottom) {
          links.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${id}`) {
              link.classList.add('active');
            }
          });
        }
      });
    };

    window.addEventListener('scroll', updateActiveLink);
    updateActiveLink();

    // Initialize feather icons in shadow DOM
    setTimeout(() => {
      if (typeof feather !== 'undefined') {
        feather.replace();
      }
    }, 100);
  }
}

customElements.define('portfolio-header', PortfolioHeader);
