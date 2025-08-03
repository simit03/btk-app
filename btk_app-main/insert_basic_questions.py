#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Basic Questions Insertion Script
Temel matematik soruları ekler
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def insert_basic_questions():
    """Temel matematik soruları ekler"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # 1. Sınıf soruları
            grade1_questions = [
                (1, 'Toplama', '2 + 3 = ?', '4', '5', '6', '7', 'B'),
                (1, 'Toplama', '1 + 4 = ?', '3', '4', '5', '6', 'C'),
                (1, 'Çıkarma', '5 - 2 = ?', '2', '3', '4', '5', 'B'),
                (1, 'Çıkarma', '7 - 3 = ?', '3', '4', '5', '6', 'B'),
                (1, 'Çarpma', '2 x 3 = ?', '4', '5', '6', '7', 'C'),
                (1, 'Çarpma', '3 x 4 = ?', '10', '11', '12', '13', 'C'),
            ]
            
            # 2. Sınıf soruları
            grade2_questions = [
                (2, 'Toplama', '15 + 25 = ?', '35', '40', '45', '50', 'B'),
                (2, 'Toplama', '30 + 20 = ?', '45', '50', '55', '60', 'B'),
                (2, 'Çıkarma', '50 - 15 = ?', '30', '35', '40', '45', 'B'),
                (2, 'Çıkarma', '60 - 25 = ?', '30', '35', '40', '45', 'B'),
                (2, 'Çarpma', '5 x 6 = ?', '25', '30', '35', '40', 'B'),
                (2, 'Çarpma', '4 x 8 = ?', '28', '32', '36', '40', 'B'),
            ]
            
            # 3. Sınıf soruları
            grade3_questions = [
                (3, 'Toplama', '125 + 75 = ?', '190', '200', '210', '220', 'B'),
                (3, 'Toplama', '150 + 100 = ?', '240', '250', '260', '270', 'B'),
                (3, 'Çıkarma', '200 - 75 = ?', '115', '125', '135', '145', 'B'),
                (3, 'Çıkarma', '300 - 125 = ?', '165', '175', '185', '195', 'B'),
                (3, 'Çarpma', '8 x 7 = ?', '54', '56', '58', '60', 'B'),
                (3, 'Çarpma', '9 x 6 = ?', '52', '54', '56', '58', 'B'),
            ]
            
            # 4. Sınıf soruları
            grade4_questions = [
                (4, 'Toplama', '250 + 350 = ?', '580', '590', '600', '610', 'C'),
                (4, 'Toplama', '400 + 300 = ?', '680', '690', '700', '710', 'C'),
                (4, 'Çıkarma', '500 - 150 = ?', '330', '340', '350', '360', 'C'),
                (4, 'Çıkarma', '600 - 200 = ?', '380', '390', '400', '410', 'C'),
                (4, 'Çarpma', '12 x 8 = ?', '92', '94', '96', '98', 'C'),
                (4, 'Çarpma', '15 x 6 = ?', '88', '90', '92', '94', 'B'),
            ]
            
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
            
    except Error as e:
        print(f"❌ Soru ekleme hatası: {e}")

if __name__ == "__main__":
    print("🚀 Temel sorular ekleniyor...")
    insert_basic_questions()
    print("✅ Soru ekleme tamamlandı!") 