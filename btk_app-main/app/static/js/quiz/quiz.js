// Quiz Main Module - Orchestrates all quiz functionality
// This file imports all modular quiz JS components

// Import GSAP for animations
// Note: GSAP should be loaded before this file

// Import Quiz Modules
// Note: These modules should be loaded before this main file

class QuizApp {
    constructor() {
        this.currentQuestionIndex = 0;
        this.questions = [];
        this.answers = [];
        this.timeLimit = 60; // seconds per question
        this.isActive = false;
        
        // Modülleri başlat
        this.header = new QuizHeader();
        this.question = new QuizQuestion();
        this.options = new QuizOptions();
        this.controls = new QuizControls();
        this.results = new QuizResults();

        this.init();
    }

    init() {
        this.loadSampleQuestions();
        this.bindEvents();
        this.setupAIChat();
        this.startQuiz();
    }

    setupQuiz() {
        // Check if GSAP is loaded
        if (typeof gsap === 'undefined') {
            console.error('GSAP is required for quiz animations. Please load GSAP before this script.');
            // Show error message to user
            const errorDiv = document.createElement('div');
            errorDiv.style.cssText = 'position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #f44336; color: white; padding: 20px; border-radius: 10px; z-index: 1000;';
            errorDiv.innerHTML = '<h3>Hata</h3><p>GSAP kütüphanesi yüklenemedi. Lütfen sayfayı yenileyin.</p>';
            document.body.appendChild(errorDiv);
            return;
        }

        // Initialize modules
        this.header = new QuizHeader();
        this.question = new QuizQuestion();
        this.options = new QuizOptions();
        this.controls = new QuizControls();
        this.results = new QuizResults();

        // Load sample questions
        this.loadSampleQuestions();
        
        // Bind events
        this.bindEvents();
        
        // Start quiz
        this.startQuiz();
    }

    loadSampleQuestions() {
        this.questions = [
            {
                id: 1,
                number: 1,
                text: "JavaScript'te 'let' ve 'var' arasındaki temel fark nedir?",
                options: [
                    { text: "Hiçbir fark yoktur", feedback: "Yanlış! 'let' ve 'var' arasında önemli farklar vardır." },
                    { text: "let block-scoped, var function-scoped'dur", feedback: "Doğru! let block-scoped, var ise function-scoped'dur." },
                    { text: "var daha modern bir syntax'tır", feedback: "Yanlış! let daha modern bir syntax'tır." },
                    { text: "let sadece sayısal değerler için kullanılır", feedback: "Yanlış! let herhangi bir veri tipi için kullanılabilir." }
                ],
                correctAnswer: 1,
                image: null,
                answered: false,
                animationPlayed: false
            },
            {
                id: 2,
                number: 2,
                text: "CSS'te 'flexbox' layout modelinin ana amacı nedir?",
                options: [
                    { text: "Sadece renk değişiklikleri yapmak", feedback: "Yanlış! Flexbox layout düzenleme için kullanılır." },
                    { text: "Responsive ve esnek layout oluşturmak", feedback: "Doğru! Flexbox responsive ve esnek layout oluşturmak için tasarlanmıştır." },
                    { text: "Sadece animasyonlar için kullanılır", feedback: "Yanlış! Flexbox layout düzenleme için kullanılır." },
                    { text: "Sadece tablo oluşturmak için kullanılır", feedback: "Yanlış! Flexbox genel layout düzenleme için kullanılır." }
                ],
                correctAnswer: 1,
                image: null,
                answered: false,
                animationPlayed: false
            },
            {
                id: 3,
                number: 3,
                text: "HTML5'te semantic elementlerin avantajı nedir?",
                options: [
                    { text: "Sadece görsel iyileştirme sağlar", feedback: "Yanlış! Semantic elementler daha fazla avantaj sağlar." },
                    { text: "SEO ve accessibility iyileştirmesi sağlar", feedback: "Doğru! Semantic elementler SEO ve accessibility açısından önemlidir." },
                    { text: "Sadece performans artışı sağlar", feedback: "Yanlış! Semantic elementler daha fazla avantaj sağlar." },
                    { text: "Sadece kod okunabilirliği artırır", feedback: "Yanlış! Semantic elementler daha fazla avantaj sağlar." }
                ],
                correctAnswer: 1,
                image: null,
                answered: false,
                animationPlayed: false
            }
        ];
    }

