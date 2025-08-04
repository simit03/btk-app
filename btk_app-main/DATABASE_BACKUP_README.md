# 🐱 MatchCatAI - Veritabanı Yedekleme ve Geri Yükleme Sistemi

Bu sistem, veritabanındaki tüm verileri yedekler ve main.py başladığında otomatik olarak geri yükler.

## 📋 Özellikler

### ✅ **Otomatik Yedekleme ve Geri Yükleme**
- Veritabanındaki tüm tabloları otomatik yedekler
- main.py başladığında otomatik geri yükleme yapar
- JSON formatında güvenli yedekleme

### 📊 **Desteklenen Tablolar**
- `users` - Kullanıcı bilgileri
- `questions` - Matematik soruları
- `user_progress` - Kullanıcı ilerleme verileri
- `quiz_sessions` - Quiz oturumları
- `achievements` - Başarılar ve kupalar

### 🔧 **Kullanım**

#### **1. Veritabanını Yedekleme**
```bash
python data_backup_restore.py backup
```

#### **2. Veritabanını Geri Yükleme**
```bash
python data_backup_restore.py restore
```

#### **3. Yedek Bilgilerini Görme**
```bash
python data_backup_restore.py info
```

#### **4. Otomatik Geri Yükleme (main.py ile)**
```bash
python main.py
```

## 📁 Dosya Yapısı

```
btk_app-main/
├── data_backup_restore.py          # Ana yedekleme sistemi
├── main.py                         # Otomatik geri yükleme ile güncellenmiş
├── backups/                        # Yedek dosyaları dizini
│   └── database_backup.json       # Yedek dosyası
└── DATABASE_BACKUP_README.md      # Bu dosya
```

## 🔄 Otomatik Geri Yükleme

main.py dosyası artık şu özelliklere sahip:

1. **Uygulama başladığında** otomatik olarak yedek dosyasını kontrol eder
2. **Yedek dosyası varsa** veritabanını geri yükler
3. **Yedek dosyası yoksa** normal şekilde devam eder

## 📊 Yedekleme İstatistikleri

### **Son Yedekleme:**
- **Tarih:** 2025-08-04T05:26:43.715102
- **Tablo Sayısı:** 5
- **Toplam Kayıt:** 138
- **Dosya Boyutu:** 49,993 bytes

### **Yedeklenen Veriler:**
- ✅ **achievements:** 9 kayıt
- ✅ **questions:** 95 kayıt
- ✅ **quiz_sessions:** 28 kayıt
- ✅ **user_progress:** 0 kayıt
- ✅ **users:** 6 kayıt

## 🛠️ Teknik Detaylar

### **Veri Tipleri Desteği:**
- ✅ **String** - Metin verileri
- ✅ **Integer** - Tam sayılar
- ✅ **Decimal** - Ondalık sayılar
- ✅ **DateTime** - Tarih/saat verileri
- ✅ **Boolean** - Mantıksal değerler
- ✅ **NULL** - Boş değerler

### **Güvenlik Özellikleri:**
- ✅ **UTF-8** karakter desteği
- ✅ **Hata yönetimi** - Bağlantı hatalarında güvenli çıkış
- ✅ **Veri doğrulama** - JSON formatında güvenli saklama
- ✅ **Otomatik temizlik** - Eski verileri temizleme

## 🚀 Kullanım Senaryoları

### **Senaryo 1: Geliştirme Ortamı**
```bash
# Veritabanını yedekle
python data_backup_restore.py backup

# Uygulamayı başlat (otomatik geri yükleme ile)
python main.py
```

### **Senaryo 2: Test Ortamı**
```bash
# Test verilerini yedekle
python data_backup_restore.py backup

# Test sonrası geri yükle
python data_backup_restore.py restore
```

### **Senaryo 3: Üretim Ortamı**
```bash
# Üretim verilerini yedekle
python data_backup_restore.py backup

# Yedek bilgilerini kontrol et
python data_backup_restore.py info
```

## ⚠️ Önemli Notlar

1. **Yedek dosyası** `backups/database_backup.json` konumunda saklanır
2. **Otomatik geri yükleme** main.py başladığında çalışır
3. **Mevcut veriler** geri yükleme sırasında silinir
4. **Yedek dosyası** UTF-8 formatında kaydedilir

## 🔧 Sorun Giderme

### **Hata: "Yedek dosyası bulunamadı"**
```bash
# Önce yedekleme yapın
python data_backup_restore.py backup
```

### **Hata: "Veritabanı bağlantı hatası"**
- MySQL servisinin çalıştığından emin olun
- config.py dosyasındaki bağlantı bilgilerini kontrol edin

### **Hata: "JSON serileştirme hatası"**
- Sistem otomatik olarak Decimal tiplerini float'a çevirir
- Eğer hata devam ederse, yeni veri tiplerini sisteme ekleyin

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. `python data_backup_restore.py info` ile yedek durumunu kontrol edin
2. Hata mesajlarını dikkatlice okuyun
3. Veritabanı bağlantısını test edin

---

**🐱 MatchCatAI - Matematik Öğrenme Platformu**
*Veritabanı Yedekleme ve Geri Yükleme Sistemi v1.0* 