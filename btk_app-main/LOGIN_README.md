# 🐱 Login Sayfası

Bu proje, quiz uygulaması için tasarlanmış sevimli bir giriş sayfasıdır. Kullanıcı adı ve şifre ile giriş yapabilir, üzerinde şirin bir kedi imleci gözleri ile takip edecek şekilde tasarlanmıştır.

## 🌟 Özellikler

### 🎨 Tasarım
- **Çocuk dostu renkli arka plan** - Gökkuşağı gradyanı
- **Sevimli animasyonlar** - Yüzen kalpler ve hareketli kediler
- **Modern form tasarımı** - Glassmorphism efekti
- **Responsive tasarım** - Mobil ve masaüstü uyumlu

### 🐱 Kedi İmleci
- **Fare takibi** - Kedi imleci fareyi takip eder
- **Göz animasyonları** - Kedinin gözleri fareye bakar
- **Durum animasyonları**:
  - `idle` - Normal durum
  - `hovering` - Üzerine gelince
  - `clicking` - Tıklayınca
  - `typing` - Yazarken
  - `loading` - Yüklenirken
  - `success` - Başarılı giriş
  - `error` - Hata durumu
  - `happy` - Mutlu durum
  - `sad` - Üzgün durum
  - `excited` - Heyecanlı durum

### 📝 Form Özellikleri
- **Gerçek zamanlı doğrulama** - Anında hata mesajları
- **Şifre göster/gizle** - Göz ikonu ile kontrol
- **Beni hatırla** - Checkbox ile seçenek
- **Yükleme animasyonu** - Giriş sırasında loading
- **Bildirimler** - Başarı ve hata mesajları

## 🚀 Kurulum

1. **Projeyi çalıştırın:**
```bash
cd btk_app-main
python main.py
```

2. **Tarayıcıda açın:**
```
http://localhost:5000/login
```

## 📁 Dosya Yapısı

```
btk_app-main/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── login/
│   │   │       ├── login.css          # Ana CSS dosyası
│   │   │       ├── login-header.css   # Header stilleri
│   │   │       ├── login-form.css     # Form stilleri
│   │   │       └── login-cursor.css   # Kedi imleci stilleri
│   │   └── js/
│   │       └── login/
│   │           ├── login.js           # Ana JavaScript
│   │           ├── login-header.js    # Header animasyonları
│   │           ├── login-form.js      # Form işlemleri
│   │           └── login-cursor.js    # Kedi imleci kontrolü
│   └── templates/
│       └── login.html                 # Login sayfası template
└── app/routes/pages/routes.py         # Login route'u
```

## 🎯 Kullanım

### Giriş Yapma
1. **Kullanıcı adı** girin (en az 3 karakter)
2. **Şifre** girin (en az 6 karakter)
3. **Beni hatırla** seçeneğini işaretleyin (isteğe bağlı)
4. **Giriş Yap** butonuna tıklayın

### Kedi İmleci Etkileşimleri
- **Fare hareketi** - Kedi imleci fareyi takip eder
- **Form alanları** - Üzerine gelince kedi büyür
- **Butonlar** - Hover durumunda animasyon
- **Yazma** - Input alanlarında typing animasyonu
- **Başarı/Hata** - Giriş sonucuna göre animasyon

## 🎨 Animasyonlar

### Kedi İmleci Animasyonları
```css
/* Kuyruk sallama */
@keyframes cursorTailWag {
    0%, 100% { transform: rotate(0deg); }
    25% { transform: rotate(15deg); }
    75% { transform: rotate(-10deg); }
}

/* Göz kırpma */
@keyframes cursorBlink {
    0%, 90%, 100% { transform: scaleY(1); }
    95% { transform: scaleY(0.1); }
}
```

### Form Animasyonları
```css
/* Input odaklanma */
.input-wrapper.focused {
    transform: scale(1.02);
}

/* Başarı durumu */
.input-wrapper.valid input {
    border-color: #4ECDC4;
}
```

## 🔧 Özelleştirme

### Renkleri Değiştirme
`login.css` dosyasında renk değişkenlerini düzenleyin:

```css
:root {
    --primary-color: #4ECDC4;
    --secondary-color: #45B7D1;
    --error-color: #ff6b6b;
    --success-color: #4ECDC4;
}
```

### Animasyon Hızını Ayarlama
`login-cursor.css` dosyasında animasyon sürelerini değiştirin:

```css
.cat-cursor .cat-tail {
    animation: cursorTailWag 2s infinite ease-in-out;
}
```

## 📱 Responsive Tasarım

### Mobil Uyumluluk
- **Küçük ekranlar** - Tek sütun düzeni
- **Dokunmatik** - Touch event desteği
- **Kedi imleci** - Mobilde küçültülmüş boyut

### Erişilebilirlik
- **Klavye navigasyonu** - Tab, Enter, Space desteği
- **Screen reader** - ARIA etiketleri
- **Yüksek kontrast** - Görme engelli kullanıcılar için

## 🐛 Hata Ayıklama

### Yaygın Sorunlar
1. **Kedi imleci görünmüyor** - JavaScript konsolunu kontrol edin
2. **Animasyonlar çalışmıyor** - CSS dosyalarının yüklendiğinden emin olun
3. **Form gönderilmiyor** - Validation hatalarını kontrol edin

### Debug Modu
Tarayıcı konsolunda debug mesajlarını görebilirsiniz:
```
🐱 Login App Initializing...
🐱 Cat Cursor Ready!
🐱 Login Form Ready!
```

## 🎉 Özellikler

- ✅ Sevimli kedi imleci
- ✅ Fare takibi ve göz animasyonları
- ✅ Gerçek zamanlı form doğrulama
- ✅ Şifre göster/gizle
- ✅ Yükleme animasyonları
- ✅ Başarı/hata bildirimleri
- ✅ Responsive tasarım
- ✅ Erişilebilirlik desteği
- ✅ Modern CSS animasyonları
- ✅ Modüler JavaScript yapısı

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. Tarayıcı konsolunu kontrol edin
2. CSS ve JavaScript dosyalarının yüklendiğinden emin olun
3. Flask uygulamasının çalıştığından emin olun

---

**Not:** Bu login sayfası demo amaçlıdır. Gerçek bir uygulamada güvenlik önlemleri (HTTPS, CSRF koruması, rate limiting vb.) eklenmelidir. 