    bindEvents() {
        // Listen for option selection
        document.addEventListener('optionSelected', (e) => {
            this.handleOptionSelection(e.detail.optionIndex);
        });

        // Listen for answer submission
        document.addEventListener('submitAnswer', (e) => {
            this.submitAnswer();
        });

        // Listen for question navigation
        document.addEventListener('navigateQuestion', (e) => {
            this.navigateToQuestion(e.detail.index);
        });

        // Listen for skip question
        document.addEventListener('skipQuestion', (e) => {
            this.skipQuestion();
        });

        // Listen for retry quiz
        document.addEventListener('retryQuiz', (e) => {
            this.retryQuiz();
        });
    }

    startQuiz() {
        this.isActive = true;
        this.currentQuestionIndex = 0;
        this.answers = [];
        this.score = 0;
        this.selectedAnswer = null;
        
        // Balık/kılçık simgelerini temizle
        this.clearCatRewards();
        
        // Kontrol: controls ve header null mı?
        if (this.controls) {
            this.controls.setTotalQuestions(this.questions.length);
        }
        if (this.header) {
            this.header.setTotalQuestions(this.questions.length);
        }
        
        this.displayCurrentQuestion();
    }

    displayCurrentQuestion() {
        const currentQuestion = this.questions[this.currentQuestionIndex];
        
        if (!currentQuestion) return;

        // Update header progress
        const progress = ((this.currentQuestionIndex + 1) / this.questions.length) * 100;
        this.header.updateProgress(progress);

        // Display question
        this.question.displayQuestion(currentQuestion);
        
        // Display options
        this.options.displayOptions(currentQuestion.options);
        
        // Update controls
        this.controls.setCurrentQuestion(this.currentQuestionIndex);
    }

    handleOptionSelection(optionIndex) {
        // Store the selected option
        this.answers[this.currentQuestionIndex] = {
            selectedOption: optionIndex,
            timeSpent: 0 // Zamanlayıcı kaldırıldı
        };
    }

    submitAnswer() {
        const currentQuestion = this.questions[this.currentQuestionIndex];
        const userAnswer = this.answers[this.currentQuestionIndex];
        
        if (!userAnswer) {
            alert('Lütfen bir seçenek seçin!');
            return;
        }

        // Eğer bu soru zaten cevaplandıysa, tekrar işlem yapma
        if (this.questions[this.currentQuestionIndex].answered) {
            return;
        }

        // Soruyu cevaplandı olarak işaretle
        this.questions[this.currentQuestionIndex].answered = true;

        const isCorrect = userAnswer.selectedOption === currentQuestion.correctAnswer;
        
        // Show correct/incorrect feedback
        if (isCorrect) {
            this.showCorrectAnswer();
        } else {
            this.showWrongAnswer();
        }

        // Disable options
        this.options.disableOptions();
        
        // Show correct answer
        this.options.showCorrectAnswer(currentQuestion.correctAnswer);
        this.options.showUserAnswer(userAnswer.selectedOption, currentQuestion.correctAnswer);
        
        // Wait a bit then move to next question
        setTimeout(() => {
            this.nextQuestion();
        }, 5000); // 5 saniye bekle
    }

    // --- Kedi ödül/kılçık ekleme fonksiyonları ---
    clearCatRewards() {
        const rewards = document.querySelector('.cat-rewards-top');
        if (rewards) {
            rewards.innerHTML = '';
        }
    }

