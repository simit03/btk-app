#!/usr/bin/env python3
"""
Reset Achievements Script
Tüm başarıları temizler ve yeni sistemi başlatır
"""

from app.database.db_connection import DatabaseConnection

def reset_achievements():
    """Tüm başarıları temizle"""
    try:
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor()
            
            # Tüm başarıları sil
            cursor.execute("DELETE FROM achievements")
            
            # Veritabanını kaydet
            db.connection.commit()
            cursor.close()
            
            print("✅ Tüm başarılar başarıyla temizlendi!")
            print("🔄 Yeni başarı sistemi hazır!")
            
        else:
            print("❌ Veritabanı bağlantısı kurulamadı!")
            
    except Exception as e:
        print(f"❌ Hata: {e}")

if __name__ == "__main__":
    print("🔄 Başarı sistemi sıfırlanıyor...")
    reset_achievements() 