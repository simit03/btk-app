/**
 * Homepage JavaScript
 * AI Matematik Asistanı Ana Sayfa
 */

class HomeApp {
    constructor() {
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.initializeAnimations();
        console.log('🏠 HomeApp initialized');
    }
    
    setupEventListeners() {
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
        
        // Add hover effects to cards
        this.setupCardHoverEffects();
        
        // Add click effects to buttons
        this.setupButtonEffects();
        
        // Add scroll animations
        this.setupScrollAnimations();
    }
    
    initializeAnimations() {
        // Animate elements on page load
        this.animateOnLoad();
        
        // Setup floating elements
        this.setupFloatingElements();
        
        // Setup cat animations
        this.setupCatAnimations();
    }
    
    setupCardHoverEffects() {
        const cards = document.querySelectorAll('.grade-card, .feature-card');
        
        cards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-10px) scale(1.02)';
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) scale(1)';
            });
        });
    }
    
    setupButtonEffects() {
        const buttons = document.querySelectorAll('.cta-button');
        
        buttons.forEach(button => {
            button.addEventListener('click', (e) => {
                // Add ripple effect
                const ripple = document.createElement('span');
                const rect = button.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.classList.add('ripple');
                
                button.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });
    }
    
    setupScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);
        
        // Observe elements for scroll animations
        const animateElements = document.querySelectorAll('.grade-card, .feature-card, .hero-content, .cta-content');
        animateElements.forEach(el => {
            observer.observe(el);
        });
    }
    
    animateOnLoad() {
        // Animate hero section
        const heroElements = document.querySelectorAll('.hero-title, .hero-subtitle, .feature-item, .hero-cat-container');
        
        heroElements.forEach((el, index) => {
            setTimeout(() => {
                el.classList.add('fade-in');
            }, index * 200);
        });
    }
    
    setupFloatingElements() {
        const floatingElements = document.querySelectorAll('.floating-element');
        
        floatingElements.forEach((element, index) => {
            // Add random movement
            setInterval(() => {
                const x = Math.random() * 20 - 10;
                const y = Math.random() * 20 - 10;
                element.style.transform = `translate(${x}px, ${y}px) rotate(${Math.random() * 360}deg)`;
            }, 3000 + index * 500);
        });
    }
    
    setupCatAnimations() {
        const cat = document.querySelector('.hero-cat');
        if (!cat) return;
        
        // Add mouse tracking for cat eyes
        this.setupCatEyeTracking();
        
        // Add tail wagging animation
        this.setupTailWagging();
    }
    
    setupCatEyeTracking() {
        const leftPupil = document.querySelector('.hero-pupil-left');
        const rightPupil = document.querySelector('.hero-pupil-right');
        const cat = document.querySelector('.hero-cat');
        
        if (!leftPupil || !rightPupil || !cat) return;
        
        document.addEventListener('mousemove', (e) => {
            const catRect = cat.getBoundingClientRect();
            const catCenterX = catRect.left + catRect.width / 2;
            const catCenterY = catRect.top + catRect.height / 2;
            
            const mouseX = e.clientX - catCenterX;
            const mouseY = e.clientY - catCenterY;
            
            const distance = Math.sqrt(mouseX * mouseX + mouseY * mouseY);
            const maxDistance = 300;
            const intensity = Math.min(distance / maxDistance, 1);
            
            const maxMovement = 3;
            const leftPupilX = (mouseX / maxDistance) * maxMovement * intensity;
            const leftPupilY = (mouseY / maxDistance) * maxMovement * intensity;
            const rightPupilX = (mouseX / maxDistance) * maxMovement * intensity;
            const rightPupilY = (mouseY / maxDistance) * maxMovement * intensity;
            
            leftPupil.style.transform = `translate(${leftPupilX}px, ${leftPupilY}px)`;
            rightPupil.style.transform = `translate(${rightPupilX}px, ${rightPupilY}px)`;
        });
    }
    
    setupTailWagging() {
        const tail = document.querySelector('.hero-tail');
        if (!tail) return;
        
        setInterval(() => {
            tail.style.transform = 'rotate(15deg)';
            setTimeout(() => {
                tail.style.transform = 'rotate(-15deg)';
            }, 500);
        }, 2000);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new HomeApp();
});

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    .fade-in {
        animation: fadeIn 0.8s ease-out forwards;
    }
    
    .animate-in {
        animation: slideUp 0.6s ease-out forwards;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .grade-card, .feature-card {
        opacity: 0;
        transform: translateY(30px);
    }
    
    .grade-card.animate-in, .feature-card.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    .hero-content {
        opacity: 0;
        transform: translateY(20px);
    }
    
    .hero-content.fade-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    .cta-content {
        opacity: 0;
        transform: scale(0.9);
    }
    
    .cta-content.animate-in {
        opacity: 1;
        transform: scale(1);
    }
`;
document.head.appendChild(style); 