    addCatReward(type) {
        const rewards = document.querySelector('.cat-rewards-top');
        if (!rewards) return;
        
        let icon;
        if (type === 'fish') {
            icon = document.createElement('span');
            icon.className = 'cat-reward-icon';
            icon.innerHTML = `<svg viewBox='0 0 32 32' width='32' height='32'><ellipse cx='16' cy='16' rx='10' ry='6' fill='#4fc3f7'/><polygon points='26,16 32,12 32,20' fill='#0288d1'/><circle cx='12' cy='16' r='1.5' fill='#fff'/></svg>`;
        } else if (type === 'bone') {
            icon = document.createElement('span');
            icon.className = 'cat-reward-icon';
            icon.innerHTML = `<svg viewBox='0 0 32 32' width='32' height='32'><circle cx='16' cy='16' r='14' fill='#ff4444' stroke='#cc0000' stroke-width='2'/><path d='M10 10 L22 22 M22 10 L10 22' stroke='#ffffff' stroke-width='3' stroke-linecap='round'/></svg>`;
        }
        
        if (icon) {
            rewards.appendChild(icon);
            // Yeni simge eklendiğinde scroll'u sağa kaydır
            rewards.scrollLeft = rewards.scrollWidth;
        }
    }

    // Doğru/yanlış cevap fonksiyonlarına entegre et
    showCorrectAnswer() {
        // Eğer bu soru zaten cevaplandıysa, animasyonları tekrar çalıştırma
        if (this.questions[this.currentQuestionIndex].animationPlayed) {
            return;
        }
        
        // Animasyonun çalıştığını işaretle
        this.questions[this.currentQuestionIndex].animationPlayed = true;
        
        this.addCatReward('fish');
        const cat = document.querySelector('.corner-cat-detailed');
        if (cat) {
            cat.classList.add('happy');
            setTimeout(() => cat.classList.remove('happy'), 1500);
        }
        // Trigger confetti
        this.triggerConfetti();
        
        // Show correct symbol
        this.showCorrectSymbol();
        
        // Show success stars
        this.showSuccessStars();
        this.options.disableOptions();
        this.options.showCorrectAnswer(this.questions[this.currentQuestionIndex].correctAnswer);
        this.options.showUserAnswer(this.answers[this.currentQuestionIndex].selectedOption, this.questions[this.currentQuestionIndex].correctAnswer);
        setTimeout(() => {
            this.nextQuestion();
        }, 5000);
    }

    showWrongAnswer() {
        // Eğer bu soru zaten cevaplandıysa, animasyonları tekrar çalıştırma
        if (this.questions[this.currentQuestionIndex].animationPlayed) {
            return;
        }
        
        // Animasyonun çalıştığını işaretle
        this.questions[this.currentQuestionIndex].animationPlayed = true;
        
        this.addCatReward('bone');
        const cat = document.querySelector('.corner-cat-detailed');
        if (cat) {
            cat.classList.add('sad');
            setTimeout(() => cat.classList.remove('sad'), 1500);
        }
        // Show wrong symbol
        this.showWrongSymbol();
        this.options.disableOptions();
        this.options.showCorrectAnswer(this.questions[this.currentQuestionIndex].correctAnswer);
        this.options.showUserAnswer(this.answers[this.currentQuestionIndex].selectedOption, this.questions[this.currentQuestionIndex].correctAnswer);
        setTimeout(() => {
            this.nextQuestion();
        }, 5000);
    }

