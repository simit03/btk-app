import mysql.connector
from config import DB_CONFIG

def insert_grade2_questions():
    """2. sınıf için yeni müfredata göre soruları ekler"""
    
    # 2. sınıf soruları - yeni müfredat
    grade2_questions = [
        # 1. Doğal Sayılar - 3 basamaklı sayılar
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "234 sayısı kaç basamaklıdır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "789 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "456 sayısının onlar basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "0", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "123 sayısının birler basamağında hangi rakam vardır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "0", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "999 sayısından sonra hangi sayı gelir?", "option_a": "998", "option_b": "999", "option_c": "1000", "option_d": "1001", "correct_answer": "C"},
        
        # 1. Doğal Sayılar - Sayı okuma ve yazma
        {"grade": 2, "topic": "Sayı Okuma ve Yazma", "question_text": "Yüz yirmi üç sayısı nasıl yazılır?", "option_a": "120", "option_b": "123", "option_c": "132", "option_d": "213", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayı Okuma ve Yazma", "question_text": "Üç yüz kırk beş sayısı nasıl yazılır?", "option_a": "345", "option_b": "354", "option_c": "435", "option_d": "453", "correct_answer": "A"},
        {"grade": 2, "topic": "Sayı Okuma ve Yazma", "question_text": "567 sayısı nasıl okunur?", "option_a": "Beş yüz altmış yedi", "option_b": "Beş yüz yetmiş altı", "option_c": "Altı yüz elli yedi", "option_d": "Altı yüz yetmiş beş", "correct_answer": "A"},
        {"grade": 2, "topic": "Sayı Okuma ve Yazma", "question_text": "Dokuz yüz doksan dokuz sayısı nasıl yazılır?", "option_a": "909", "option_b": "990", "option_c": "999", "option_d": "900", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Okuma ve Yazma", "question_text": "234 sayısı nasıl okunur?", "option_a": "İki yüz otuz dört", "option_b": "İki yüz kırk üç", "option_c": "Üç yüz yirmi dört", "option_d": "Üç yüz kırk iki", "correct_answer": "A"},
        
        # 1. Doğal Sayılar - Basamak değeri ve çözümleme
        {"grade": 2, "topic": "Basamak Değeri ve Çözümleme", "question_text": "456 sayısının çözümlemesi hangisidir?", "option_a": "400+50+6", "option_b": "400+56", "option_c": "450+6", "option_d": "456", "correct_answer": "A"},
        {"grade": 2, "topic": "Basamak Değeri ve Çözümleme", "question_text": "789 sayısının yüzler basamağının değeri kaçtır?", "option_a": "7", "option_b": "70", "option_c": "700", "option_d": "7000", "correct_answer": "C"},
        {"grade": 2, "topic": "Basamak Değeri ve Çözümleme", "question_text": "234 sayısının onlar basamağının değeri kaçtır?", "option_a": "2", "option_b": "20", "option_c": "30", "option_d": "200", "correct_answer": "C"},
        {"grade": 2, "topic": "Basamak Değeri ve Çözümleme", "question_text": "567 sayısının birler basamağının değeri kaçtır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "70", "correct_answer": "C"},
        {"grade": 2, "topic": "Basamak Değeri ve Çözümleme", "question_text": "123 sayısının çözümlemesi hangisidir?", "option_a": "100+20+3", "option_b": "120+3", "option_c": "100+23", "option_d": "123", "correct_answer": "A"},
        
        # 1. Doğal Sayılar - Sıralama ve karşılaştırma
        {"grade": 2, "topic": "Sıralama ve Karşılaştırma", "question_text": "234 ile 432 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 2, "topic": "Sıralama ve Karşılaştırma", "question_text": "567 ile 765 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 2, "topic": "Sıralama ve Karşılaştırma", "question_text": "999 ile 999 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "C"},
        {"grade": 2, "topic": "Sıralama ve Karşılaştırma", "question_text": "123 ile 321 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 2, "topic": "Sıralama ve Karşılaştırma", "question_text": "456 ile 654 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        
        # 1. Doğal Sayılar - Sayı örüntüleri
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "2, 4, 6, 8, ? örüntüsünde ? yerine ne gelir?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "5, 10, 15, 20, ? örüntüsünde ? yerine ne gelir?", "option_a": "22", "option_b": "25", "option_c": "30", "option_d": "35", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "100, 200, 300, 400, ? örüntüsünde ? yerine ne gelir?", "option_a": "450", "option_b": "500", "option_c": "550", "option_d": "600", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "3, 6, 9, 12, ? örüntüsünde ? yerine ne gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "10, 20, 30, 40, ? örüntüsünde ? yerine ne gelir?", "option_a": "45", "option_b": "50", "option_c": "55", "option_d": "60", "correct_answer": "B"},
        
        # 2. Toplama ve Çıkarma İşlemleri - 3 basamaklı sayılarla toplama
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "234 + 123 = ?", "option_a": "345", "option_b": "356", "option_c": "357", "option_d": "367", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "456 + 234 = ?", "option_a": "680", "option_b": "690", "option_c": "700", "option_d": "710", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "567 + 123 = ?", "option_a": "680", "option_b": "690", "option_c": "700", "option_d": "710", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "789 + 111 = ?", "option_a": "890", "option_b": "900", "option_c": "910", "option_d": "920", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "345 + 255 = ?", "option_a": "590", "option_b": "600", "option_c": "610", "option_d": "620", "correct_answer": "B"},
        
        # 2. Toplama ve Çıkarma İşlemleri - 3 basamaklı sayılarla çıkarma
        {"grade": 2, "topic": "3 Basamaklı Çıkarma", "question_text": "456 - 123 = ?", "option_a": "323", "option_b": "333", "option_c": "343", "option_d": "353", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Çıkarma", "question_text": "789 - 234 = ?", "option_a": "545", "option_b": "555", "option_c": "565", "option_d": "575", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Çıkarma", "question_text": "567 - 123 = ?", "option_a": "434", "option_b": "444", "option_c": "454", "option_d": "464", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Çıkarma", "question_text": "999 - 111 = ?", "option_a": "878", "option_b": "888", "option_c": "898", "option_d": "908", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Çıkarma", "question_text": "678 - 234 = ?", "option_a": "434", "option_b": "444", "option_c": "454", "option_d": "464", "correct_answer": "B"},
        
        # 2. Toplama ve Çıkarma İşlemleri - Eksik eleman bulma
        {"grade": 2, "topic": "Eksik Eleman Bulma", "question_text": "? + 123 = 456", "option_a": "323", "option_b": "333", "option_c": "343", "option_d": "353", "correct_answer": "B"},
        {"grade": 2, "topic": "Eksik Eleman Bulma", "question_text": "234 + ? = 567", "option_a": "323", "option_b": "333", "option_c": "343", "option_d": "353", "correct_answer": "B"},
        {"grade": 2, "topic": "Eksik Eleman Bulma", "question_text": "? - 123 = 234", "option_a": "345", "option_b": "355", "option_c": "357", "option_d": "367", "correct_answer": "C"},
        {"grade": 2, "topic": "Eksik Eleman Bulma", "question_text": "456 - ? = 123", "option_a": "323", "option_b": "333", "option_c": "343", "option_d": "353", "correct_answer": "B"},
        {"grade": 2, "topic": "Eksik Eleman Bulma", "question_text": "? + 234 = 789", "option_a": "545", "option_b": "555", "option_c": "565", "option_d": "575", "correct_answer": "B"},
        
        # 3. Çarpma İşlemi - Çarpma işleminin anlamı
        {"grade": 2, "topic": "Çarpma İşleminin Anlamı", "question_text": "3 x 4 = 12 ise 3 tane 4'lü grup kaç eder?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşleminin Anlamı", "question_text": "5 x 2 = 10 ise 5 tane 2'li grup kaç eder?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşleminin Anlamı", "question_text": "2 x 6 = 12 ise 2 tane 6'lı grup kaç eder?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşleminin Anlamı", "question_text": "4 x 3 = 12 ise 4 tane 3'lü grup kaç eder?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşleminin Anlamı", "question_text": "6 x 2 = 12 ise 6 tane 2'li grup kaç eder?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        
        # 3. Çarpma İşlemi - Çarpım tablosu
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "7 x 8 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "6 x 9 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "8 x 7 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "9 x 6 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "5 x 8 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        
        # 3. Çarpma İşlemi - Çarpma problemleri
        {"grade": 2, "topic": "Çarpma Problemleri", "question_text": "Her kutuda 6 kalem var. 8 kutuda kaç kalem vardır?", "option_a": "42", "option_b": "46", "option_c": "48", "option_d": "52", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma Problemleri", "question_text": "Her sırada 7 öğrenci var. 5 sırada kaç öğrenci vardır?", "option_a": "30", "option_b": "32", "option_c": "35", "option_d": "38", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma Problemleri", "question_text": "Her pakette 8 bisküvi var. 4 pakette kaç bisküvi vardır?", "option_a": "28", "option_b": "30", "option_c": "32", "option_d": "36", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma Problemleri", "question_text": "Her kutuya 9 elma konuluyor. 6 kutuda kaç elma vardır?", "option_a": "48", "option_b": "52", "option_c": "54", "option_d": "58", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma Problemleri", "question_text": "Her masada 5 kişi oturuyor. 7 masada kaç kişi vardır?", "option_a": "30", "option_b": "32", "option_c": "35", "option_d": "38", "correct_answer": "C"},
        
        # 4. Bölme İşlemi - Eşit gruplara ayırma
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "12 elmayı 3 kişiye eşit paylaştırırsak her kişiye kaç elma düşer?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "15 kalemi 5 kişiye eşit paylaştırırsak her kişiye kaç kalem düşer?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "18 bisküviyi 6 kişiye eşit paylaştırırsak her kişiye kaç bisküvi düşer?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "20 çiçeği 4 vazoya eşit koyarsak her vazoda kaç çiçek olur?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "16 topu 2 gruba eşit paylaştırırsak her grupta kaç top olur?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        
        # 4. Bölme İşlemi - Kalanlı/kalansız bölme
        {"grade": 2, "topic": "Kalanlı/Kalansız Bölme", "question_text": "14 ÷ 3 = ? (kalan kaç?)", "option_a": "4 kalan 1", "option_b": "4 kalan 2", "option_c": "5 kalan 1", "option_d": "5 kalan 2", "correct_answer": "B"},
        {"grade": 2, "topic": "Kalanlı/Kalansız Bölme", "question_text": "17 ÷ 4 = ? (kalan kaç?)", "option_a": "3 kalan 1", "option_b": "3 kalan 2", "option_c": "4 kalan 1", "option_d": "4 kalan 2", "correct_answer": "C"},
        {"grade": 2, "topic": "Kalanlı/Kalansız Bölme", "question_text": "19 ÷ 5 = ? (kalan kaç?)", "option_a": "3 kalan 2", "option_b": "3 kalan 4", "option_c": "4 kalan 1", "option_d": "4 kalan 2", "correct_answer": "B"},
        {"grade": 2, "topic": "Kalanlı/Kalansız Bölme", "question_text": "16 ÷ 4 = ? (kalan var mı?)", "option_a": "3 kalan 1", "option_b": "3 kalan 2", "option_c": "4 kalan 0", "option_d": "4 kalan 1", "correct_answer": "C"},
        {"grade": 2, "topic": "Kalanlı/Kalansız Bölme", "question_text": "18 ÷ 6 = ? (kalan var mı?)", "option_a": "2 kalan 1", "option_b": "2 kalan 2", "option_c": "3 kalan 0", "option_d": "3 kalan 1", "correct_answer": "C"},
        
        # 5. Geometrik Şekiller - Düzlemsel şekiller
        {"grade": 2, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 kenarlı ve tüm kenarları eşittir?", "option_a": "Dikdörtgen", "option_b": "Kare", "option_c": "Üçgen", "option_d": "Çember", "correct_answer": "B"},
        {"grade": 2, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Çember", "correct_answer": "C"},
        {"grade": 2, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "D"},
        {"grade": 2, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Çember", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 2, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "D"},
        
        # 5. Geometrik Şekiller - Geometrik cisimler
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küre şeklindedir?", "option_a": "Zar", "option_b": "Top", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim silindir şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Kutu", "option_d": "Koni", "correct_answer": "C"},
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim koni şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Dondurma külahı", "correct_answer": "D"},
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim dikdörtgen prizma şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Kutu", "option_d": "Koni", "correct_answer": "C"},
        
        # 6. Uzunluk Ölçme - Standart ölçme birimi
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "1 metre kaç santimetredir?", "option_a": "10", "option_b": "50", "option_c": "100", "option_d": "1000", "correct_answer": "C"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "50 cm + 50 cm = kaç metredir?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "B"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "2 metre kaç santimetredir?", "option_a": "100", "option_b": "150", "option_c": "200", "option_d": "250", "correct_answer": "C"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "150 cm kaç metredir?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "C"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "3 metre kaç santimetredir?", "option_a": "200", "option_b": "250", "option_c": "300", "option_d": "350", "correct_answer": "C"},
        
        # 7. Ağırlık Ölçme - Gram ve kilogram
        {"grade": 2, "topic": "Ağırlık Ölçme", "question_text": "1 kilogram kaç gramdır?", "option_a": "10", "option_b": "50", "option_c": "100", "option_d": "1000", "correct_answer": "D"},
        {"grade": 2, "topic": "Ağırlık Ölçme", "question_text": "500 gram kaç kilogramdır?", "option_a": "0.1", "option_b": "0.5", "option_c": "1", "option_d": "1.5", "correct_answer": "B"},
        {"grade": 2, "topic": "Ağırlık Ölçme", "question_text": "2 kilogram kaç gramdır?", "option_a": "1000", "option_b": "1500", "option_c": "2000", "option_d": "2500", "correct_answer": "C"},
        {"grade": 2, "topic": "Ağırlık Ölçme", "question_text": "1500 gram kaç kilogramdır?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "C"},
        {"grade": 2, "topic": "Ağırlık Ölçme", "question_text": "3 kilogram kaç gramdır?", "option_a": "2000", "option_b": "2500", "option_c": "3000", "option_d": "3500", "correct_answer": "C"},
        
        # 8. Zaman Ölçme - Takvim
        {"grade": 2, "topic": "Takvim", "question_text": "1 hafta kaç gündür?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Takvim", "question_text": "1 ay kaç haftadır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 2, "topic": "Takvim", "question_text": "1 yıl kaç aydır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Takvim", "question_text": "1 yıl kaç gündür?", "option_a": "360", "option_b": "365", "option_c": "370", "option_d": "375", "correct_answer": "B"},
        {"grade": 2, "topic": "Takvim", "question_text": "1 ay kaç gündür?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        
        # 8. Zaman Ölçme - Saat okuma
        {"grade": 2, "topic": "Saat Okuma", "question_text": "Saat 3:30'da akrep nerede olur?", "option_a": "3'te", "option_b": "3 ile 4 arasında", "option_c": "4'te", "option_d": "6'da", "correct_answer": "B"},
        {"grade": 2, "topic": "Saat Okuma", "question_text": "Saat 6:15'te akrep nerede olur?", "option_a": "6'da", "option_b": "6 ile 7 arasında", "option_c": "7'de", "option_d": "3'te", "correct_answer": "B"},
        {"grade": 2, "topic": "Saat Okuma", "question_text": "Saat 9:45'te akrep nerede olur?", "option_a": "9'da", "option_b": "9 ile 10 arasında", "option_c": "10'da", "option_d": "12'de", "correct_answer": "B"},
        {"grade": 2, "topic": "Saat Okuma", "question_text": "Saat 12:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "1'de", "option_c": "6'da", "option_d": "9'da", "correct_answer": "A"},
        {"grade": 2, "topic": "Saat Okuma", "question_text": "Saat 2:15'te akrep nerede olur?", "option_a": "2'de", "option_b": "2 ile 3 arasında", "option_c": "3'te", "option_d": "6'da", "correct_answer": "B"},
        
        # 9. Paralarımız - Türk lirası ve kuruşları
        {"grade": 2, "topic": "Türk Lirası ve Kuruşları", "question_text": "1 TL kaç kuruştur?", "option_a": "50", "option_b": "75", "option_c": "100", "option_d": "150", "correct_answer": "C"},
        {"grade": 2, "topic": "Türk Lirası ve Kuruşları", "question_text": "50 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "B"},
        {"grade": 2, "topic": "Türk Lirası ve Kuruşları", "question_text": "25 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "A"},
        {"grade": 2, "topic": "Türk Lirası ve Kuruşları", "question_text": "75 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "C"},
        {"grade": 2, "topic": "Türk Lirası ve Kuruşları", "question_text": "2 TL kaç kuruştur?", "option_a": "150", "option_b": "200", "option_c": "250", "option_d": "300", "correct_answer": "B"},
        
        # 9. Paralarımız - Para üstü hesaplama
        {"grade": 2, "topic": "Para Üstü Hesaplama", "question_text": "5 TL'lik ürün için 10 TL verdim. Kaç TL para üstü alırım?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Üstü Hesaplama", "question_text": "3 TL'lik ürün için 5 TL verdim. Kaç TL para üstü alırım?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 2, "topic": "Para Üstü Hesaplama", "question_text": "7 TL'lik ürün için 10 TL verdim. Kaç TL para üstü alırım?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 2, "topic": "Para Üstü Hesaplama", "question_text": "4 TL'lik ürün için 10 TL verdim. Kaç TL para üstü alırım?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Üstü Hesaplama", "question_text": "6 TL'lik ürün için 10 TL verdim. Kaç TL para üstü alırım?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        
        # 10. Veri Toplama ve Değerlendirme - Sıklık tablosu
        {"grade": 2, "topic": "Sıklık Tablosu", "question_text": "5 öğrenci elma, 3 öğrenci armut, 2 öğrenci muz seviyor. Kaç öğrenci vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 2, "topic": "Sıklık Tablosu", "question_text": "4 çocuk kırmızı, 6 çocuk mavi, 3 çocuk yeşil renk seviyor. Kaç çocuk vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "D"},
        {"grade": 2, "topic": "Sıklık Tablosu", "question_text": "3 kedi, 2 köpek, 1 kuş, 4 balık var. Kaç hayvan vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 2, "topic": "Sıklık Tablosu", "question_text": "2 büyük kutu, 5 küçük kutu, 3 orta kutu var. Kaç kutu vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 2, "topic": "Sıklık Tablosu", "question_text": "7 kırmızı top, 3 mavi top, 2 yeşil top var. Kaç top vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"}
    ]
    
    try:
        # Veritabanına bağlan
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Mevcut 2. sınıf sorularını sil
            cursor.execute("DELETE FROM questions WHERE grade = 2")
            print("Mevcut 2. sınıf soruları silindi.")
            
            # Yeni soruları ekle
            for question in grade2_questions:
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
            print(f"Toplam {len(grade2_questions)} soru başarıyla eklendi!")
            print("2. Sınıf: Yeni müfredata göre sorular hazırlandı")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

if __name__ == "__main__":
    insert_grade2_questions() 