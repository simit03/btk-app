/**
 * Progress Page JavaScript
 * İlerleme tablosu sayfası işlevleri
 */

let dailyProgressChart = null;

document.addEventListener('DOMContentLoaded', function() {
    console.log('📊 Progress page loaded');
    
    // Sayfa animasyonları
    initializePageAnimations();
    
    // Period selector'ı ayarla
    setupPeriodSelector();
    
    // Verileri yükle
    loadProgressData();
});

// Günlük ilerleme verilerini yükle
async function loadDailyProgress() {
    try {
        const response = await fetch('/api/progress/daily', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const data = result.data;
            
            // Eğer veri yoksa boş durum göster
            if (!data.daily_data || data.daily_data.length === 0) {
                showEmptyState('daily-progress-section', 'Henüz ilerleme verisi bulunmuyor', 'Quiz çözmeye başlayarak verilerinizi görün!');
                return;
            }
            
            // İstatistikleri güncelle
            updateDailyStats(data.summary);
            
            // Tabloyu oluştur
            createDailyTable(data.daily_data);
        } else {
            showEmptyState('daily-progress-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
        }
    } catch (error) {
        console.error('Günlük ilerleme yükleme hatası:', error);
        showEmptyState('daily-progress-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
    }
}

// Detaylı ilerleme verilerini yükle
async function loadDetailedProgress() {
    try {
        const response = await fetch('/api/progress/detailed', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const data = result.data;
            
            // Eğer veri yoksa boş durum göster
            if (!data.daily_data || data.daily_data.length === 0) {
                showEmptyState('detailed-progress-section', 'Henüz ilerleme verisi bulunmuyor', 'Quiz çözmeye başlayarak verilerinizi görün!');
                return;
            }
            
            // Tabloyu oluştur
            createDetailedTable(data.daily_data);
        } else {
            showEmptyState('detailed-progress-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
        }
    } catch (error) {
        console.error('Detaylı ilerleme yükleme hatası:', error);
        showEmptyState('detailed-progress-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
    }
}

// Konu detay verilerini yükle
async function loadTopicDetail() {
    try {
        const response = await fetch('/api/progress/topics', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const data = result.data;
            
            // Eğer veri yoksa boş durum göster
            if (!data.topics || data.topics.length === 0) {
                showEmptyState('topic-detail-section', 'Henüz konu verisi bulunmuyor', 'Quiz çözmeye başlayarak verilerinizi görün!');
                return;
            }
            
            // Tabloyu oluştur
            createTopicDetailTable(data.topics);
        } else {
            showEmptyState('topic-detail-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
        }
    } catch (error) {
        console.error('Konu detay yükleme hatası:', error);
        showEmptyState('topic-detail-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
    }
}

// Period selector event listeners
function setupPeriodSelector() {
    const periodBtns = document.querySelectorAll('.period-btn');
    periodBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            periodBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Reload data with new period
            const period = this.dataset.period;
            loadDailyProgressWithPeriod(period);
        });
    });
}

// Load daily progress with specific period
async function loadDailyProgressWithPeriod(period) {
    try {
        const response = await fetch(`/api/progress/daily?period=${period}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const data = result.data;
            
            // Eğer veri yoksa boş durum göster
            if (!data.daily_data || data.daily_data.length === 0) {
                showEmptyState('daily-progress-section', 'Henüz ilerleme verisi bulunmuyor', 'Quiz çözmeye başlayarak verilerinizi görün!');
                return;
            }
            
            updateDailyStats(data.summary);
            createDailyTable(data.daily_data);
        }
    } catch (error) {
        console.error('Period değiştirme hatası:', error);
    }
}

// Günlük istatistikleri güncelle
function updateDailyStats(summary) {
    document.getElementById('mostActiveDay').textContent = summary.most_active_day || '-';
    document.getElementById('averageDaily').textContent = summary.average_daily || 0;
    document.getElementById('studyDays').textContent = summary.study_days || 0;
    document.getElementById('totalStudyTime').textContent = summary.total_study_time || 0;
}

// Günlük tabloyu oluştur
function createDailyTable(dailyData) {
    const tbody = document.getElementById('dailyTableBody');
    
    if (!dailyData || dailyData.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="6">
                    <div class="empty-state">
                        <div class="empty-state-icon">📊</div>
                        <div class="empty-state-text">Henüz ilerleme verisi bulunmuyor</div>
                        <div class="empty-state-subtext">Quiz çözmeye başlayarak verilerinizi görün!</div>
                    </div>
                </td>
            </tr>
        `;
        return;
    }
    
    let html = '';
    dailyData.forEach(day => {
        const successRate = day.solved > 0 ? Math.round((day.correct / day.solved) * 100) : 0;
        const successClass = successRate >= 80 ? 'high' : successRate >= 60 ? 'medium' : 'low';
        const pointsEarned = day.correct * 10; // Her doğru cevap 10 puan
        
        html += `
            <tr>
                <td class="date-cell">${new Date(day.date).toLocaleDateString('tr-TR')}</td>
                <td>${day.solved}</td>
                <td>${day.correct}</td>
                <td>${day.solved - day.correct}</td>
                <td class="success-rate ${successClass}">${successRate}%</td>
                <td>${pointsEarned}</td>
            </tr>
        `;
    });
    
    tbody.innerHTML = html;
}

// Detaylı tabloyu oluştur
function createDetailedTable(dailyData) {
    const tbody = document.getElementById('detailedTableBody');
    
    if (!dailyData || dailyData.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="8">
                    <div class="empty-state">
                        <div class="empty-state-icon">📊</div>
                        <div class="empty-state-text">Henüz ilerleme verisi bulunmuyor</div>
                        <div class="empty-state-subtext">Quiz çözmeye başlayarak verilerinizi görün!</div>
                    </div>
                </td>
            </tr>
        `;
        return;
    }
    
    let html = '';
    dailyData.forEach(day => {
        const successRate = day.solved > 0 ? Math.round((day.correct / day.solved) * 100) : 0;
        const successClass = successRate >= 80 ? 'high' : successRate >= 60 ? 'medium' : 'low';
        const pointsEarned = day.correct * 10; // Her doğru cevap 10 puan
        
        html += `
            <tr>
                <td class="date-cell">${new Date(day.date).toLocaleDateString('tr-TR')}</td>
                <td>${day.solved}</td>
                <td>${day.correct}</td>
                <td>${day.solved - day.correct}</td>
                <td class="success-rate ${successClass}">${successRate}%</td>
                <td>${pointsEarned}</td>
                <td>-</td>
                <td>-</td>
            </tr>
        `;
    });
    
    tbody.innerHTML = html;
}

// Konu detay tablosunu oluştur
function createTopicDetailTable(topics) {
    const tbody = document.getElementById('topicDetailTableBody');
    
    if (!topics || topics.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="7">
                    <div class="empty-state">
                        <div class="empty-state-icon">📚</div>
                        <div class="empty-state-text">Henüz konu verisi bulunmuyor</div>
                        <div class="empty-state-subtext">Quiz çözmeye başlayarak verilerinizi görün!</div>
                    </div>
                </td>
            </tr>
        `;
        return;
    }
    
    let html = '';
    topics.forEach(topic => {
        const successRate = topic.total_questions > 0 ? Math.round((topic.correct_questions / topic.total_questions) * 100) : 0;
        const successClass = successRate >= 80 ? 'high' : successRate >= 60 ? 'medium' : 'low';
        const status = successRate >= 80 ? '✅ Tamamlandı' : successRate >= 60 ? '🔄 Devam Ediyor' : '❌ Geliştirilmeli';
        
        html += `
            <tr>
                <td>${topic.topic}</td>
                <td>${topic.total_questions}</td>
                <td>${topic.correct_questions}</td>
                <td>${topic.total_questions - topic.correct_questions}</td>
                <td class="success-rate ${successClass}">${successRate}%</td>
                <td>-</td>
                <td>${status}</td>
            </tr>
        `;
    });
    
    tbody.innerHTML = html;
}

// Sayfa animasyonları
function initializePageAnimations() {
    const sections = document.querySelectorAll('.stats-overview, .achievements-history-section, .weekly-summary-section, .daily-progress-section, .detailed-progress-section, .topic-detail-section');
    
    sections.forEach((section, index) => {
        section.classList.add('fade-in');
        section.style.animationDelay = `${index * 0.2}s`;
    });
}

// Ana veri yükleme fonksiyonu
async function loadProgressData() {
    try {
        // Tüm verileri paralel olarak yükle
        await Promise.all([
            loadOverviewStats(),
            loadDailyProgress(),
            loadDetailedProgress(),
            loadTopicDetail(),
            loadAchievementsHistory(),
            loadWeeklySummary()
        ]);
        
        console.log('✅ Tüm veriler başarıyla yüklendi');
    } catch (error) {
        console.error('❌ Veri yükleme hatası:', error);
        showNotification('Veriler yüklenirken hata oluştu!', 'error');
    }
}

// Genel istatistikleri yükle
async function loadOverviewStats() {
    try {
        const response = await fetch('/api/user/stats', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const stats = result.data;
            
            // İstatistikleri güncelle
            updateStatElement('totalQuestionsSolved', stats.total_questions);
            updateStatElement('totalCorrectAnswers', stats.correct_questions);
            updateStatElement('successRate', `${stats.success_percentage}%`);
            updateStatElement('totalPoints', stats.total_points);
            
            // Animasyonlu güncelleme
            animateStatUpdates();
        }
    } catch (error) {
        console.error('Genel istatistik yükleme hatası:', error);
    }
}







// Başarı geçmişini yükle
async function loadAchievementsHistory() {
    try {
        const response = await fetch('/api/achievements', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const achievements = result.data.achievements;
            displayAchievementsHistory(achievements);
        } else {
            showEmptyState('achievements-history-section', 'Henüz başarı bulunmuyor', 'Quiz çözmeye başlayarak başarılarınızı görün!');
        }
    } catch (error) {
        console.error('Başarı geçmişi yükleme hatası:', error);
        showEmptyState('achievements-history-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
    }
}

// Başarı geçmişini görüntüle
function displayAchievementsHistory(achievements) {
    const container = document.getElementById('achievementsTimeline');
    
    if (achievements.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🏆</div>
                <div class="empty-state-text">Henüz başarı bulunmuyor</div>
                <div class="empty-state-subtext">Quiz çözmeye başlayarak başarılarınızı görün!</div>
            </div>
        `;
        return;
    }
    
    let html = '';
    achievements.forEach(achievement => {
        const date = new Date(achievement.earned_at).toLocaleDateString('tr-TR');
        
        html += `
            <div class="achievement-item">
                <div class="achievement-icon">
                    ${achievement.achievement_type === 'perfect_score' ? '🏆' : '⭐'}
                </div>
                <div class="achievement-info">
                    <div class="achievement-name">${achievement.achievement_name}</div>
                    <div class="achievement-date">Kazanıldı: ${date}</div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Haftalık özeti yükle
async function loadWeeklySummary() {
    try {
        const response = await fetch('/api/progress/weekly', {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const result = await response.json();
        
        if (result.success) {
            const weeks = result.data.weeks;
            displayWeeklySummary(weeks);
        } else {
            showEmptyState('weekly-summary-section', 'Henüz haftalık veri bulunmuyor', 'Quiz çözmeye başlayarak haftalık özetinizi görün!');
        }
    } catch (error) {
        console.error('Haftalık özet yükleme hatası:', error);
        showEmptyState('weekly-summary-section', 'Veri yüklenemedi', 'Lütfen sayfayı yenileyin.');
    }
}

// Haftalık özeti görüntüle
function displayWeeklySummary(weeks) {
    const container = document.getElementById('weeklyCards');
    
    if (weeks.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📋</div>
                <div class="empty-state-text">Henüz haftalık veri bulunmuyor</div>
                <div class="empty-state-subtext">Quiz çözmeye başlayarak haftalık özetinizi görün!</div>
            </div>
        `;
        return;
    }
    
    let html = '';
    weeks.forEach(week => {
        const successRate = week.total_questions > 0 ? Math.round((week.correct_questions / week.total_questions) * 100) : 0;
        
        html += `
            <div class="weekly-card">
                <div class="weekly-header">
                    <span class="weekly-title">${week.week_title}</span>
                    <span class="weekly-date">${week.date_range}</span>
                </div>
                <div class="weekly-stats">
                    <div class="weekly-stat">
                        <span class="weekly-stat-value">${week.total_questions}</span>
                        <span class="weekly-stat-label">Toplam Soru</span>
                    </div>
                    <div class="weekly-stat">
                        <span class="weekly-stat-value">${week.correct_questions}</span>
                        <span class="weekly-stat-label">Doğru</span>
                    </div>
                    <div class="weekly-stat">
                        <span class="weekly-stat-value">${successRate}%</span>
                        <span class="weekly-stat-label">Başarı</span>
                    </div>
                    <div class="weekly-stat">
                        <span class="weekly-stat-value">${week.points_earned}</span>
                        <span class="weekly-stat-label">Puan</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}



// İstatistik elementini güncelle
function updateStatElement(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = value;
    }
}

// İstatistik güncellemelerini animasyonlu yapma
function animateStatUpdates() {
    const statValues = document.querySelectorAll('.stat-value');
    
    statValues.forEach((value, index) => {
        const finalValue = value.textContent;
        let currentValue = 0;
        
        // Eğer yüzde işareti varsa, sadece sayıyı al
        const isPercentage = finalValue.includes('%');
        const numericValue = isPercentage ? parseFloat(finalValue) : parseInt(finalValue);
        
        if (isNaN(numericValue)) return;
        
        const increment = numericValue / 20; // 20 adımda artır
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= numericValue) {
                currentValue = numericValue;
                clearInterval(timer);
            }
            
            if (isPercentage) {
                value.textContent = `${Math.floor(currentValue)}%`;
            } else {
                value.textContent = Math.floor(currentValue);
            }
        }, 50 + (index * 10)); // Her istatistik için farklı hız
    });
}

// Boş durum göster
function showEmptyState(sectionId, title, subtitle) {
    const section = document.querySelector(`#${sectionId}`);
    if (section) {
        // Eğer content bulunamazsa, section'ı güncelle
        section.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📊</div>
                <div class="empty-state-text">${title}</div>
                <div class="empty-state-subtext">${subtitle}</div>
            </div>
        `;
    }
}

// Bildirim gösterme fonksiyonu
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#F44336' : '#2196F3'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        animation: slideInRight 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
} 