    triggerConfetti() {
        // Check if confetti library is loaded
        if (typeof confetti !== 'undefined') {
            // Ana konfeti patlaması - daha uzun süre
            confetti({
                particleCount: 150,
                spread: 90,
                origin: { y: 0.6 },
                colors: ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
            });
            
            // İkinci patlama - 1 saniye sonra
            setTimeout(() => {
                confetti({
                    particleCount: 100,
                    angle: 60,
                    spread: 70,
                    origin: { x: 0 },
                    colors: ['#FF8E53', '#FFD93D', '#6BCF7F', '#4ECDC4', '#45B7D1']
                });
            }, 1000);
            
            // Üçüncü patlama - 2 saniye sonra
            setTimeout(() => {
                confetti({
                    particleCount: 100,
                    angle: 120,
                    spread: 70,
                    origin: { x: 1 },
                    colors: ['#FF6B6B', '#FF8E53', '#FFD93D', '#6BCF7F', '#4ECDC4']
                });
            }, 2000);
            
            // Dördüncü patlama - 3 saniye sonra
            setTimeout(() => {
                confetti({
                    particleCount: 80,
                    spread: 360,
                    origin: { y: 0.3 },
                    colors: ['#FFD700', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
                });
            }, 3000);
        }
    }

    showSuccessStars() {
        const starsContainer = document.createElement('div');
        starsContainer.className = 'success-stars';
        
        // 20 yıldız oluştur
        for (let i = 0; i < 20; i++) {
            const star = document.createElement('div');
            star.className = 'success-star';
            star.textContent = '⭐';
            star.style.left = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 2 + 's';
            star.style.animationDuration = (3 + Math.random() * 2) + 's';
            starsContainer.appendChild(star);
        }
        
        document.body.appendChild(starsContainer);
        
        // 6 saniye sonra kaldır
        setTimeout(() => {
            if (starsContainer.parentNode) {
                starsContainer.parentNode.removeChild(starsContainer);
            }
        }, 6000);
    }

    showCorrectSymbol() {
        const overlay = document.createElement('div');
        overlay.className = 'correct-answer-overlay';
        overlay.innerHTML = '<div class="correct-symbol">✓</div>';
        
        document.body.appendChild(overlay);
        
        // Konfeti burst efekti ekle
        const burst = document.createElement('div');
        burst.className = 'confetti-burst';
        document.body.appendChild(burst);
        
        // Remove overlay after animation (2.5 saniye)
        setTimeout(() => {
            if (overlay.parentNode) {
                overlay.parentNode.removeChild(overlay);
            }
            if (burst.parentNode) {
                burst.parentNode.removeChild(burst);
            }
        }, 2500);
    }

    showWrongSymbol() {
        const overlay = document.createElement('div');
        overlay.className = 'wrong-answer-overlay';
        overlay.innerHTML = '<div class="wrong-symbol">✗</div>';
        
        document.body.appendChild(overlay);
        
        // Remove overlay after animation (2 saniye)
        setTimeout(() => {
            if (overlay.parentNode) {
                overlay.parentNode.removeChild(overlay);
            }
        }, 2000);
    }

    skipQuestion() {
        // Mark as skipped
        this.answers[this.currentQuestionIndex] = null;
        
        // Move to next question
        this.nextQuestion();
    }

    nextQuestion() {
        if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++;
            this.displayCurrentQuestion();
        } else {
            this.finishQuiz();
        }
    }

    navigateToQuestion(index) {
        if (index >= 0 && index < this.questions.length) {
            this.currentQuestionIndex = index;
            this.displayCurrentQuestion();
        }
    }

    finishQuiz() {
        this.isActive = false;
        
        // Calculate results
        const quizData = {
            questions: this.questions,
            answers: this.answers,
            timeLimit: 0 // Zamanlayıcı kaldırıldı
        };
        
        // Show results
        this.results.showResults(quizData);
    }

    retryQuiz() {
        // Reset quiz state
        this.currentQuestionIndex = 0;
        this.answers = [];
        this.isActive = true;
        
        // Hide results
        document.querySelector('.quiz-results-container').style.display = 'none';
        
        // Start quiz again
        this.startQuiz();
    }

    destroy() {
        if (this.header) this.header.destroy();
        if (this.question) this.question.destroy();
        if (this.options) this.options.destroy();
        if (this.controls) this.controls.destroy();
        if (this.results) this.results.destroy();
    }

