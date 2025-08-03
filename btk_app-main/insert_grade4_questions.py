import mysql.connector
from config import DB_CONFIG

def insert_grade4_questions():
    """4. sınıf için yeni müfredata göre soruları ekler"""
    
    # 4. sınıf soruları - yeni müfredat
    grade4_questions = [
        # 1. Doğal Sayılar - 6 basamaklı sayılar
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "123456 sayısı kaç basamaklıdır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "789012 sayısının yüz binler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "456789 sayısının on binler basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "234567 sayısının binler basamağında hangi rakam vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "999999 sayısından sonra hangi sayı gelir?", "option_a": "999998", "option_b": "999999", "option_c": "1000000", "option_d": "1000001", "correct_answer": "C"},
        
        # 1. Doğal Sayılar - Yuvarlama
        {"grade": 4, "topic": "Yuvarlama", "question_text": "123456 sayısını yüzler basamağına yuvarlayın", "option_a": "123400", "option_b": "123500", "option_c": "123600", "option_d": "123700", "correct_answer": "B"},
        {"grade": 4, "topic": "Yuvarlama", "question_text": "789012 sayısını binler basamağına yuvarlayın", "option_a": "789000", "option_b": "790000", "option_c": "791000", "option_d": "792000", "correct_answer": "A"},
        {"grade": 4, "topic": "Yuvarlama", "question_text": "456789 sayısını on binler basamağına yuvarlayın", "option_a": "450000", "option_b": "460000", "option_c": "470000", "option_d": "480000", "correct_answer": "B"},
        {"grade": 4, "topic": "Yuvarlama", "question_text": "234567 sayısını yüz binler basamağına yuvarlayın", "option_a": "200000", "option_b": "300000", "option_c": "400000", "option_d": "500000", "correct_answer": "A"},
        {"grade": 4, "topic": "Yuvarlama", "question_text": "567890 sayısını onlar basamağına yuvarlayın", "option_a": "567880", "option_b": "567890", "option_c": "567900", "option_d": "567910", "correct_answer": "C"},
        
        # 2. Dört İşlem - 6 basamaklı toplama
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "123456 + 234567 = ?", "option_a": "357023", "option_b": "358023", "option_c": "359023", "option_d": "360023", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "456789 + 123456 = ?", "option_a": "580245", "option_b": "581245", "option_c": "582245", "option_d": "583245", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "789012 + 210987 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "345678 + 654321 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "567890 + 432109 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        
        # 2. Dört İşlem - 6 basamaklı çıkarma
        {"grade": 4, "topic": "6 Basamaklı Çıkarma", "question_text": "789012 - 123456 = ?", "option_a": "665556", "option_b": "666556", "option_c": "667556", "option_d": "668556", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Çıkarma", "question_text": "456789 - 234567 = ?", "option_a": "222222", "option_b": "223222", "option_c": "224222", "option_d": "225222", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Çıkarma", "question_text": "567890 - 123456 = ?", "option_a": "444434", "option_b": "445434", "option_c": "446434", "option_d": "447434", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Çıkarma", "question_text": "678901 - 234567 = ?", "option_a": "444334", "option_b": "445334", "option_c": "446334", "option_d": "447334", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Çıkarma", "question_text": "789012 - 345678 = ?", "option_a": "443334", "option_b": "444334", "option_c": "445334", "option_d": "446334", "correct_answer": "A"},
        
        # 2. Dört İşlem - 4 basamaklı çarpma
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "2345 x 67 = ?", "option_a": "157115", "option_b": "158115", "option_c": "159115", "option_d": "160115", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "4567 x 89 = ?", "option_a": "406463", "option_b": "407463", "option_c": "408463", "option_d": "409463", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "5678 x 123 = ?", "option_a": "698394", "option_b": "699394", "option_c": "700394", "option_d": "701394", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "6789 x 456 = ?", "option_a": "3095784", "option_b": "3096784", "option_c": "3097784", "option_d": "3098784", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "7890 x 234 = ?", "option_a": "1846260", "option_b": "1847260", "option_c": "1848260", "option_d": "1849260", "correct_answer": "A"},
        
        # 2. Dört İşlem - Bölme işlemi
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "123456 ÷ 12 = ?", "option_a": "10288", "option_b": "10289", "option_c": "10290", "option_d": "10291", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "456789 ÷ 23 = ?", "option_a": "19860", "option_b": "19861", "option_c": "19862", "option_d": "19863", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "567890 ÷ 34 = ?", "option_a": "16702", "option_b": "16703", "option_c": "16704", "option_d": "16705", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "678901 ÷ 45 = ?", "option_a": "15086", "option_b": "15087", "option_c": "15088", "option_d": "15089", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "789012 ÷ 56 = ?", "option_a": "14089", "option_b": "14090", "option_c": "14091", "option_d": "14092", "correct_answer": "A"},
        
        # 2. Dört İşlem - İşlem önceliği
        {"grade": 4, "topic": "İşlem Önceliği", "question_text": "(12 + 8) x 5 = ?", "option_a": "80", "option_b": "100", "option_c": "120", "option_d": "140", "correct_answer": "B"},
        {"grade": 4, "topic": "İşlem Önceliği", "question_text": "(25 - 5) ÷ 4 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "C"},
        {"grade": 4, "topic": "İşlem Önceliği", "question_text": "(16 + 4) x 3 = ?", "option_a": "40", "option_b": "50", "option_c": "60", "option_d": "70", "correct_answer": "C"},
        {"grade": 4, "topic": "İşlem Önceliği", "question_text": "(30 - 6) ÷ 6 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 4, "topic": "İşlem Önceliği", "question_text": "(18 + 2) x 4 = ?", "option_a": "60", "option_b": "70", "option_c": "80", "option_d": "90", "correct_answer": "C"},
        
        # 3. Çarpanlar ve Katlar
        {"grade": 4, "topic": "Çarpanlar ve Katlar", "question_text": "8'in 5 katı kaçtır?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        {"grade": 4, "topic": "Çarpanlar ve Katlar", "question_text": "12'nin 6 katı kaçtır?", "option_a": "60", "option_b": "66", "option_c": "72", "option_d": "78", "correct_answer": "C"},
        {"grade": 4, "topic": "Çarpanlar ve Katlar", "question_text": "15'in 8 katı kaçtır?", "option_a": "100", "option_b": "110", "option_c": "120", "option_d": "130", "correct_answer": "C"},
        {"grade": 4, "topic": "Çarpanlar ve Katlar", "question_text": "20'nin 7 katı kaçtır?", "option_a": "120", "option_b": "130", "option_c": "140", "option_d": "150", "correct_answer": "C"},
        {"grade": 4, "topic": "Çarpanlar ve Katlar", "question_text": "25'in 9 katı kaçtır?", "option_a": "200", "option_b": "210", "option_c": "220", "option_d": "225", "correct_answer": "D"},
        
        # 4. Kesirler - Birim kesir
        {"grade": 4, "topic": "Birim Kesir", "question_text": "1/5 kesri nasıl okunur?", "option_a": "Bir beşinci", "option_b": "Beşte bir", "option_c": "Beş bölü bir", "option_d": "Bir bölü beş", "correct_answer": "B"},
        {"grade": 4, "topic": "Birim Kesir", "question_text": "1/8 kesri nasıl okunur?", "option_a": "Bir sekizinci", "option_b": "Sekizde bir", "option_c": "Sekiz bölü bir", "option_d": "Bir bölü sekiz", "correct_answer": "B"},
        {"grade": 4, "topic": "Birim Kesir", "question_text": "1/10 kesri nasıl okunur?", "option_a": "Bir onuncu", "option_b": "Onda bir", "option_c": "On bölü bir", "option_d": "Bir bölü on", "correct_answer": "B"},
        {"grade": 4, "topic": "Birim Kesir", "question_text": "1/12 kesri nasıl okunur?", "option_a": "Bir on ikinci", "option_b": "On ikide bir", "option_c": "On iki bölü bir", "option_d": "Bir bölü on iki", "correct_answer": "B"},
        {"grade": 4, "topic": "Birim Kesir", "question_text": "1/15 kesri nasıl okunur?", "option_a": "Bir on beşinci", "option_b": "On beşte bir", "option_c": "On beş bölü bir", "option_d": "Bir bölü on beş", "correct_answer": "B"},
        
        # 4. Kesirler - Bileşik kesir
        {"grade": 4, "topic": "Bileşik Kesir", "question_text": "7/4 kesri nasıl okunur?", "option_a": "Yedi dördüncü", "option_b": "Dörtte yedi", "option_c": "Yedi bölü dört", "option_d": "Dört bölü yedi", "correct_answer": "B"},
        {"grade": 4, "topic": "Bileşik Kesir", "question_text": "9/5 kesri nasıl okunur?", "option_a": "Dokuz beşinci", "option_b": "Beşte dokuz", "option_c": "Dokuz bölü beş", "option_d": "Beş bölü dokuz", "correct_answer": "B"},
        {"grade": 4, "topic": "Bileşik Kesir", "question_text": "11/6 kesri nasıl okunur?", "option_a": "On bir altıncı", "option_b": "Altıda on bir", "option_c": "On bir bölü altı", "option_d": "Altı bölü on bir", "correct_answer": "B"},
        {"grade": 4, "topic": "Bileşik Kesir", "question_text": "13/8 kesri nasıl okunur?", "option_a": "On üç sekizinci", "option_b": "Sekizde on üç", "option_c": "On üç bölü sekiz", "option_d": "Sekiz bölü on üç", "correct_answer": "B"},
        {"grade": 4, "topic": "Bileşik Kesir", "question_text": "15/10 kesri nasıl okunur?", "option_a": "On beş onuncu", "option_b": "Onda on beş", "option_c": "On beş bölü on", "option_d": "On bölü on beş", "correct_answer": "B"},
        
        # 4. Kesirler - Kesirleri karşılaştırma
        {"grade": 4, "topic": "Kesirleri Karşılaştırma", "question_text": "3/4 ile 5/6 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma", "question_text": "2/3 ile 4/5 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma", "question_text": "7/8 ile 8/9 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma", "question_text": "1/2 ile 1/2 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma", "question_text": "3/5 ile 4/7 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "B"},
        
        # 5. Ondalık Gösterimler - Basamak değeri
        {"grade": 4, "topic": "Ondalık Basamak Değeri", "question_text": "3.45 sayısında 4 hangi basamaktadır?", "option_a": "Birler", "option_b": "Onda birler", "option_c": "Yüzde birler", "option_d": "Binde birler", "correct_answer": "B"},
        {"grade": 4, "topic": "Ondalık Basamak Değeri", "question_text": "7.89 sayısında 8 hangi basamaktadır?", "option_a": "Birler", "option_b": "Onda birler", "option_c": "Yüzde birler", "option_d": "Binde birler", "correct_answer": "B"},
        {"grade": 4, "topic": "Ondalık Basamak Değeri", "question_text": "12.34 sayısında 3 hangi basamaktadır?", "option_a": "Birler", "option_b": "Onda birler", "option_c": "Yüzde birler", "option_d": "Binde birler", "correct_answer": "B"},
        {"grade": 4, "topic": "Ondalık Basamak Değeri", "question_text": "45.67 sayısında 6 hangi basamaktadır?", "option_a": "Birler", "option_b": "Onda birler", "option_c": "Yüzde birler", "option_d": "Binde birler", "correct_answer": "B"},
        {"grade": 4, "topic": "Ondalık Basamak Değeri", "question_text": "89.12 sayısında 1 hangi basamaktadır?", "option_a": "Birler", "option_b": "Onda birler", "option_c": "Yüzde birler", "option_d": "Binde birler", "correct_answer": "B"},
        
        # 5. Ondalık Gösterimler - Karşılaştırma
        {"grade": 4, "topic": "Ondalık Karşılaştırma", "question_text": "3.45 ile 3.54 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Ondalık Karşılaştırma", "question_text": "7.89 ile 7.98 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Ondalık Karşılaştırma", "question_text": "12.34 ile 12.43 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Ondalık Karşılaştırma", "question_text": "45.67 ile 45.76 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        {"grade": 4, "topic": "Ondalık Karşılaştırma", "question_text": "89.12 ile 89.21 arasında hangi işaret gelir?", "option_a": "<", "option_b": ">", "option_c": "=", "option_d": "+", "correct_answer": "A"},
        
        # 6. Geometri ve Açılar - Açı tanıma
        {"grade": 4, "topic": "Açı Tanıma", "question_text": "45 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "A"},
        {"grade": 4, "topic": "Açı Tanıma", "question_text": "90 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "B"},
        {"grade": 4, "topic": "Açı Tanıma", "question_text": "120 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "C"},
        {"grade": 4, "topic": "Açı Tanıma", "question_text": "180 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "D"},
        {"grade": 4, "topic": "Açı Tanıma", "question_text": "30 derecelik açı nasıl adlandırılır?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "A"},
        
        # 6. Geometri ve Açılar - Çokgenler
        {"grade": 4, "topic": "Çokgenler", "question_text": "Hangi şekil 5 kenarlıdır?", "option_a": "Dörtgen", "option_b": "Beşgen", "option_c": "Altıgen", "option_d": "Yedigen", "correct_answer": "B"},
        {"grade": 4, "topic": "Çokgenler", "question_text": "Hangi şekil 6 kenarlıdır?", "option_a": "Beşgen", "option_b": "Altıgen", "option_c": "Yedigen", "option_d": "Sekizgen", "correct_answer": "B"},
        {"grade": 4, "topic": "Çokgenler", "question_text": "Hangi şekil 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Dörtgen", "option_c": "Beşgen", "option_d": "Altıgen", "correct_answer": "B"},
        {"grade": 4, "topic": "Çokgenler", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Üçgen", "option_b": "Dörtgen", "option_c": "Beşgen", "option_d": "Altıgen", "correct_answer": "A"},
        {"grade": 4, "topic": "Çokgenler", "question_text": "Hangi şekil 7 kenarlıdır?", "option_a": "Altıgen", "option_b": "Yedigen", "option_c": "Sekizgen", "option_d": "Dokuzgen", "correct_answer": "B"},
        
        # 7. Uzunluk Ölçme - Birimler arası dönüşüm
        {"grade": 4, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "1000 mm kaç metredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "100 cm kaç metredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "10 dm kaç metredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "1000 m kaç kilometredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk Birimleri Dönüşüm", "question_text": "5000 m kaç kilometredir?", "option_a": "0.5", "option_b": "5", "option_c": "50", "option_d": "500", "correct_answer": "B"},
        
        # 8. Ağırlık Ölçme - Birimler arası dönüşüm
        {"grade": 4, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "1000 mg kaç gramdır?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "1000 g kaç kilogramdır?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "500 mg kaç gramdır?", "option_a": "0.05", "option_b": "0.5", "option_c": "5", "option_d": "50", "correct_answer": "B"},
        {"grade": 4, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "2000 g kaç kilogramdır?", "option_a": "0.2", "option_b": "2", "option_c": "20", "option_d": "200", "correct_answer": "B"},
        {"grade": 4, "topic": "Ağırlık Birimleri Dönüşüm", "question_text": "1500 g kaç kilogramdır?", "option_a": "0.15", "option_b": "1.5", "option_c": "15", "option_d": "150", "correct_answer": "B"},
        
        # 9. Sıvı Ölçme - Birimler arası dönüşüm
        {"grade": 4, "topic": "Sıvı Birimleri Dönüşüm", "question_text": "1000 mL kaç litredir?", "option_a": "0.1", "option_b": "1", "option_c": "10", "option_d": "100", "correct_answer": "B"},
        {"grade": 4, "topic": "Sıvı Birimleri Dönüşüm", "question_text": "500 mL kaç litredir?", "option_a": "0.05", "option_b": "0.5", "option_c": "5", "option_d": "50", "correct_answer": "B"},
        {"grade": 4, "topic": "Sıvı Birimleri Dönüşüm", "question_text": "2000 mL kaç litredir?", "option_a": "0.2", "option_b": "2", "option_c": "20", "option_d": "200", "correct_answer": "B"},
        {"grade": 4, "topic": "Sıvı Birimleri Dönüşüm", "question_text": "1500 mL kaç litredir?", "option_a": "0.15", "option_b": "1.5", "option_c": "15", "option_d": "150", "correct_answer": "B"},
        {"grade": 4, "topic": "Sıvı Birimleri Dönüşüm", "question_text": "3000 mL kaç litredir?", "option_a": "0.3", "option_b": "3", "option_c": "30", "option_d": "300", "correct_answer": "B"},
        
        # 10. Zaman Ölçme - Takvim
        {"grade": 4, "topic": "Takvim", "question_text": "1 yıl kaç aydır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 4, "topic": "Takvim", "question_text": "1 ay kaç haftadır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 4, "topic": "Takvim", "question_text": "1 hafta kaç gündür?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 4, "topic": "Takvim", "question_text": "1 yıl kaç gündür?", "option_a": "360", "option_b": "365", "option_c": "370", "option_d": "375", "correct_answer": "B"},
        {"grade": 4, "topic": "Takvim", "question_text": "1 ay kaç gündür?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        
        # 10. Zaman Ölçme - Süre hesaplama
        {"grade": 4, "topic": "Süre Hesaplama", "question_text": "1 saat kaç dakikadır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 4, "topic": "Süre Hesaplama", "question_text": "1 dakika kaç saniyedir?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 4, "topic": "Süre Hesaplama", "question_text": "2 saat kaç dakikadır?", "option_a": "60", "option_b": "90", "option_c": "120", "option_d": "150", "correct_answer": "C"},
        {"grade": 4, "topic": "Süre Hesaplama", "question_text": "3 dakika kaç saniyedir?", "option_a": "120", "option_b": "150", "option_c": "180", "option_d": "210", "correct_answer": "C"},
        {"grade": 4, "topic": "Süre Hesaplama", "question_text": "1.5 saat kaç dakikadır?", "option_a": "60", "option_b": "75", "option_c": "90", "option_d": "105", "correct_answer": "C"},
        
        # 11. Paralarımız - TL ve kuruş işlemleri
        {"grade": 4, "topic": "TL ve Kuruş İşlemleri", "question_text": "5 TL 50 kuruş kaç kuruştur?", "option_a": "500", "option_b": "550", "option_c": "600", "option_d": "650", "correct_answer": "B"},
        {"grade": 4, "topic": "TL ve Kuruş İşlemleri", "question_text": "3 TL 75 kuruş kaç kuruştur?", "option_a": "300", "option_b": "350", "option_c": "375", "option_d": "400", "correct_answer": "C"},
        {"grade": 4, "topic": "TL ve Kuruş İşlemleri", "question_text": "8 TL 25 kuruş kaç kuruştur?", "option_a": "800", "option_b": "825", "option_c": "850", "option_d": "875", "correct_answer": "B"},
        {"grade": 4, "topic": "TL ve Kuruş İşlemleri", "question_text": "12 TL 80 kuruş kaç kuruştur?", "option_a": "1200", "option_b": "1250", "option_c": "1280", "option_d": "1300", "correct_answer": "C"},
        {"grade": 4, "topic": "TL ve Kuruş İşlemleri", "question_text": "15 TL 90 kuruş kaç kuruştur?", "option_a": "1500", "option_b": "1550", "option_c": "1590", "option_d": "1600", "correct_answer": "C"},
        
        # 12. Veri Toplama ve Değerlendirme - Verileri sınıflandırma
        {"grade": 4, "topic": "Verileri Sınıflandırma", "question_text": "5 öğrenci elma, 3 öğrenci armut, 2 öğrenci muz, 4 öğrenci portakal, 6 öğrenci çilek seviyor. Kaç öğrenci vardır?", "option_a": "18", "option_b": "19", "option_c": "20", "option_d": "21", "correct_answer": "C"},
        {"grade": 4, "topic": "Verileri Sınıflandırma", "question_text": "4 çocuk kırmızı, 6 çocuk mavi, 3 çocuk yeşil, 5 çocuk sarı, 7 çocuk turuncu renk seviyor. Kaç çocuk vardır?", "option_a": "22", "option_b": "23", "option_c": "24", "option_d": "25", "correct_answer": "D"},
        {"grade": 4, "topic": "Verileri Sınıflandırma", "question_text": "3 kedi, 2 köpek, 1 kuş, 4 balık, 2 tavşan, 5 hamster var. Kaç hayvan vardır?", "option_a": "15", "option_b": "16", "option_c": "17", "option_d": "18", "correct_answer": "C"},
        {"grade": 4, "topic": "Verileri Sınıflandırma", "question_text": "2 büyük kutu, 5 küçük kutu, 3 orta kutu, 4 yuvarlak kutu, 6 kare kutu var. Kaç kutu vardır?", "option_a": "18", "option_b": "19", "option_c": "20", "option_d": "21", "correct_answer": "C"},
        {"grade": 4, "topic": "Verileri Sınıflandırma", "question_text": "7 kırmızı top, 3 mavi top, 2 yeşil top, 6 sarı top, 4 turuncu top var. Kaç top vardır?", "option_a": "20", "option_b": "21", "option_c": "22", "option_d": "23", "correct_answer": "C"}
    ]
    
    try:
        # Veritabanına bağlan
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Mevcut 4. sınıf sorularını sil
            cursor.execute("DELETE FROM questions WHERE grade = 4")
            print("Mevcut 4. sınıf soruları silindi.")
            
            # Yeni soruları ekle
            for question in grade4_questions:
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
            print(f"Toplam {len(grade4_questions)} soru başarıyla eklendi!")
            print("4. Sınıf: Yeni müfredata göre sorular hazırlandı")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

if __name__ == "__main__":
    insert_grade4_questions() 