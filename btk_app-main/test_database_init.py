#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veritabanı başlatıcı test dosyası
Bu dosya veritabanı tablolarının doğru oluşturulup oluşturulmadığını test eder.
"""

import sys
import os

# Ana dizini path'e ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_database_initialization():
    """Veritabanı başlatıcıyı test eder"""
    try:
        from database_initializer import auto_initialize_database
        
        print("🧪 Veritabanı başlatıcı test ediliyor...")
        
        # Veritabanını başlat
        success = auto_initialize_database()
        
        if success:
            print("✅ Veritabanı başlatma testi başarılı!")
            return True
        else:
            print("❌ Veritabanı başlatma testi başarısız!")
            return False
            
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def check_tables_exist():
    """Oluşturulan tabloları kontrol eder"""
    try:
        from config import DB_CONFIG
        import mysql.connector
        
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        # Tüm tabloları listele
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        print("\n📋 Mevcut tablolar:")
        for table in tables:
            print(f"  - {table[0]}")
        
        expected_tables = [
            'users',
            'questions', 
            'user_progress',
            'quiz_sessions',
            'achievements',
            'user_settings',
            'daily_stats'
        ]
        
        print("\n🔍 Beklenen tablolar kontrol ediliyor...")
        missing_tables = []
        
        for expected_table in expected_tables:
            if any(expected_table in table for table in tables):
                print(f"✅ {expected_table} tablosu mevcut")
            else:
                print(f"❌ {expected_table} tablosu eksik")
                missing_tables.append(expected_table)
        
        if missing_tables:
            print(f"\n⚠️ Eksik tablolar: {', '.join(missing_tables)}")
            return False
        else:
            print("\n✅ Tüm tablolar başarıyla oluşturuldu!")
            return True
            
    except Exception as e:
        print(f"❌ Tablo kontrol hatası: {e}")
        return False
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    print("🚀 Veritabanı başlatıcı test başlatılıyor...\n")
    
    # Test 1: Veritabanı başlatma
    test1_success = test_database_initialization()
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: Tablo kontrolü
    test2_success = check_tables_exist()
    
    print("\n" + "="*50)
    if test1_success and test2_success:
        print("🎉 Tüm testler başarılı! Veritabanı hazır.")
    else:
        print("⚠️ Bazı testler başarısız oldu. Lütfen hataları kontrol edin.")
