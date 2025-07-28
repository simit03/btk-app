# Quiz Uygulaması - Modüler Yapı

Bu quiz uygulaması, modüler CSS ve JavaScript yapısı kullanılarak geliştirilmiştir.

## Yapı

### CSS Modülleri
- `quiz-header.css` - Quiz başlığı ve ilerleme çubuğu
- `quiz-question.css` - Soru gösterimi ve zamanlayıcı
- `quiz-options.css` - Seçenekler ve etkileşim
- `quiz-controls.css` - Navigasyon butonları ve kontroller
- `quiz-results.css` - Sonuç ekranı ve istatistikler

### JavaScript Modülleri
- `quiz-header.js` - Başlık yönetimi ve ilerleme takibi
- `quiz-question.js` - Soru gösterimi ve animasyonlar
- `quiz-options.js` - Seçenek yönetimi ve etkileşim
- `quiz-controls.js` - Kontrol butonları ve navigasyon
- `quiz-results.js` - Sonuç hesaplama ve gösterimi

## Özellikler

### 🎨 Modern Tasarım
- Gradient arka planlar
- Smooth animasyonlar (GSAP)
- Responsive tasarım
- Modern UI/UX

### ⚡ Animasyonlar
- GSAP kütüphanesi kullanımı
- Smooth geçişler
- Hover efektleri
- Loading animasyonları

### 📱 Responsive
- Bootstrap Grid sistemi
- Mobile-first yaklaşım
- Tablet ve desktop uyumlu

### 🎯 Etkileşim
- Seçenek seçimi
- Zamanlayıcı
- Navigasyon
- Sonuç gösterimi

## Kullanım

### Quiz Erişimi
```
http://localhost:5000/quiz
```

### Modül Yükleme Sırası
1. GSAP Core
2. Quiz Header
3. Quiz Question
4. Quiz Options
5. Quiz Controls
6. Quiz Results
7. Main Quiz App

## Özelleştirme

### Yeni Soru Ekleme
```javascript
{
    id: 4,
    number: 4,
    text: "Yeni soru metni",
    options: [
        { text: "Seçenek A", feedback: "Açıklama" },
        { text: "Seçenek B", feedback: "Açıklama" },
        { text: "Seçenek C", feedback: "Açıklama" },
        { text: "Seçenek D", feedback: "Açıklama" }
    ],
    correctAnswer: 1,
    image: null
}
```

### CSS Özelleştirme
Her modül için ayrı CSS dosyası düzenlenebilir:
- Renkler
- Animasyonlar
- Layout
- Responsive breakpoint'ler

### JavaScript Özelleştirme
Her modül bağımsız olarak düzenlenebilir:
- Event handling
- Animasyonlar
- Logic
- API entegrasyonu

## Bağımlılıklar

### CSS
- Bootstrap Grid System
- Custom CSS modülleri

### JavaScript
- GSAP (GreenSock Animation Platform)
- Vanilla JavaScript (ES6+)

## Tarayıcı Desteği

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Performans

- Modüler yapı sayesinde hızlı yükleme
- Lazy loading desteği
- Optimized animasyonlar
- Minimal bundle size

## Geliştirme

### Yeni Modül Ekleme
1. CSS dosyası oluştur
2. JavaScript modülü oluştur
3. Ana quiz.js'e import et
4. HTML'de referans ver

### Test Etme
```bash
python main.py
```
Ardından `http://localhost:5000/quiz` adresine git

## Lisans

Bu proje MIT lisansı altında geliştirilmiştir. 