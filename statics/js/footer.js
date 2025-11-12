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
        .contact-item i {
          color: #666;
          transition: color 0.3s ease;
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
              <h3>پورتفولیو</h3>
              <p>ایجاد تجربیات دیجیتالی استثنایی که سریع، قابل دسترس، جذاب و واکنش‌گرا هستند.</p>
              <div class="social-links">
                <a href="#" class="social-link" aria-label="GitHub">
                  <i data-feather="github"></i>
                </a>
                <a href="#" class="social-link" aria-label="LinkedIn">
                  <i data-feather="linkedin"></i>
                </a>
                <a href="#" class="social-link" aria-label="Twitter">
                  <i data-feather="twitter"></i>
                </a>
                <a href="#" class="social-link" aria-label="Instagram">
                  <i data-feather="instagram"></i>
                </a>
              </div>
            </div>
            <div class="footer-column">
              <h3>لینک‌های سریع</h3>
              <ul class="footer-links">
                <li><a href="#home" class="footer-link">خانه</a></li>
                <li><a href="#about" class="footer-link">بیوگرافی</a></li>
                <li><a href="#education" class="footer-link">تحصیلات</a></li>
                <li><a href="#languages" class="footer-link">زبان‌ها</a></li>
                <li><a href="#skills" class="footer-link">توانایی‌ها</a></li>
                <li><a href="#projects" class="footer-link">پروژه‌ها</a></li>
                <li><a href="#contact" class="footer-link">تماس</a></li>
              </ul>
            </div>
            <div class="footer-column contact-info">
              <h3>اطلاعات تماس</h3>
              <div class="contact-item">
                <i data-feather="mail"></i>
                <span>example@email.com</span>
              </div>
              <div class="contact-item">
                <i data-feather="phone"></i>
                <span>+98 912 345 6789</span>
              </div>
              <div class="contact-item">
                <i data-feather="map-pin"></i>
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

    // Initialize Feather icons
    setTimeout(() => {
      if (typeof feather !== 'undefined') {
        feather.replace();
      }
    }, 100);
  }
}

customElements.define('portfolio-footer', PortfolioFooter);

