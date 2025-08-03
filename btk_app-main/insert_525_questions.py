#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
525 Questions Insertion Script
525 adet kapsamlı matematik sorusu ekler
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def insert_525_questions():
    """525 adet kapsamlı matematik sorusu ekler"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # 1. Sınıf soruları (150 soru)
            grade1_questions = []
            
            # Toplama (50 soru)
            for i in range(1, 51):
                a = i
                b = i + 1
                result = a + b
                options = [result-2, result-1, result, result+1]
                correct_idx = 2
                grade1_questions.append((1, 'Toplama', f'{a} + {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çıkarma (50 soru)
            for i in range(5, 55):
                a = i + 5
                b = i
                result = a - b
                options = [result-2, result-1, result, result+1]
                correct_idx = 2
                grade1_questions.append((1, 'Çıkarma', f'{a} - {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çarpma (50 soru)
            for i in range(1, 51):
                a = (i % 9) + 1
                b = (i % 8) + 2
                result = a * b
                options = [result-2, result-1, result, result+1]
                correct_idx = 2
                grade1_questions.append((1, 'Çarpma', f'{a} x {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # 2. Sınıf soruları (150 soru)
            grade2_questions = []
            
            # Toplama (50 soru)
            for i in range(10, 60):
                a = i * 5
                b = i * 3
                result = a + b
                options = [result-10, result-5, result, result+5]
                correct_idx = 2
                grade2_questions.append((2, 'Toplama', f'{a} + {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çıkarma (50 soru)
            for i in range(15, 65):
                a = i * 4
                b = i * 2
                result = a - b
                options = [result-10, result-5, result, result+5]
                correct_idx = 2
                grade2_questions.append((2, 'Çıkarma', f'{a} - {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çarpma (50 soru)
            for i in range(2, 52):
                a = (i % 8) + 3
                b = (i % 7) + 4
                result = a * b
                options = [result-5, result-2, result, result+2]
                correct_idx = 2
                grade2_questions.append((2, 'Çarpma', f'{a} x {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # 3. Sınıf soruları (150 soru)
            grade3_questions = []
            
            # Toplama (50 soru)
            for i in range(20, 70):
                a = i * 10
                b = i * 5
                result = a + b
                options = [result-20, result-10, result, result+10]
                correct_idx = 2
                grade3_questions.append((3, 'Toplama', f'{a} + {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çıkarma (50 soru)
            for i in range(25, 75):
                a = i * 8
                b = i * 3
                result = a - b
                options = [result-20, result-10, result, result+10]
                correct_idx = 2
                grade3_questions.append((3, 'Çıkarma', f'{a} - {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çarpma (50 soru)
            for i in range(3, 53):
                a = (i % 9) + 4
                b = (i % 8) + 5
                result = a * b
                options = [result-8, result-4, result, result+4]
                correct_idx = 2
                grade3_questions.append((3, 'Çarpma', f'{a} x {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # 4. Sınıf soruları (75 soru)
            grade4_questions = []
            
            # Toplama (25 soru)
            for i in range(30, 55):
                a = i * 15
                b = i * 8
                result = a + b
                options = [result-30, result-15, result, result+15]
                correct_idx = 2
                grade4_questions.append((4, 'Toplama', f'{a} + {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çıkarma (25 soru)
            for i in range(35, 60):
                a = i * 12
                b = i * 5
                result = a - b
                options = [result-30, result-15, result, result+15]
                correct_idx = 2
                grade4_questions.append((4, 'Çıkarma', f'{a} - {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            # Çarpma (25 soru)
            for i in range(4, 29):
                a = (i % 10) + 6
                b = (i % 9) + 7
                result = a * b
                options = [result-10, result-5, result, result+5]
                correct_idx = 2
                grade4_questions.append((4, 'Çarpma', f'{a} x {b} = ?', str(options[0]), str(options[1]), str(options[2]), str(options[3]), 'C'))
            
            all_questions = grade1_questions + grade2_questions + grade3_questions + grade4_questions
            
            for question in all_questions:
                cursor.execute("""
                    INSERT INTO questions (grade, topic, question_text, option_a, option_b, option_c, option_d, correct_answer)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, question)
            
            connection.commit()
            cursor.close()
            connection.close()
            
            print(f"✅ {len(all_questions)} adet soru başarıyla eklendi!")
            print(f"📊 Sınıf bazında dağılım:")
            print(f"   1. Sınıf: {len(grade1_questions)} soru")
            print(f"   2. Sınıf: {len(grade2_questions)} soru")
            print(f"   3. Sınıf: {len(grade3_questions)} soru")
            print(f"   4. Sınıf: {len(grade4_questions)} soru")
            print(f"   Toplam: {len(all_questions)} soru")
            
    except Error as e:
        print(f"❌ Soru ekleme hatası: {e}")

if __name__ == "__main__":
    print("🚀 525 soru ekleniyor...")
    insert_525_questions()
    print("✅ Soru ekleme tamamlandı!") 