    setupAIChat() {
        const chatInput = document.getElementById('aiChatInput');
        const chatSend = document.getElementById('aiChatSend');
        const chatMessages = document.querySelector('.ai-chat-messages');

        if (chatSend) {
            chatSend.addEventListener('click', () => {
                this.sendAIMessage();
            });
        }

        if (chatInput) {
            chatInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.sendAIMessage();
                }
            });
        }
    }

    sendAIMessage() {
        const chatInput = document.getElementById('aiChatInput');
        const chatMessages = document.querySelector('.ai-chat-messages');
        
        if (!chatInput || !chatMessages) return;

        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        this.addChatMessage(message, 'user');
        chatInput.value = '';

        // Simulate AI response
        setTimeout(() => {
            const aiResponse = this.getAIResponse(message);
            this.addChatMessage(aiResponse, 'ai');
        }, 1000);
    }

    addChatMessage(text, sender) {
        const chatMessages = document.querySelector('.ai-chat-messages');
        if (!chatMessages) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `ai-message ${sender}`;
        messageDiv.textContent = text;

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Eğer AI mesajıysa, baloncuğu güncelle
        if (sender === 'ai') {
            this.showCatSpeechBubble(text);
        }
    }

    showCatSpeechBubble(text) {
        const bubble = document.getElementById('catSpeechBubble');
        if (!bubble) return;
        bubble.textContent = text;
        bubble.classList.add('active');
        // Otomatik gizleme yok, baloncuk sürekli açık kalacak
    }

    getAIResponse(userMessage) {
        const responses = {
            'merhaba': 'Merhaba! Quiz sırasında size nasıl yardım edebilirim? 😊',
            'yardım': 'Quiz hakkında yardım istiyorsanız, soruları dikkatlice okuyun ve doğru cevabı seçin. Size konfeti ve yıldızlarla güzel animasyonlar göstereceğiz! 🌟',
            'nasıl': 'Quiz çok basit! Soruları okuyup doğru cevabı seçmeniz yeterli. Her doğru cevapta konfeti patlar! 🎉',
            'teşekkür': 'Rica ederim! Başka bir sorunuz varsa sormaktan çekinmeyin! 😸',
            'güzel': 'Teşekkürler! Quiz sistemimiz gerçekten çok eğlenceli, değil mi? 🌈',
            'quiz': 'Quiz sistemimiz interaktif ve eğlenceli! Her soru için animasyonlar ve görsel efektler var! ✨',
            'animasyon': 'Evet! Doğru cevaplarda konfeti patlar, yanlış cevaplarda ise çarpı işareti çıkar. Çok eğlenceli! 🎊',
            'catmatch': 'Ben CatmatchAI! Quiz sırasında size yardım etmek için buradayım. Herhangi bir sorunuz varsa sorabilirsiniz! 🐱'
        };

        const lowerMessage = userMessage.toLowerCase();
        
        for (const [key, response] of Object.entries(responses)) {
            if (lowerMessage.includes(key)) {
                return response;
            }
        }

        // Default responses
        const defaultResponses = [
            'Harika bir soru! Quiz hakkında daha fazla bilgi almak ister misiniz? 😊',
            'Quiz sistemimiz çok eğlenceli! Her doğru cevapta konfeti patlar! 🎉',
            'Size nasıl yardım edebilirim? Quiz hakkında herhangi bir sorunuz var mı? 🌟',
            'Quiz sırasında size yardım etmek için buradayım! Başka bir sorunuz var mı? 😸',
            'Harika! Quiz sistemimiz interaktif ve eğlenceli. Daha fazla bilgi almak ister misiniz? ✨'
        ];

        return defaultResponses[Math.floor(Math.random() * defaultResponses.length)];
    }
}

// Initialize quiz when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize quiz
    window.quizApp = new QuizApp();
});
