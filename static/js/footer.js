class PortfolioFooter extends HTMLElement {
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
        .footer-container {
          background-color: #0f0f0f;
          color: #cccccc;
          padding: 3rem 0 1.5rem;
          border-top: 1px solid #333;
          transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        :host-context(body.light-theme) .footer-container {
          background-color: #f5f5f5;
          border-top: 1px solid #e0e0e0;
        }
        .container {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 2rem;
        }
        .footer-content {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 2rem;
          margin-bottom: 2rem;
        }
        .footer-column h3 {
          color: #ffffff;
          margin-bottom: 1rem;
          font-size: 1.1rem;
          font-weight: 600;
          transition: color 0.3s ease;
        }
        :host-context(body.light-theme) .footer-column h3 {
          color: #1a1a1a;
        }
        .footer-column p {
          color: #888;
          line-height: 1.6;
          margin-bottom: 1rem;
          transition: color 0.3s ease;
        }
        :host-context(body.light-theme) .footer-column p {
          color: #666;
        }
        .social-links {
          display: flex;
          gap: 0.75rem;
          margin-top: 1rem;
        }
        .social-link {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background-color: #1a1a1a;
          color: #cccccc;
          transition: all 0.3s ease;
          text-decoration: none;
          border: 1px solid #333;
        }
        .social-link:hover {
          background-color: #2a2a2a;
          color: #ffffff;
          transform: translateY(-3px);
          border-color: #444;
        }
        :host-context(body.light-theme) .social-link {
          background-color: #ffffff;
          color: #666;
          border: 1px solid #e0e0e0;
        }
        :host-context(body.light-theme) .social-link:hover {
          background-color: #f0f0f0;
          color: #1a1a1a;
          border-color: #ccc;
        }
        .footer-links {
          list-style: none;
        }
        .footer-link {
          color: #888;
          transition: color 0.3s ease;
          display: block;
          margin-bottom: 0.75rem;
          text-decoration: none;
        }
        .footer-link:hover {
          color: #ffffff;
        }
        :host-context(body.light-theme) .footer-link {
          color: #666;
        }
        :host-context(body.light-theme) .footer-link:hover {
          color: #1a1a1a;
        }
        .contact-info {
          display: flex;
          flex-direction: column;
          gap: 1rem;
        }
        .contact-item {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          color: #888;
          transition: color 0.3s ease;
        }
        .contact-item i,
        .contact-item svg {
          color: #666;
          transition: color 0.3s ease;
          width: 18px;
          height: 18px;
          flex-shrink: 0;
        }
        .social-link svg {
          width: 20px;
          height: 20px;
          stroke: currentColor;
          fill: none;
          stroke-width: 2;
          stroke-linecap: round;
          stroke-linejoin: round;
        }
        .contact-item:hover {
          color: #cccccc;
        }
        .contact-item:hover i {
          color: #888;
        }
        :host-context(body.light-theme) .contact-item {
          color: #666;
        }
        :host-context(body.light-theme) .contact-item:hover {
          color: #1a1a1a;
        }
        :host-context(body.light-theme) .contact-item i {
          color: #999;
        }
        :host-context(body.light-theme) .contact-item:hover i {
          color: #666;
        }
        .copyright {
          text-align: center;
          padding-top: 2rem;
          border-top: 1px solid #333;
          color: #666;
          font-size: 0.875rem;
          transition: color 0.3s ease, border-color 0.3s ease;
        }
        :host-context(body.light-theme) .copyright {
          border-top: 1px solid #e0e0e0;
          color: #999;
        }
        @media (max-width: 768px) {
          .footer-content {
            grid-template-columns: 1fr;
          }
          .container {
            padding: 0 1rem;
          }
        }
      </style>
      <footer class="footer-container">
        <div class="container">
          <div class="footer-content">
            <div class="footer-column">
              <h3>Ali Bahrami</h3>
              <p>شبکه های اجتماعی</p>
              <div class="social-links">
                <a href="https://github.com/alibahrami1376" class="social-link" aria-label="GitHub">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                  </svg>
                </a>
                <a href="https://www.linkedin.com/in/ali-bahrami-90a296168/" class="social-link" aria-label="LinkedIn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                    <rect x="2" y="9" width="4" height="12"></rect>
                    <circle cx="4" cy="4" r="2"></circle>
                  </svg>
                </a>
                <a href="https://t.me/ali_bahramiiii" class="social-link" aria-label="Telegram">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="22" y1="2" x2="11" y2="13"></line>
                    <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                  </svg>
                </a>
                <a href="https://instagram.com/__alii_bahrami__" class="social-link" aria-label="Instagram">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                  </svg>
                </a>
              </div>
            </div>
            <div class="footer-column">
              <h3>لینک‌های سریع</h3>
              <ul class="footer-links">
                <li><a href="#home" class="footer-link">خانه</a></li>
                <li><a href="/blog/" class="footer-link"> وبلاگ</a></li>
                <li><a href="#projects" class="footer-link">پروژه‌ها</a></li>
              </ul>
            </div>
            <div class="footer-column contact-info">
              <h3>اطلاعات تماس</h3>
              <div class="contact-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
                <span>alifbahrami13766@gmail.com</span>
              </div>
              <div class="contact-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
                <span>@ali_bahramiiii</span>
              </div>
              <div class="contact-item">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>تهران، ایران</span>
              </div>
            </div>
          </div>
          <div class="copyright">
            <p>&copy; ${new Date().getFullYear()} پورتفولیو. تمامی حقوق محفوظ است.</p>
          </div>
        </div>
      </footer>
    `;

    // SVG icons are already embedded, no need for Feather initialization
  }
}

customElements.define('portfolio-footer', PortfolioFooter);

