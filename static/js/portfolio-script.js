// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const headerHeight = 80;
            const targetPosition = targetElement.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Update URL without page reload (Dynamic URL)
            if (history.pushState) {
                history.pushState(null, null, targetId);
            }
        }
    });
});

// Handle browser back/forward buttons
window.addEventListener('popstate', function(e) {
    const hash = window.location.hash;
    if (hash) {
        const targetElement = document.querySelector(hash);
        if (targetElement) {
            const headerHeight = 80;
            const targetPosition = targetElement.offsetTop - headerHeight;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    }
});

// Update URL on scroll (Dynamic URL)
let scrollTimeout;
window.addEventListener('scroll', () => {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 150;
        
        sections.forEach(section => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            const id = section.getAttribute('id');
            
            if (scrollPos >= top && scrollPos < bottom) {
                if (history.pushState && window.location.hash !== `#${id}`) {
                    history.pushState(null, null, `#${id}`);
                }
            }
        });
    }, 100);
});

// Handle initial hash on page load
window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash;
    if (hash) {
        setTimeout(() => {
            const targetElement = document.querySelector(hash);
            if (targetElement) {
                const headerHeight = 80;
                const targetPosition = targetElement.offsetTop - headerHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }, 100);
    }
});

// // Form submission handling
// const contactForm = document.getElementById('contactForm');
// if (contactForm) {
//     contactForm.addEventListener('submit', function(e) {
//         e.preventDefault();
        
//         const name = document.getElementById('name').value;
//         const email = document.getElementById('email').value;
//         const subject = document.getElementById('subject') ? document.getElementById('subject').value : '';
//         const message = document.getElementById('message').value;
        
//         if (name && email && message) {
//             // In a real application, you would send this data to a server
//             alert('ممنون از پیام شما! به زودی با شما تماس خواهم گرفت.');
//             contactForm.reset();
//         } else {
//             alert('لطفاً تمام فیلدها را پر کنید.');
//         }
//     });
// }

// Intersection Observer for scroll animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
        }
    });
}, observerOptions);

// Observe sections for animation
document.querySelectorAll('section, .project-card, .skill-card, .education-item, .language-item').forEach(element => {
    observer.observe(element);
});

// Update active navigation link on scroll
const updateActiveNavLink = () => {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 150;
    
    sections.forEach(section => {
        const top = section.offsetTop;
        const bottom = top + section.offsetHeight;
        const id = section.getAttribute('id');
        
        if (scrollPos >= top && scrollPos < bottom) {
            // Update links in main document
            document.querySelectorAll(`a[href="#${id}"]`).forEach(link => {
                document.querySelectorAll('a[href^="#"]').forEach(l => {
                    if (l.classList.contains('nav-link') || l.classList.contains('footer-link')) {
                        l.classList.remove('active');
                    }
                });
                if (link.classList.contains('nav-link') || link.classList.contains('footer-link')) {
                    link.classList.add('active');
                }
            });
        }
    });
};

window.addEventListener('scroll', updateActiveNavLink);
updateActiveNavLink();

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    const body = document.body;
    
    // Apply transition after initial load
    setTimeout(() => {
        body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
    }, 100);
    
    if (savedTheme === 'light') {
        body.classList.add('light-theme');
        body.classList.remove('dark-theme');
    } else {
        body.classList.add('dark-theme');
        body.classList.remove('light-theme');
    }
});

// Listen for theme changes and update all components
window.addEventListener('themechange', (e) => {
    // Force re-render of components if needed
    const theme = e.detail.theme;
    console.log(`Theme changed to: ${theme}`);
});

