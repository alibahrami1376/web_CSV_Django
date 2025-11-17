class PortfolioHeader extends HTMLElement {
  connectedCallback() {
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
        .theme-toggle {
          background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
          border: 1px solid #333;
          border-radius: 50px;
          color: #cccccc;
          cursor: pointer;
          padding: 0.5rem 1rem;
          margin-left: 1rem;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 0.5rem;
          transition: all 0.3s ease;
          position: relative;
          overflow: hidden;
          min-width: 50px;
          height: 40px;
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
          font-size: 0.85rem;
          font-weight: 500;
          display: none;
          user-select: none;
          white-space: nowrap;
        }
        @media (min-width: 769px) {
          .theme-toggle {
            padding: 0.5rem 1.25rem;
          }
          .theme-toggle-text {
            display: inline;
          }
        }
        @media (max-width: 768px) {
          .theme-toggle {
            min-width: 40px;
            padding: 0.5rem;
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
            <a href="#home" class="logo">پورتفولیو | Portfolio</a>
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
            <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
              <i data-feather="moon"></i>
              <span class="theme-toggle-text" id="themeToggleText">Dark</span>
            </button>
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
      const text = this.shadowRoot.querySelector('#themeToggleText');
      
      // Add transition class for smooth theme change
      body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
      
      if (isDark) {
        body.classList.add('dark-theme');
        body.classList.remove('light-theme');
        icon.setAttribute('data-feather', 'sun');
        if (text) text.textContent = 'Light';
        localStorage.setItem('theme', 'dark');
      } else {
        body.classList.add('light-theme');
        body.classList.remove('dark-theme');
        icon.setAttribute('data-feather', 'moon');
        if (text) text.textContent = 'Dark';
        localStorage.setItem('theme', 'light');
      }
      
      // Dispatch custom event for theme change
      window.dispatchEvent(new CustomEvent('themechange', { 
        detail: { theme: isDark ? 'dark' : 'light' } 
      }));
      
      // Re-initialize feather icons
      setTimeout(() => {
        if (typeof feather !== 'undefined') {
          feather.replace();
        }
      }, 50);
    };

    // Initialize theme and text
    const themeToggleText = this.shadowRoot.querySelector('#themeToggleText');
    if (themeToggleText) {
      themeToggleText.textContent = isDarkMode ? 'Light' : 'Dark';
    }
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

