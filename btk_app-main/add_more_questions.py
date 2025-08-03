import mysql.connector
from config import DB_CONFIG

def add_more_questions():
    """Tüm sınıflar için 20'şer soru daha ekler"""
    
    # 1. sınıf için ek sorular
    grade1_extra_questions = [
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "5'ten sonra hangi sayı gelir?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "8'den önce hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "3'ten sonra hangi sayı gelir?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "10'dan önce hangi sayı gelir?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "7'den sonra hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "2 + 3 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "4 + 1 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "1 + 5 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "3 + 2 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "0 + 6 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "5 - 2 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "4 - 1 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "6 - 3 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "7 - 4 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "8 - 5 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        
        {"grade": 1, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "D"},
        {"grade": 1, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Çember", "correct_answer": "B"},
        {"grade": 1, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 köşelidir?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Çember", "option_d": "Hiçbiri", "correct_answer": "B"},
        {"grade": 1, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Çember", "option_d": "Dikdörtgen", "correct_answer": "C"},
        {"grade": 1, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Çember", "option_d": "Hiçbiri", "correct_answer": "B"}
    ]
    
    # 2. sınıf için ek sorular
    grade2_extra_questions = [
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "567 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "0", "correct_answer": "A"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "234 sayısının onlar basamağında hangi rakam vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "0", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "789 sayısının birler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "456 sayısından sonra hangi sayı gelir?", "option_a": "455", "option_b": "456", "option_c": "457", "option_d": "458", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "123 sayısından önce hangi sayı gelir?", "option_a": "121", "option_b": "122", "option_c": "123", "option_d": "124", "correct_answer": "B"},
        
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "345 + 123 = ?", "option_a": "456", "option_b": "467", "option_c": "468", "option_d": "469", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "567 + 234 = ?", "option_a": "790", "option_b": "800", "option_c": "801", "option_d": "802", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "789 + 111 = ?", "option_a": "890", "option_b": "900", "option_c": "910", "option_d": "920", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "456 + 344 = ?", "option_a": "790", "option_b": "800", "option_c": "810", "option_d": "820", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "678 + 222 = ?", "option_a": "890", "option_b": "900", "option_c": "910", "option_d": "920", "correct_answer": "B"},
        
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "4 x 7 = ?", "option_a": "26", "option_b": "28", "option_c": "30", "option_d": "32", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "6 x 6 = ?", "option_a": "32", "option_b": "34", "option_c": "36", "option_d": "38", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "8 x 5 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "3 x 9 = ?", "option_a": "24", "option_b": "27", "option_c": "30", "option_d": "33", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "7 x 4 = ?", "option_a": "26", "option_b": "28", "option_c": "30", "option_d": "32", "correct_answer": "B"},
        
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "20 elmayı 4 kişiye eşit paylaştırırsak her kişiye kaç elma düşer?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "24 kalemi 6 kişiye eşit paylaştırırsak her kişiye kaç kalem düşer?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "30 bisküviyi 5 kişiye eşit paylaştırırsak her kişiye kaç bisküvi düşer?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "28 çiçeği 7 vazoya eşit koyarsak her vazoda kaç çiçek olur?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "32 topu 8 gruba eşit paylaştırırsak her grupta kaç top olur?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"}
    ]
    
    # 3. sınıf için ek sorular
    grade3_extra_questions = [
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "5678 sayısının binler basamağında hangi rakam vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "A"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "2345 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "7890 sayısının onlar basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "4567 sayısından sonra hangi sayı gelir?", "option_a": "4566", "option_b": "4567", "option_c": "4568", "option_d": "4569", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "1234 sayısından önce hangi sayı gelir?", "option_a": "1232", "option_b": "1233", "option_c": "1234", "option_d": "1235", "correct_answer": "B"},
        
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "3456 + 1234 = ?", "option_a": "4567", "option_b": "4678", "option_c": "4689", "option_d": "4690", "correct_answer": "D"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "5678 + 2345 = ?", "option_a": "7900", "option_b": "8000", "option_c": "8023", "option_d": "8123", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "7890 + 1110 = ?", "option_a": "8900", "option_b": "9000", "option_c": "9100", "option_d": "9200", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "4567 + 3444 = ?", "option_a": "7900", "option_b": "8000", "option_c": "8011", "option_d": "8111", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "6789 + 2222 = ?", "option_a": "8900", "option_b": "9000", "option_c": "9011", "option_d": "9111", "correct_answer": "C"},
        
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "9 x 8 = ?", "option_a": "70", "option_b": "72", "option_c": "74", "option_d": "76", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "7 x 9 = ?", "option_a": "61", "option_b": "63", "option_c": "65", "option_d": "67", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "8 x 6 = ?", "option_a": "46", "option_b": "48", "option_c": "50", "option_d": "52", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "6 x 8 = ?", "option_a": "46", "option_b": "48", "option_c": "50", "option_d": "52", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "9 x 5 = ?", "option_a": "40", "option_b": "45", "option_c": "50", "option_d": "55", "correct_answer": "B"},
        
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "32 ÷ 8 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "40 ÷ 8 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "48 ÷ 6 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "54 ÷ 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "56 ÷ 7 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"}
    ]
    
    # 4. sınıf için ek sorular
    grade4_extra_questions = [
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "345678 sayısının yüz binler basamağında hangi rakam vardır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "567890 sayısının on binler basamağında hangi rakam vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "234567 sayısının binler basamağında hangi rakam vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "456789 sayısından sonra hangi sayı gelir?", "option_a": "456788", "option_b": "456789", "option_c": "456790", "option_d": "456791", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "123456 sayısından önce hangi sayı gelir?", "option_a": "123454", "option_b": "123455", "option_c": "123456", "option_d": "123457", "correct_answer": "B"},
        
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "234567 + 123456 = ?", "option_a": "357023", "option_b": "358023", "option_c": "359023", "option_d": "360023", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "456789 + 234567 = ?", "option_a": "690356", "option_b": "691356", "option_c": "692356", "option_d": "693356", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "567890 + 123456 = ?", "option_a": "690346", "option_b": "691346", "option_c": "692346", "option_d": "693346", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "678901 + 123456 = ?", "option_a": "800357", "option_b": "801357", "option_c": "802357", "option_d": "803357", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "789012 + 123456 = ?", "option_a": "910468", "option_b": "911468", "option_c": "912468", "option_d": "913468", "correct_answer": "C"},
        
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "3456 x 78 = ?", "option_a": "269568", "option_b": "270568", "option_c": "271568", "option_d": "272568", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "5678 x 89 = ?", "option_a": "505342", "option_b": "506342", "option_c": "507342", "option_d": "508342", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "6789 x 123 = ?", "option_a": "834947", "option_b": "835947", "option_c": "836947", "option_d": "837947", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "7890 x 456 = ?", "option_a": "3597840", "option_b": "3598840", "option_c": "3599840", "option_d": "3600840", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "8901 x 234 = ?", "option_a": "2082834", "option_b": "2083834", "option_c": "2084834", "option_d": "2085834", "correct_answer": "A"},
        
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "234567 ÷ 13 = ?", "option_a": "18043", "option_b": "18044", "option_c": "18045", "option_d": "18046", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "456789 ÷ 24 = ?", "option_a": "19032", "option_b": "19033", "option_c": "19034", "option_d": "19035", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "567890 ÷ 35 = ?", "option_a": "16225", "option_b": "16226", "option_c": "16227", "option_d": "16228", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "678901 ÷ 46 = ?", "option_a": "14758", "option_b": "14759", "option_c": "14760", "option_d": "14761", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "789012 ÷ 57 = ?", "option_a": "13842", "option_b": "13843", "option_c": "13844", "option_d": "13845", "correct_answer": "A"}
    ]
    
    try:
        # Veritabanına bağlan
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Tüm soruları birleştir
            all_questions = grade1_extra_questions + grade2_extra_questions + grade3_extra_questions + grade4_extra_questions
            
            # Yeni soruları ekle
            for question in all_questions:
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
            print(f"Toplam {len(all_questions)} soru başarıyla eklendi!")
            print(f"1. Sınıf: {len(grade1_extra_questions)} soru eklendi")
            print(f"2. Sınıf: {len(grade2_extra_questions)} soru eklendi")
            print(f"3. Sınıf: {len(grade3_extra_questions)} soru eklendi")
            print(f"4. Sınıf: {len(grade4_extra_questions)} soru eklendi")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

if __name__ == "__main__":
    add_more_questions() 