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
        this.userAnswers = [];
        this.correctAnswers = 0;
        this.quizSessionId = null;
        this.isQuizActive = false;
        
        this.initializeQuiz();
    }
    
    async initializeQuiz() {
        try {
            // Quiz oturumu başlat
            const sessionResponse = await fetch('/api/quiz/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            if (sessionResponse.ok) {
                const sessionData = await sessionResponse.json();
                this.quizSessionId = sessionData.data.session_id;
            }
            
            // Soruları getir
            const response = await fetch('/api/quiz/questions?limit=20');
            if (response.ok) {
                const data = await response.json();
                this.questions = data.data.questions;
                this.userAnswers = new Array(this.questions.length).fill(null);
                
                this.displayQuestion();
                this.isQuizActive = true;
            } else {
                console.error('Sorular yüklenemedi');
            }
        } catch (error) {
            console.error('Quiz başlatma hatası:', error);
        }
    }
    
    displayQuestion() {
        if (this.currentQuestionIndex >= this.questions.length) {
            this.showResults();
            return;
        }

        const question = this.questions[this.currentQuestionIndex];
        
        // Soru numarasını güncelle
        document.querySelector('.question-number').textContent = `Soru ${question.number}`;
        document.querySelector('.question-text').textContent = question.question_text;
        
        // Şıkları güncelle
        const optionsContainer = document.querySelector('.quiz-options');
        optionsContainer.innerHTML = '';
        
        Object.entries(question.options).forEach(([key, value]) => {
            const optionDiv = document.createElement('div');
            optionDiv.className = 'option-item';
            optionDiv.innerHTML = `
                <div class="option-label">
                    <span class="option-letter">${key}</span>
                    <span class="option-text">${value}</span>
                </div>
            `;
            
            optionDiv.addEventListener('click', () => this.selectOption(key));
            optionsContainer.appendChild(optionDiv);
        });
        
        // Navigasyon bilgilerini güncelle
        document.querySelector('.quiz-nav-info').textContent = `${this.currentQuestionIndex + 1} / ${this.questions.length}`;
        
        // Butonları güncelle
        document.getElementById('prevBtn').disabled = this.currentQuestionIndex === 0;
        document.getElementById('nextBtn').disabled = this.currentQuestionIndex === this.questions.length - 1;
    }
    
    selectOption(option) {
        // Önceki seçimi temizle
        document.querySelectorAll('.option-item').forEach(item => {
            item.classList.remove('selected');
        });
        
        // Yeni seçimi işaretle
        event.target.closest('.option-item').classList.add('selected');
        
        // Cevabı kaydet
        this.userAnswers[this.currentQuestionIndex] = option;
    }
    
    async submitAnswer() {
        if (this.userAnswers[this.currentQuestionIndex] === null) {
            alert('Lütfen bir seçenek seçin!');
            return;
        }

        const question = this.questions[this.currentQuestionIndex];
        const userAnswer = this.userAnswers[this.currentQuestionIndex];
        const isCorrect = userAnswer === question.correct_answer;
        
        if (isCorrect) {
            this.correctAnswers++;
            this.showCorrectAnimation();
        } else {
            this.showIncorrectAnimation();
        }
        
        // Cevabı sunucuya gönder
        try {
            await fetch('/api/quiz/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    question_id: question.id,
                    user_answer: userAnswer,
                    is_correct: isCorrect,
                    session_id: this.quizSessionId
                })
            });
        } catch (error) {
            console.error('Cevap gönderme hatası:', error);
        }
        
        // Sonraki soruya geç
        setTimeout(() => {
            this.nextQuestion();
        }, 2000);
    }
    
    skipQuestion() {
        this.nextQuestion();
    }
    
    nextQuestion() {
        if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++;
            this.displayQuestion();
        } else {
            this.showResults();
        }
    }
    
    prevQuestion() {
        if (this.currentQuestionIndex > 0) {
            this.currentQuestionIndex--;
            this.displayQuestion();
        }
    }
    
    async showResults() {
        // Quiz'i tamamla
        try {
            const response = await fetch('/api/quiz/complete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    session_id: this.quizSessionId,
                    correct_answers: this.correctAnswers,
                    total_questions: this.questions.length
                })
            });
            
            const result = await response.json();
            
            // Başarı kazanıldıysa göster
            if (result.success && result.data.achievement_earned) {
                this.showAchievementNotification(result.data.achievement_earned);
            }
        } catch (error) {
            console.error('Quiz tamamlama hatası:', error);
        }
        
        // Sonuçları göster
        const scorePercentage = Math.round((this.correctAnswers / this.questions.length) * 100);
        
        document.querySelector('.score-percentage').textContent = `${scorePercentage}%`;
        document.querySelector('.score-details').textContent = `${this.correctAnswers} / ${this.questions.length} doğru`;
        
        // Quiz container'ı gizle, sonuçları göster
        document.querySelector('.quiz-content').style.display = 'none';
        document.querySelector('.quiz-results-container').style.display = 'block';
        
        // Konfeti efekti
        if (scorePercentage >= 80) {
            this.showConfetti();
        }
    }
    
    showAchievementNotification(achievement) {
        // Başarı bildirimi oluştur
        const notification = document.createElement('div');
        notification.className = 'achievement-notification';
        notification.innerHTML = `
            <div class="achievement-content">
                <div class="achievement-icon">${achievement.icon}</div>
                <div class="achievement-text">
                    <div class="achievement-title">${achievement.name}</div>
                    <div class="achievement-description">${achievement.description}</div>
                </div>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Animasyon için GSAP kullan
        if (typeof gsap !== 'undefined') {
            gsap.fromTo(notification, 
                { 
                    scale: 0, 
                    opacity: 0,
                    y: 50
                },
                { 
                    scale: 1, 
                    opacity: 1,
                    y: 0,
                    duration: 0.5,
                    ease: "back.out(1.7)"
                }
            );
            
            // 5 saniye sonra kaldır
            setTimeout(() => {
                gsap.to(notification, {
                    scale: 0.8,
                    opacity: 0,
                    y: -50,
                    duration: 0.3,
                    onComplete: () => {
                        if (document.body.contains(notification)) {
                            document.body.removeChild(notification);
                        }
                    }
                });
            }, 5000);
        } else {
            // GSAP yoksa basit animasyon
            notification.style.transform = 'scale(0)';
            notification.style.opacity = '0';
            
            setTimeout(() => {
                notification.style.transition = 'all 0.5s ease';
                notification.style.transform = 'scale(1)';
                notification.style.opacity = '1';
            }, 100);
            
            setTimeout(() => {
                notification.style.transform = 'scale(0.8)';
                notification.style.opacity = '0';
                setTimeout(() => {
                    if (document.body.contains(notification)) {
                        document.body.removeChild(notification);
                    }
                }, 300);
            }, 5000);
        }
    }
    
    showCorrectAnimation() {
        const overlay = document.createElement('div');
        overlay.className = 'correct-answer-overlay';
        overlay.innerHTML = '<div class="correct-symbol">✓</div>';
        document.body.appendChild(overlay);
        
        // Balık ekle
        this.addScoreFish();
        
        setTimeout(() => {
            document.body.removeChild(overlay);
        }, 2500);
    }

    showIncorrectAnimation() {
        const overlay = document.createElement('div');
        overlay.className = 'wrong-answer-overlay';
        overlay.innerHTML = '<div class="wrong-symbol">✗</div>';
        document.body.appendChild(overlay);
        
        // Çarpı işareti ekle
        this.addScoreCross();
        
        setTimeout(() => {
            document.body.removeChild(overlay);
        }, 2000);
    }

    showConfetti() {
        if (typeof confetti !== 'undefined') {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    }

    addScoreFish() {
        const scoreContainer = document.querySelector('.score-container');
        if (scoreContainer) {
            const fish = document.createElement('div');
            fish.className = 'score-fish';
            fish.innerHTML = '🐠';
            
            // Mevcut satırları say
            const rows = scoreContainer.querySelectorAll('.score-row');
            const currentRow = rows[rows.length - 1];
            
            if (currentRow && currentRow.children.length < 5) {
                // Mevcut satıra ekle
                currentRow.appendChild(fish);
            } else {
                // Yeni satır oluştur
                const newRow = document.createElement('div');
                newRow.className = 'score-row';
                newRow.style.display = 'flex';
                newRow.style.gap = '3px';
                newRow.style.marginTop = '5px';
                newRow.appendChild(fish);
                scoreContainer.appendChild(newRow);
            }
        }
    }
    
    addScoreCross() {
        const scoreContainer = document.querySelector('.score-container');
        if (scoreContainer) {
            const cross = document.createElement('div');
            cross.className = 'score-cross';
            cross.innerHTML = '❌';
            
            // Mevcut satırları say
            const rows = scoreContainer.querySelectorAll('.score-row');
            const currentRow = rows[rows.length - 1];
            
            if (currentRow && currentRow.children.length < 5) {
                // Mevcut satıra ekle
                currentRow.appendChild(cross);
            } else {
                // Yeni satır oluştur
                const newRow = document.createElement('div');
                newRow.className = 'score-row';
                newRow.style.display = 'flex';
                newRow.style.gap = '3px';
                newRow.style.marginTop = '5px';
                newRow.appendChild(cross);
                scoreContainer.appendChild(newRow);
            }
        }
    }
}

// Quiz uygulamasını başlat
document.addEventListener('DOMContentLoaded', () => {
    const quizApp = new QuizApp();
    
    // Event listeners
    document.getElementById('submitBtn').addEventListener('click', () => {
        quizApp.submitAnswer();
    });
    
    document.getElementById('skipBtn').addEventListener('click', () => {
        quizApp.skipQuestion();
    });
    
    document.getElementById('nextBtn').addEventListener('click', () => {
        quizApp.nextQuestion();
    });
    
    document.getElementById('prevBtn').addEventListener('click', () => {
        quizApp.prevQuestion();
    });
});
