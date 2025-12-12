// Navigation and UI Interactions
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Add animation class when elements come into view
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

document.querySelectorAll('.card, .btn, h2, h3').forEach(el => {
    observer.observe(el);
});

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = 'red';
                    isValid = false;
                } else {
                    input.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('WildGuard loaded');
});


document.addEventListener('click', function(e){
    const a = e.target.closest('a');
    if(!a) return;
    const href = a.getAttribute('href') || '';
    if(href.includes('/sources') || href.endsWith('/sources') || href === 'sources' || href.endsWith('sources.html')){
        try{ sessionStorage.setItem('navigateToSources', '1'); }catch(_){ }
    }
});


document.addEventListener('DOMContentLoaded', function(){
    try{
        if(sessionStorage.getItem('navigateToSources') === '1'){
            const sections = document.querySelectorAll('.sources-section');
            sections.forEach((sec, sIdx) => {
                sec.classList.add('sources-fade');

                const sectionBase = sIdx * 180; 

                // animate the section h2
                const mainH2 = sec.querySelector('h2');
                if(mainH2){
                    mainH2.style.opacity = 0;
                    mainH2.style.transform = 'translateY(8px)';
                    mainH2.style.animation = `fadeInUpSmall 420ms ease ${sectionBase}ms both`;
                }

                // animate subheadings (h3)
                const subheads = sec.querySelectorAll('h3');
                subheads.forEach((h, idx)=>{
                    const d = sectionBase + 120 + idx * 70;
                    h.style.opacity = 0;
                    h.style.transform = 'translateY(8px)';
                    h.style.animation = `fadeInUpSmall 420ms ease ${d}ms both`;
                });

                
                const paras = sec.querySelectorAll('p');
                paras.forEach((p, idx)=>{
                    const d = sectionBase + 160 + (subheads.length * 60) + idx * 70;
                    p.style.opacity = 0;
                    p.style.transform = 'translateY(8px)';
                    p.style.animation = `fadeInUpSmall 420ms ease ${d}ms both`;
                });

                // animate list items with stagger
                const items = sec.querySelectorAll('.sources-list li');
                items.forEach((it, i)=>{
                    const d = sectionBase + 300 + i * 60;
                    it.style.opacity = 0;
                    it.style.transform = 'translateY(8px)';
                    it.style.animation = `fadeInUpSmall 420ms ease ${d}ms both`;
                });
            });

            sessionStorage.removeItem('navigateToSources');
        }
    }catch(_){ }
});


// Simple image for infographics
document.addEventListener('click', function(e) {
    const target = e.target;
    // clicking infographic images
    if (target.matches('.infographic-card img')) {
        const src = target.getAttribute('src');
        const caption = target.closest('.infographic-card').querySelector('figcaption')?.innerText || '';
        const modal = document.getElementById('img-modal');
        const modalImg = document.getElementById('img-modal-img');
        const modalCaption = document.getElementById('img-modal-caption');
        if (modal && modalImg) {
            modalImg.src = src;
            modalCaption.textContent = caption;
            modal.style.display = 'flex';
            modal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
        }
    }

    // clicking close button or backdrop
    if (target.id === 'img-modal-close' || target.classList.contains('img-modal-backdrop')) {
        const modal = document.getElementById('img-modal');
        if (modal) {
            modal.style.display = 'none';
            modal.setAttribute('aria-hidden', 'true');
            const modalImg = document.getElementById('img-modal-img');
            if (modalImg) modalImg.src = '';
            document.body.style.overflow = '';
        }
    }

    // Open contact modal
    if (target.closest && target.closest('#footer-contact-link')) {
        const link = target.closest('#footer-contact-link');
        if (link) {
            try { e.preventDefault(); } catch(_){}
            const cModal = document.getElementById('contact-modal');
            if (cModal) {
                cModal.style.display = 'flex';
                cModal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';
            }
        }
    }

    // clicking close button for contact modal
    if (target.id === 'contact-modal-close' || (target.classList.contains('contact-modal-backdrop') && target.closest('#contact-modal'))) {
        const cm = document.getElementById('contact-modal');
        if (cm) {
            cm.style.display = 'none';
            cm.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }

    // Open privacy modal 
    if (target.closest && target.closest('#footer-privacy-link')) {
        const link = target.closest('#footer-privacy-link');
        if (link) {
            try { e.preventDefault(); } catch(_){}
            const pModal = document.getElementById('privacy-modal');
            if (pModal) {
                pModal.style.display = 'flex';
                pModal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';
            }
        }
    }

    // clicking close button for privacy modal
    if (target.id === 'privacy-modal-close' || (target.classList.contains('contact-modal-backdrop') && target.closest('#privacy-modal'))) {
        const pm = document.getElementById('privacy-modal');
        if (pm) {
            pm.style.display = 'none';
            pm.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }
    }
 });
 
 // Close contact modal with Escape key
document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
        const cm = document.getElementById('contact-modal');
        const im = document.getElementById('img-modal');
        if(cm && cm.style.display === 'flex'){
            cm.style.display = 'none'; cm.setAttribute('aria-hidden','true'); document.body.style.overflow = '';
        }
        if(im && im.style.display === 'flex'){
            im.style.display = 'none'; im.setAttribute('aria-hidden','true'); const modalImg = document.getElementById('img-modal-img'); if (modalImg) modalImg.src = ''; document.body.style.overflow = '';
        }
    }
});