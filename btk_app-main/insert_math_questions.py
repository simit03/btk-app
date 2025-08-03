import mysql.connector
from config import DB_CONFIG
import random

def insert_questions():
    """1. sınıf için yeni müfredata göre soruları ekler"""
    
    # 1. sınıf soruları - yeni müfredat
    grade1_questions = [
        # 2. Toplama İşlemi - Toplama işleminin anlamı
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "3 elma + 2 elma = kaç elma eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "2 kalem + 3 kalem = kaç kalem eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "1 top + 4 top = kaç top eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "5 çiçek + 2 çiçek = kaç çiçek eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "3 kuş + 2 kuş = kaç kuş eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        
        # 2. Toplama İşlemi - Nesnelerle toplama
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "4 kırmızı top + 3 mavi top = kaç top eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "2 büyük kutu + 3 küçük kutu = kaç kutu eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "5 uzun çubuk + 2 kısa çubuk = kaç çubuk eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "3 yuvarlak nesne + 4 köşeli nesne = kaç nesne eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "1 ağır kutu + 5 hafif kutu = kaç kutu eder?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        
        # 2. Toplama İşlemi - Toplama işlemi yapma (20'ye kadar)
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "8 + 7 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "9 + 6 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "7 + 8 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "6 + 9 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "5 + 10 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # 2. Toplama İşlemi - Toplamı tahmin etme
        {"grade": 1, "topic": "Toplamı Tahmin Etme", "question_text": "6 + 8 yaklaşık kaç eder?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplamı Tahmin Etme", "question_text": "7 + 9 yaklaşık kaç eder?", "option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplamı Tahmin Etme", "question_text": "8 + 6 yaklaşık kaç eder?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplamı Tahmin Etme", "question_text": "9 + 7 yaklaşık kaç eder?", "option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplamı Tahmin Etme", "question_text": "5 + 11 yaklaşık kaç eder?", "option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17", "correct_answer": "C"},
        
        # 2. Toplama İşlemi - Toplama ile ilgili problem çözme
        {"grade": 1, "topic": "Toplama Problemleri", "question_text": "Ahmet'in 5 kalemi vardı. 3 kalem daha aldı. Kaç kalemi oldu?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama Problemleri", "question_text": "Ayşe'nin 4 elması vardı. 6 elma daha topladı. Kaç elması oldu?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama Problemleri", "question_text": "Mehmet'in 3 topu vardı. 7 top daha aldı. Kaç topu oldu?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama Problemleri", "question_text": "Fatma'nın 6 çiçeği vardı. 4 çiçek daha dikti. Kaç çiçeği oldu?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama Problemleri", "question_text": "Ali'nin 2 kuşu vardı. 8 kuş daha aldı. Kaç kuşu oldu?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        
        # 3. Çıkarma İşlemi - Çıkarma işleminin anlamı
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "5 elma - 2 elma = kaç elma kalır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "7 kalem - 3 kalem = kaç kalem kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "8 top - 4 top = kaç top kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "6 çiçek - 2 çiçek = kaç çiçek kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "9 kuş - 5 kuş = kaç kuş kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        
        # 3. Çıkarma İşlemi - Nesnelerle çıkarma
        {"grade": 1, "topic": "Nesnelerle Çıkarma", "question_text": "8 kırmızı top - 3 mavi top = kaç top kalır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Çıkarma", "question_text": "7 büyük kutu - 2 küçük kutu = kaç kutu kalır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Çıkarma", "question_text": "9 uzun çubuk - 4 kısa çubuk = kaç çubuk kalır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Çıkarma", "question_text": "6 yuvarlak nesne - 1 köşeli nesne = kaç nesne kalır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Çıkarma", "question_text": "8 ağır kutu - 3 hafif kutu = kaç kutu kalır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        
        # 3. Çıkarma İşlemi - Çıkarma işlemi yapma (20'ye kadar)
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "15 - 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "16 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "17 - 8 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "18 - 9 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "19 - 10 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        
        # 3. Çıkarma İşlemi - Çıkarma ile ilgili problem çözme
        {"grade": 1, "topic": "Çıkarma Problemleri", "question_text": "Ahmet'in 12 kalemi vardı. 5 kalem kaybetti. Kaç kalemi kaldı?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma Problemleri", "question_text": "Ayşe'nin 15 elması vardı. 8 elma yedi. Kaç elması kaldı?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma Problemleri", "question_text": "Mehmet'in 14 topu vardı. 6 top kaybetti. Kaç topu kaldı?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma Problemleri", "question_text": "Fatma'nın 16 çiçeği vardı. 9 çiçek soldu. Kaç çiçeği kaldı?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma Problemleri", "question_text": "Ali'nin 18 kuşu vardı. 10 kuş uçtu. Kaç kuşu kaldı?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        
        # 5. Karşılaştırma ve Sıralama - Sayıları büyüklük açısından karşılaştırma
        {"grade": 1, "topic": "Sayıları Karşılaştırma", "question_text": "8 ile 5 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma", "question_text": "3 ile 7 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma", "question_text": "6 ile 6 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma", "question_text": "9 ile 4 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma", "question_text": "2 ile 8 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        
        # 5. Karşılaştırma ve Sıralama - Uzunlukları, ağırlıkları karşılaştırma
        {"grade": 1, "topic": "Uzunluk ve Ağırlık Karşılaştırma", "question_text": "Hangisi daha uzun?", "option_a": "Kalem", "option_b": "Çubuk", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk ve Ağırlık Karşılaştırma", "question_text": "Hangisi daha ağır?", "option_a": "Tüy", "option_b": "Taş", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk ve Ağırlık Karşılaştırma", "question_text": "Hangisi daha kısa?", "option_a": "Ağaç", "option_b": "Çiçek", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk ve Ağırlık Karşılaştırma", "question_text": "Hangisi daha hafif?", "option_a": "Demir", "option_b": "Pamuk", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk ve Ağırlık Karşılaştırma", "question_text": "Hangisi daha uzun?", "option_a": "Kedi", "option_b": "Fil", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # 5. Karşılaştırma ve Sıralama - Sıralı sayma
        {"grade": 1, "topic": "Sıralı Sayma", "question_text": "1'den 5'e kadar sayarken 3'ten sonra ne gelir?", "option_a": "2", "option_b": "4", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Sıralı Sayma", "question_text": "5'ten 10'a kadar sayarken 7'den sonra ne gelir?", "option_a": "6", "option_b": "8", "option_c": "9", "option_d": "11", "correct_answer": "B"},
        {"grade": 1, "topic": "Sıralı Sayma", "question_text": "10'dan 15'e kadar sayarken 12'den sonra ne gelir?", "option_a": "11", "option_b": "13", "option_c": "14", "option_d": "16", "correct_answer": "B"},
        {"grade": 1, "topic": "Sıralı Sayma", "question_text": "15'ten 20'ye kadar sayarken 17'den sonra ne gelir?", "option_a": "16", "option_b": "18", "option_c": "19", "option_d": "21", "correct_answer": "B"},
        {"grade": 1, "topic": "Sıralı Sayma", "question_text": "20'den 25'e kadar sayarken 22'den sonra ne gelir?", "option_a": "21", "option_b": "23", "option_c": "24", "option_d": "26", "correct_answer": "B"},
        
        # 6. Geometrik Cisimler ve Şekiller - Düzlemsel şekiller
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        
        # 6. Geometrik Cisimler ve Şekiller - Geometrik cisimler
        {"grade": 1, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 1, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küre şeklindedir?", "option_a": "Zar", "option_b": "Top", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 1, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim silindir şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Kutu", "option_d": "Koni", "correct_answer": "C"},
        {"grade": 1, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim koni şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Dondurma külahı", "correct_answer": "D"},
        {"grade": 1, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklinde değildir?", "option_a": "Zar", "option_b": "Top", "option_c": "Kutu", "option_d": "Küp", "correct_answer": "B"},
        
        # 7. Zaman - Günlük zaman dilimleri
        {"grade": 1, "topic": "Günlük Zaman Dilimleri", "question_text": "Güneş doğduğunda hangi zaman dilimidir?", "option_a": "Akşam", "option_b": "Gece", "option_c": "Sabah", "option_d": "Öğle", "correct_answer": "C"},
        {"grade": 1, "topic": "Günlük Zaman Dilimleri", "question_text": "Güneş tam tepedeyken hangi zaman dilimidir?", "option_a": "Sabah", "option_b": "Öğle", "option_c": "Akşam", "option_d": "Gece", "correct_answer": "B"},
        {"grade": 1, "topic": "Günlük Zaman Dilimleri", "question_text": "Güneş batarken hangi zaman dilimidir?", "option_a": "Sabah", "option_b": "Öğle", "option_c": "Akşam", "option_d": "Gece", "correct_answer": "C"},
        {"grade": 1, "topic": "Günlük Zaman Dilimleri", "question_text": "Güneş yokken hangi zaman dilimidir?", "option_a": "Sabah", "option_b": "Öğle", "option_c": "Akşam", "option_d": "Gece", "correct_answer": "D"},
        {"grade": 1, "topic": "Günlük Zaman Dilimleri", "question_text": "Kahvaltı yaparken hangi zaman dilimidir?", "option_a": "Sabah", "option_b": "Öğle", "option_c": "Akşam", "option_d": "Gece", "correct_answer": "A"},
        
        # 7. Zaman - Haftanın günleri
        {"grade": 1, "topic": "Haftanın Günleri", "question_text": "Haftanın ilk günü hangisidir?", "option_a": "Salı", "option_b": "Çarşamba", "option_c": "Pazartesi", "option_d": "Perşembe", "correct_answer": "C"},
        {"grade": 1, "topic": "Haftanın Günleri", "question_text": "Haftanın son günü hangisidir?", "option_a": "Cumartesi", "option_b": "Pazar", "option_c": "Cuma", "option_d": "Perşembe", "correct_answer": "B"},
        {"grade": 1, "topic": "Haftanın Günleri", "question_text": "Pazartesi'den sonra hangi gün gelir?", "option_a": "Pazar", "option_b": "Salı", "option_c": "Çarşamba", "option_d": "Perşembe", "correct_answer": "B"},
        {"grade": 1, "topic": "Haftanın Günleri", "question_text": "Cuma'dan önce hangi gün gelir?", "option_a": "Çarşamba", "option_b": "Perşembe", "option_c": "Cumartesi", "option_d": "Pazar", "correct_answer": "B"},
        {"grade": 1, "topic": "Haftanın Günleri", "question_text": "Hafta sonu hangi günlerdir?", "option_a": "Pazartesi-Salı", "option_b": "Çarşamba-Perşembe", "option_c": "Cuma-Cumartesi", "option_d": "Cumartesi-Pazar", "correct_answer": "D"},
        
        # 7. Zaman - Saat okuma (tam saatler)
        {"grade": 1, "topic": "Saat Okuma", "question_text": "Saat 3:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "3'te", "option_c": "6'da", "option_d": "9'da", "correct_answer": "B"},
        {"grade": 1, "topic": "Saat Okuma", "question_text": "Saat 6:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "3'te", "option_c": "6'da", "option_d": "9'da", "correct_answer": "C"},
        {"grade": 1, "topic": "Saat Okuma", "question_text": "Saat 9:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "3'te", "option_c": "6'da", "option_d": "9'da", "correct_answer": "D"},
        {"grade": 1, "topic": "Saat Okuma", "question_text": "Saat 12:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "3'te", "option_c": "6'da", "option_d": "9'da", "correct_answer": "A"},
        {"grade": 1, "topic": "Saat Okuma", "question_text": "Saat 1:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "1'de", "option_c": "2'de", "option_d": "3'te", "correct_answer": "B"},
        
        # 8. Paralarımız - Türk lirası tanıma
        {"grade": 1, "topic": "Türk Lirası Tanıma", "question_text": "1 TL kaç kuruştur?", "option_a": "50", "option_b": "75", "option_c": "100", "option_d": "150", "correct_answer": "C"},
        {"grade": 1, "topic": "Türk Lirası Tanıma", "question_text": "5 TL kaç kuruştur?", "option_a": "250", "option_b": "400", "option_c": "500", "option_d": "750", "correct_answer": "C"},
        {"grade": 1, "topic": "Türk Lirası Tanıma", "question_text": "10 TL kaç kuruştur?", "option_a": "500", "option_b": "750", "option_c": "1000", "option_d": "1500", "correct_answer": "C"},
        {"grade": 1, "topic": "Türk Lirası Tanıma", "question_text": "25 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "A"},
        {"grade": 1, "topic": "Türk Lirası Tanıma", "question_text": "50 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "B"},
        
        # 8. Paralarımız - Para ile alışveriş yapma
        {"grade": 1, "topic": "Para ile Alışveriş", "question_text": "2 TL'lik kalem + 3 TL'lik defter = kaç TL eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Para ile Alışveriş", "question_text": "5 TL'lik oyuncak + 2 TL'lik şeker = kaç TL eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Para ile Alışveriş", "question_text": "10 TL'lik kitap - 3 TL indirim = kaç TL eder?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Para ile Alışveriş", "question_text": "8 TL'lik çanta - 2 TL indirim = kaç TL eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Para ile Alışveriş", "question_text": "15 TL'lik ayakkabı - 5 TL indirim = kaç TL eder?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        
        # 9. Uzunluk Ölçme - Uzun–kısa kavramı
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangisi daha uzundur?", "option_a": "Kalem", "option_b": "Cetvel", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangisi daha kısadır?", "option_a": "Ağaç", "option_b": "Çiçek", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangisi daha uzundur?", "option_a": "Kedi", "option_b": "Fil", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangisi daha kısadır?", "option_a": "Gökdelen", "option_b": "Ev", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangisi daha uzundur?", "option_a": "Kurşun kalem", "option_b": "Tükenmez kalem", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # 10. Ağırlık Ölçme - Hafif–ağır kavramları
        {"grade": 1, "topic": "Ağırlık Ölçme", "question_text": "Hangisi daha ağırdır?", "option_a": "Tüy", "option_b": "Taş", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Ağırlık Ölçme", "question_text": "Hangisi daha hafiftir?", "option_a": "Demir", "option_b": "Pamuk", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Ağırlık Ölçme", "question_text": "Hangisi daha ağırdır?", "option_a": "Kedi", "option_b": "Fil", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Ağırlık Ölçme", "question_text": "Hangisi daha hafiftir?", "option_a": "Araba", "option_b": "Bisiklet", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Ağırlık Ölçme", "question_text": "Hangisi daha ağırdır?", "option_a": "Kağıt", "option_b": "Kitap", "option_c": "İkisi de aynı", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # 11. Veri Toplama ve Grafik
        {"grade": 1, "topic": "Veri Toplama ve Grafik", "question_text": "5 öğrenci elma, 3 öğrenci armut seviyor. Kaç öğrenci vardır?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 1, "topic": "Veri Toplama ve Grafik", "question_text": "4 çocuk kırmızı, 6 çocuk mavi renk seviyor. Kaç çocuk vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Veri Toplama ve Grafik", "question_text": "3 kedi, 2 köpek, 1 kuş var. Kaç hayvan vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Veri Toplama ve Grafik", "question_text": "2 büyük kutu, 5 küçük kutu var. Kaç kutu vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Veri Toplama ve Grafik", "question_text": "7 kırmızı top, 3 mavi top var. Kaç top vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"}
    ]
    
    try:
        # Veritabanına bağlan
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Mevcut 1. sınıf sorularını sil
            cursor.execute("DELETE FROM questions WHERE grade = 1")
            print("Mevcut 1. sınıf soruları silindi.")
            
            # Yeni soruları ekle
            for question in grade1_questions:
                cursor.execute("""
                    INSERT INTO questions (grade, topic, question_text, option_a, option_b, option_c, option_d, correct_answer)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    question['grade'],
                    question['topic'],
                    question['question_text'],
                    question['option_a'],
                    question['option_b'],
                    question['option_c'],
                    question['option_d'],
                    question['correct_answer']
                ))
            
            connection.commit()
            print(f"Toplam {len(grade1_questions)} soru başarıyla eklendi!")
            print("1. Sınıf: Yeni müfredata göre sorular hazırlandı")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

if __name__ == "__main__":
    insert_questions() 