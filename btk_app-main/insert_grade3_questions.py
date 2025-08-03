import mysql.connector
from config import DB_CONFIG

def insert_grade3_questions():
    """3. sınıf için yeni müfredata göre soruları ekler"""
    
    # 3. sınıf soruları - yeni müfredat
    grade3_questions = [
        # 1. Doğal Sayılar - 4 basamaklı doğal sayılar
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "2345 sayısı kaç basamaklıdır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "7890 sayısının binler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "4567 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "1234 sayısının onlar basamağında hangi rakam vardır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "9999 sayısından sonra hangi sayı gelir?", "option_a": "9998", "option_b": "9999", "option_c": "10000", "option_d": "10001", "correct_answer": "C"},
        
        # 1. Doğal Sayılar - Basamak değeri
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "3456 sayısının binler basamağının değeri kaçtır?", "option_a": "3", "option_b": "30", "option_c": "300", "option_d": "3000", "correct_answer": "D"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "5678 sayısının yüzler basamağının değeri kaçtır?", "option_a": "5", "option_b": "50", "option_c": "500", "option_d": "600", "correct_answer": "D"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "2345 sayısının onlar basamağının değeri kaçtır?", "option_a": "2", "option_b": "20", "option_c": "30", "option_d": "40", "correct_answer": "D"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "6789 sayısının birler basamağının değeri kaçtır?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "D"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "1234 sayısının binler basamağının değeri kaçtır?", "option_a": "1", "option_b": "10", "option_c": "100", "option_d": "1000", "correct_answer": "D"},
        
        # 1. Doğal Sayılar - Çözümleme
        {"grade": 3, "topic": "Çözümleme", "question_text": "3456 sayısının çözümlemesi hangisidir?", "option_a": "3000+400+50+6", "option_b": "3000+456", "option_c": "3450+6", "option_d": "3456", "correct_answer": "A"},
        {"grade": 3, "topic": "Çözümleme", "question_text": "7890 sayısının çözümlemesi hangisidir?", "option_a": "7000+800+90+0", "option_b": "7000+890", "option_c": "7890", "option_d": "789+0", "correct_answer": "A"},
        {"grade": 3, "topic": "Çözümleme", "question_text": "2345 sayısının çözümlemesi hangisidir?", "option_a": "2000+300+40+5", "option_b": "2000+345", "option_c": "2340+5", "option_d": "2345", "correct_answer": "A"},
        {"grade": 3, "topic": "Çözümleme", "question_text": "5678 sayısının çözümlemesi hangisidir?", "option_a": "5000+600+70+8", "option_b": "5000+678", "option_c": "5670+8", "option_d": "5678", "correct_answer": "A"},
        {"grade": 3, "topic": "Çözümleme", "question_text": "1234 sayısının çözümlemesi hangisidir?", "option_a": "1000+200+30+4", "option_b": "1000+234", "option_c": "1230+4", "option_d": "1234", "correct_answer": "A"},
        
        # 1. Doğal Sayılar - Sayı karşılaştırma ve sıralama
        {"grade": 3, "topic": "Sayı Karşılaştırma ve Sıralama", "question_text": "2345 ile 5432 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayı Karşılaştırma ve Sıralama", "question_text": "6789 ile 9876 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayı Karşılaştırma ve Sıralama", "question_text": "9999 ile 9999 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "C"},
        {"grade": 3, "topic": "Sayı Karşılaştırma ve Sıralama", "question_text": "1234 ile 4321 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayı Karşılaştırma ve Sıralama", "question_text": "4567 ile 7654 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        
        # 2. Toplama ve Çıkarma İşlemleri - 4 basamaklı sayılarla toplama
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "2345 + 1234 = ?", "option_a": "3456", "option_b": "3567", "option_c": "3579", "option_d": "3679", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "4567 + 2345 = ?", "option_a": "6800", "option_b": "6900", "option_c": "6912", "option_d": "7000", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "5678 + 1234 = ?", "option_a": "6800", "option_b": "6900", "option_c": "6912", "option_d": "7000", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "7890 + 1110 = ?", "option_a": "8900", "option_b": "9000", "option_c": "9100", "option_d": "9200", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "3456 + 2554 = ?", "option_a": "5900", "option_b": "6000", "option_c": "6010", "option_d": "6100", "correct_answer": "C"},
        
        # 2. Toplama ve Çıkarma İşlemleri - 4 basamaklı sayılarla çıkarma
        {"grade": 3, "topic": "4 Basamaklı Çıkarma", "question_text": "4567 - 1234 = ?", "option_a": "3233", "option_b": "3333", "option_c": "3433", "option_d": "3533", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Çıkarma", "question_text": "7890 - 2345 = ?", "option_a": "5445", "option_b": "5545", "option_c": "5645", "option_d": "5745", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Çıkarma", "question_text": "5678 - 1234 = ?", "option_a": "4344", "option_b": "4444", "option_c": "4544", "option_d": "4644", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Çıkarma", "question_text": "9999 - 1111 = ?", "option_a": "8778", "option_b": "8888", "option_c": "8988", "option_d": "9088", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Çıkarma", "question_text": "6789 - 2345 = ?", "option_a": "4344", "option_b": "4444", "option_c": "4544", "option_d": "4644", "correct_answer": "B"},
        
        # 3. Çarpma İşlemi - Çarpım tablosu
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "8 x 9 = ?", "option_a": "70", "option_b": "72", "option_c": "74", "option_d": "76", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "7 x 8 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "9 x 7 = ?", "option_a": "61", "option_b": "63", "option_c": "65", "option_d": "67", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "6 x 9 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "5 x 8 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        
        # 3. Çarpma İşlemi - Çok basamaklı sayılarla çarpma
        {"grade": 3, "topic": "Çok Basamaklı Çarpma", "question_text": "234 x 5 = ?", "option_a": "1150", "option_b": "1170", "option_c": "1190", "option_d": "1210", "correct_answer": "B"},
        {"grade": 3, "topic": "Çok Basamaklı Çarpma", "question_text": "456 x 3 = ?", "option_a": "1348", "option_b": "1368", "option_c": "1388", "option_d": "1408", "correct_answer": "B"},
        {"grade": 3, "topic": "Çok Basamaklı Çarpma", "question_text": "567 x 4 = ?", "option_a": "2248", "option_b": "2268", "option_c": "2288", "option_d": "2308", "correct_answer": "B"},
        {"grade": 3, "topic": "Çok Basamaklı Çarpma", "question_text": "789 x 2 = ?", "option_a": "1568", "option_b": "1578", "option_c": "1588", "option_d": "1598", "correct_answer": "B"},
        {"grade": 3, "topic": "Çok Basamaklı Çarpma", "question_text": "345 x 6 = ?", "option_a": "2050", "option_b": "2070", "option_c": "2090", "option_d": "2110", "correct_answer": "B"},
        
        # 3. Çarpma İşlemi - 10 ve 100 ile kısa yoldan çarpma
        {"grade": 3, "topic": "10 ve 100 ile Çarpma", "question_text": "45 x 10 = ?", "option_a": "450", "option_b": "460", "option_c": "470", "option_d": "480", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Çarpma", "question_text": "67 x 100 = ?", "option_a": "670", "option_b": "6700", "option_c": "67000", "option_d": "670000", "correct_answer": "B"},
        {"grade": 3, "topic": "10 ve 100 ile Çarpma", "question_text": "23 x 10 = ?", "option_a": "230", "option_b": "240", "option_c": "250", "option_d": "260", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Çarpma", "question_text": "89 x 100 = ?", "option_a": "890", "option_b": "8900", "option_c": "89000", "option_d": "890000", "correct_answer": "B"},
        {"grade": 3, "topic": "10 ve 100 ile Çarpma", "question_text": "34 x 10 = ?", "option_a": "340", "option_b": "350", "option_c": "360", "option_d": "370", "correct_answer": "A"},
        
        # 4. Bölme İşlemi - Kalansız bölme
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "24 ÷ 6 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "35 ÷ 7 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "48 ÷ 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "63 ÷ 9 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "42 ÷ 6 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        
        # 4. Bölme İşlemi - Kalanlı bölme
        {"grade": 3, "topic": "Kalanlı Bölme", "question_text": "25 ÷ 6 = ? (kalan kaç?)", "option_a": "4 kalan 1", "option_b": "4 kalan 2", "option_c": "5 kalan 1", "option_d": "5 kalan 2", "correct_answer": "A"},
        {"grade": 3, "topic": "Kalanlı Bölme", "question_text": "37 ÷ 8 = ? (kalan kaç?)", "option_a": "4 kalan 3", "option_b": "4 kalan 5", "option_c": "5 kalan 1", "option_d": "5 kalan 2", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalanlı Bölme", "question_text": "49 ÷ 9 = ? (kalan kaç?)", "option_a": "4 kalan 4", "option_b": "4 kalan 5", "option_c": "5 kalan 4", "option_d": "5 kalan 5", "correct_answer": "C"},
        {"grade": 3, "topic": "Kalanlı Bölme", "question_text": "58 ÷ 7 = ? (kalan kaç?)", "option_a": "7 kalan 1", "option_b": "7 kalan 2", "option_c": "8 kalan 1", "option_d": "8 kalan 2", "correct_answer": "C"},
        {"grade": 3, "topic": "Kalanlı Bölme", "question_text": "67 ÷ 8 = ? (kalan kaç?)", "option_a": "7 kalan 3", "option_b": "7 kalan 4", "option_c": "8 kalan 3", "option_d": "8 kalan 4", "correct_answer": "C"},
        
        # 4. Bölme İşlemi - 10 ve 100 ile bölme
        {"grade": 3, "topic": "10 ve 100 ile Bölme", "question_text": "450 ÷ 10 = ?", "option_a": "45", "option_b": "46", "option_c": "47", "option_d": "48", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Bölme", "question_text": "6700 ÷ 100 = ?", "option_a": "67", "option_b": "68", "option_c": "69", "option_d": "70", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Bölme", "question_text": "230 ÷ 10 = ?", "option_a": "23", "option_b": "24", "option_c": "25", "option_d": "26", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Bölme", "question_text": "8900 ÷ 100 = ?", "option_a": "89", "option_b": "90", "option_c": "91", "option_d": "92", "correct_answer": "A"},
        {"grade": 3, "topic": "10 ve 100 ile Bölme", "question_text": "340 ÷ 10 = ?", "option_a": "34", "option_b": "35", "option_c": "36", "option_d": "37", "correct_answer": "A"},
        
        # 5. Kesirler - Bütün, yarım, çeyrek
        {"grade": 3, "topic": "Bütün Yarım Çeyrek", "question_text": "Bir pizzanın yarısı kaç dilim eder?", "option_a": "2", "option_b": "4", "option_c": "6", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Bütün Yarım Çeyrek", "question_text": "Bir elmanın çeyreği kaç parça eder?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "A"},
        {"grade": 3, "topic": "Bütün Yarım Çeyrek", "question_text": "Bir kekin yarısı kaç dilim eder?", "option_a": "2", "option_b": "4", "option_c": "6", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Bütün Yarım Çeyrek", "question_text": "Bir portakalın çeyreği kaç dilim eder?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "A"},
        {"grade": 3, "topic": "Bütün Yarım Çeyrek", "question_text": "Bir ekmeğin yarısı kaç dilim eder?", "option_a": "2", "option_b": "4", "option_c": "6", "option_d": "8", "correct_answer": "B"},
        
        # 5. Kesirler - Basit kesirleri tanıma
        {"grade": 3, "topic": "Basit Kesirler", "question_text": "1/2 kesri nasıl okunur?", "option_a": "Bir ikinci", "option_b": "İkide bir", "option_c": "Yarım", "option_d": "Çeyrek", "correct_answer": "C"},
        {"grade": 3, "topic": "Basit Kesirler", "question_text": "1/4 kesri nasıl okunur?", "option_a": "Bir dördüncü", "option_b": "Dörtte bir", "option_c": "Yarım", "option_d": "Çeyrek", "correct_answer": "D"},
        {"grade": 3, "topic": "Basit Kesirler", "question_text": "3/4 kesri nasıl okunur?", "option_a": "Üç dördüncü", "option_b": "Dörtte üç", "option_c": "Yarım", "option_d": "Çeyrek", "correct_answer": "B"},
        {"grade": 3, "topic": "Basit Kesirler", "question_text": "1/3 kesri nasıl okunur?", "option_a": "Bir üçüncü", "option_b": "Üçte bir", "option_c": "Yarım", "option_d": "Çeyrek", "correct_answer": "B"},
        {"grade": 3, "topic": "Basit Kesirler", "question_text": "2/3 kesri nasıl okunur?", "option_a": "İki üçüncü", "option_b": "Üçte iki", "option_c": "Yarım", "option_d": "Çeyrek", "correct_answer": "B"},
        
        # 5. Kesirler - Kesirleri karşılaştırma
        {"grade": 3, "topic": "Kesirleri Karşılaştırma", "question_text": "1/2 ile 1/4 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "B"},
        {"grade": 3, "topic": "Kesirleri Karşılaştırma", "question_text": "1/4 ile 3/4 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 3, "topic": "Kesirleri Karşılaştırma", "question_text": "2/3 ile 1/3 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "B"},
        {"grade": 3, "topic": "Kesirleri Karşılaştırma", "question_text": "1/2 ile 1/2 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "C"},
        {"grade": 3, "topic": "Kesirleri Karşılaştırma", "question_text": "1/4 ile 1/3 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        
        # 6. Geometrik Cisimler ve Şekiller - Düzlemsel şekiller
        {"grade": 3, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Çember", "correct_answer": "C"},
        {"grade": 3, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 kenarlı ve tüm kenarları eşittir?", "option_a": "Dikdörtgen", "option_b": "Kare", "option_c": "Üçgen", "option_d": "Çember", "correct_answer": "B"},
        {"grade": 3, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "D"},
        {"grade": 3, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Çember", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 3, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "D"},
        
        # 6. Geometrik Cisimler ve Şekiller - Geometrik cisimler
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küre şeklindedir?", "option_a": "Zar", "option_b": "Top", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim silindir şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Kutu", "option_d": "Koni", "correct_answer": "C"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim koni şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Dondurma külahı", "correct_answer": "D"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim dikdörtgen prizma şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Kutu", "option_d": "Koni", "correct_answer": "C"},
        
        # 6. Geometrik Cisimler ve Şekiller - Açıları tanıma
        {"grade": 3, "topic": "Açıları Tanıma", "question_text": "90 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Doğru açı", "option_c": "Geniş açı", "option_d": "Düz açı", "correct_answer": "B"},
        {"grade": 3, "topic": "Açıları Tanıma", "question_text": "45 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Doğru açı", "option_c": "Geniş açı", "option_d": "Düz açı", "correct_answer": "A"},
        {"grade": 3, "topic": "Açıları Tanıma", "question_text": "120 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Doğru açı", "option_c": "Geniş açı", "option_d": "Düz açı", "correct_answer": "C"},
        {"grade": 3, "topic": "Açıları Tanıma", "question_text": "30 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Doğru açı", "option_c": "Geniş açı", "option_d": "Düz açı", "correct_answer": "A"},
        {"grade": 3, "topic": "Açıları Tanıma", "question_text": "150 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Doğru açı", "option_c": "Geniş açı", "option_d": "Düz açı", "correct_answer": "C"},
        
        # 7. Uzunluk Ölçme - Birimler arası dönüşüm
        {"grade": 3, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "100 cm kaç metredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "1000 m kaç kilometredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "200 cm kaç metredir?", "option_a": "0.2", "option_b": "2", "option_c": "20", "option_d": "200", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "5000 m kaç kilometredir?", "option_a": "0.5", "option_b": "5", "option_c": "50", "option_d": "500", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "150 cm kaç metredir?", "option_a": "0.15", "option_b": "1.5", "option_c": "15", "option_d": "150", "correct_answer": "B"},
        
        # 8. Ağırlık Ölçme - Birimler arası dönüşüm
        {"grade": 3, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "1000 g kaç kilogramdır?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 3, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "2000 g kaç kilogramdır?", "option_a": "0.2", "option_b": "2", "option_c": "20", "option_d": "200", "correct_answer": "B"},
        {"grade": 3, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "500 g kaç kilogramdır?", "option_a": "0.05", "option_b": "0.5", "option_c": "5", "option_d": "50", "correct_answer": "B"},
        {"grade": 3, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "3000 g kaç kilogramdır?", "option_a": "0.3", "option_b": "3", "option_c": "30", "option_d": "300", "correct_answer": "B"},
        {"grade": 3, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "1500 g kaç kilogramdır?", "option_a": "0.15", "option_b": "1.5", "option_c": "15", "option_d": "150", "correct_answer": "B"},
        
        # 10. Zaman Ölçme - Takvim
        {"grade": 3, "topic": "Takvim", "question_text": "1 yıl kaç aydır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 3, "topic": "Takvim", "question_text": "1 ay kaç haftadır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 3, "topic": "Takvim", "question_text": "1 hafta kaç gündür?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 3, "topic": "Takvim", "question_text": "1 yıl kaç gündür?", "option_a": "360", "option_b": "365", "option_c": "370", "option_d": "375", "correct_answer": "B"},
        {"grade": 3, "topic": "Takvim", "question_text": "1 ay kaç gündür?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        
        # 10. Zaman Ölçme - Saat okuma
        {"grade": 3, "topic": "Saat Okuma", "question_text": "Saat 3:45'te akrep nerede olur?", "option_a": "3'te", "option_b": "3 ile 4 arasında", "option_c": "4'te", "option_d": "6'da", "correct_answer": "B"},
        {"grade": 3, "topic": "Saat Okuma", "question_text": "Saat 6:30'da akrep nerede olur?", "option_a": "6'da", "option_b": "6 ile 7 arasında", "option_c": "7'de", "option_d": "3'te", "correct_answer": "B"},
        {"grade": 3, "topic": "Saat Okuma", "question_text": "Saat 9:15'te akrep nerede olur?", "option_a": "9'da", "option_b": "9 ile 10 arasında", "option_c": "10'da", "option_d": "12'de", "correct_answer": "B"},
        {"grade": 3, "topic": "Saat Okuma", "question_text": "Saat 12:00'da akrep nerede olur?", "option_a": "12'de", "option_b": "1'de", "option_c": "6'da", "option_d": "9'da", "correct_answer": "A"},
        {"grade": 3, "topic": "Saat Okuma", "question_text": "Saat 2:20'de akrep nerede olur?", "option_a": "2'de", "option_b": "2 ile 3 arasında", "option_c": "3'te", "option_d": "6'da", "correct_answer": "B"},
        
        # 11. Veri Toplama ve Değerlendirme - Sıklık tablosu
        {"grade": 3, "topic": "Sıklık Tablosu", "question_text": "5 öğrenci elma, 3 öğrenci armut, 2 öğrenci muz, 4 öğrenci portakal seviyor. Kaç öğrenci vardır?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 3, "topic": "Sıklık Tablosu", "question_text": "4 çocuk kırmızı, 6 çocuk mavi, 3 çocuk yeşil, 5 çocuk sarı renk seviyor. Kaç çocuk vardır?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "C"},
        {"grade": 3, "topic": "Sıklık Tablosu", "question_text": "3 kedi, 2 köpek, 1 kuş, 4 balık, 2 tavşan var. Kaç hayvan vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 3, "topic": "Sıklık Tablosu", "question_text": "2 büyük kutu, 5 küçük kutu, 3 orta kutu, 4 yuvarlak kutu var. Kaç kutu vardır?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 3, "topic": "Sıklık Tablosu", "question_text": "7 kırmızı top, 3 mavi top, 2 yeşil top, 6 sarı top var. Kaç top vardır?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "C"}
    ]
    
    try:
        # Veritabanına bağlan
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Mevcut 3. sınıf sorularını sil
            cursor.execute("DELETE FROM questions WHERE grade = 3")
            print("Mevcut 3. sınıf soruları silindi.")
            
            # Yeni soruları ekle
            for question in grade3_questions:
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
            print(f"Toplam {len(grade3_questions)} soru başarıyla eklendi!")
            print("3. Sınıf: Yeni müfredata göre sorular hazırlandı")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

if __name__ == "__main__":
    insert_grade3_questions() 