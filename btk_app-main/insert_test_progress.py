#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Progress Data Insertion Script
Test kullanıcıları ve ilerleme verileri ekler
"""

import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import random
from config import DB_CONFIG

def insert_test_users():
    """Test kullanıcıları ekler"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Test kullanıcıları
            test_users = [
                ('test_user1', 'password123', 'Ahmet', 'Yılmaz', 3),
                ('test_user2', 'password123', 'Ayşe', 'Demir', 4),
                ('test_user3', 'password123', 'Mehmet', 'Kaya', 2),
                ('test_user4', 'password123', 'Fatma', 'Özkan', 1)
            ]
            
            for user in test_users:
                cursor.execute("""
                    INSERT IGNORE INTO users (username, password, first_name, last_name, grade, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
                """, user)
            
            connection.commit()
            print("✅ Test kullanıcıları eklendi")
            
    except Error as e:
        print(f"❌ Test kullanıcıları ekleme hatası: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_test_progress():
    """Test ilerleme verileri ekler"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Kullanıcıları al
            cursor.execute("SELECT id, grade FROM users WHERE username LIKE 'test_user%'")
            users = cursor.fetchall()
            
            if not users:
                print("❌ Test kullanıcıları bulunamadı!")
                return
            
            # Soruları al
            cursor.execute("SELECT id, topic FROM questions")
            questions = cursor.fetchall()
            
            if not questions:
                print("❌ Sorular bulunamadı!")
                return
            
            # Son 30 gün için test verileri oluştur
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            
            progress_data = []
            
            for user_id, grade in users:
                # Her kullanıcı için son 30 günde rastgele aktivite
                current_date = start_date
                
                while current_date <= end_date:
                    # Her gün için 0-10 arası soru çözme ihtimali
                    daily_questions = random.randint(0, 10)
                    
                    if daily_questions > 0:
                        # O gün için rastgele sorular seç
                        daily_questions_list = random.sample(questions, min(daily_questions, len(questions)))
                        
                        for question_id, topic in daily_questions_list:
                            # Rastgele doğru/yanlış cevap (70% doğru oranı)
                            is_correct = random.random() < 0.7
                            user_answer = random.choice(['A', 'B', 'C', 'D'])
                            
                            # Rastgele saat (9:00-22:00 arası)
                            hour = random.randint(9, 22)
                            minute = random.randint(0, 59)
                            answered_time = current_date.replace(hour=hour, minute=minute)
                            
                            progress_data.append((
                                user_id,
                                question_id,
                                user_answer,
                                is_correct,
                                f"quiz_session_{user_id}_{current_date.strftime('%Y%m%d')}",
                                answered_time
                            ))
                    
                    current_date += timedelta(days=1)
            
            # Verileri ekle
            if progress_data:
                cursor.executemany("""
                    INSERT INTO user_progress 
                    (user_id, question_id, user_answer, is_correct, quiz_session_id, answered_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, [(p[0], p[1], p[2], p[3], p[4], p[5]) for p in progress_data])
                
                connection.commit()
                print(f"✅ {len(progress_data)} adet test ilerleme verisi eklendi")
            
    except Error as e:
        print(f"❌ Test ilerleme verisi ekleme hatası: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_test_achievements():
    """Test başarı verileri ekler"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Kullanıcıları al
            cursor.execute("SELECT id FROM users WHERE username LIKE 'test_user%'")
            users = cursor.fetchall()
            
            if not users:
                print("❌ Test kullanıcıları bulunamadı!")
                return
            
            # Test başarıları
            achievements_data = []
            
            for user_id, in users:
                # Her kullanıcı için rastgele başarılar
                achievement_types = ['perfect_score', 'first_quiz', 'streak_5', 'streak_10']
                achievement_names = {
                    'perfect_score': 'Mükemmel Skor',
                    'first_quiz': 'İlk Quiz',
                    'streak_5': '5 Soru Serisi',
                    'streak_10': '10 Soru Serisi'
                }
                
                # Rastgele 1-3 başarı ekle
                num_achievements = random.randint(1, 3)
                selected_achievements = random.sample(achievement_types, num_achievements)
                
                for achievement_type in selected_achievements:
                    earned_date = datetime.now() - timedelta(days=random.randint(1, 30))
                    
                    achievements_data.append((
                        user_id,
                        achievement_type,
                        achievement_names[achievement_type],
                        f"{achievement_names[achievement_type]} başarısı kazanıldı!",
                        earned_date
                    ))
            
            # Verileri ekle
            if achievements_data:
                cursor.executemany("""
                    INSERT INTO achievements 
                    (user_id, achievement_type, achievement_name, achievement_description, earned_at)
                    VALUES (%s, %s, %s, %s, %s)
                """, achievements_data)
                
                connection.commit()
                print(f"✅ {len(achievements_data)} adet test başarı verisi eklendi")
            
    except Error as e:
        print(f"❌ Test başarı verisi ekleme hatası: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    """Ana fonksiyon"""
    print("🚀 Test verileri ekleniyor...")
    
    # Test kullanıcıları ekle
    insert_test_users()
    
    # Test ilerleme verileri ekle
    insert_test_progress()
    
    # Test başarı verileri ekle
    insert_test_achievements()
    
    print("✅ Tüm test verileri başarıyla eklendi!")

if __name__ == "__main__":
    main() 