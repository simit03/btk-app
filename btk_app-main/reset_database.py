#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Database Reset Script
Veritabanını tamamen sıfırlar ve yeniden oluşturur
"""

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def reset_database():
    """Veritabanını tamamen sıfırlar"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Tüm tabloları sil
            tables = [
                'achievements',
                'user_progress', 
                'quiz_sessions',
                'questions',
                'users'
            ]
            
            for table in tables:
                try:
                    cursor.execute(f"DROP TABLE IF EXISTS {table}")
                    print(f"✅ {table} tablosu silindi")
                except Error as e:
                    print(f"❌ {table} tablosu silinirken hata: {e}")
            
            connection.commit()
            cursor.close()
            connection.close()
            
            print("✅ Veritabanı tamamen sıfırlandı!")
            
    except Error as e:
        print(f"❌ Veritabanı sıfırlama hatası: {e}")

if __name__ == "__main__":
    print("🔄 Veritabanı sıfırlanıyor...")
    reset_database()
    print("✅ Veritabanı sıfırlama tamamlandı!") 