#!/usr/bin/env python3
"""
MatchCatAI - Veritabanı Yedekleme ve Geri Yükleme Sistemi
Veritabanındaki tüm verileri yedekler ve main.py başladığında otomatik olarak yükler
"""

import mysql.connector
import json
import os
import sys
from datetime import datetime
from config import DB_CONFIG

class DatabaseBackupRestore:
    def __init__(self):
        self.backup_file = "database_backup.json"
        self.backup_dir = "backups"
        
        # Backup dizinini oluştur
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def get_connection(self):
        """Veritabanı bağlantısı oluşturur"""
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection
        except mysql.connector.Error as e:
            print(f"Veritabanı bağlantı hatası: {e}")
            return None
    
    def backup_all_data(self):
        """Veritabanındaki tüm verileri yedekler"""
        print("🐱 MatchCatAI - Veritabanı Yedekleme Sistemi")
        print("=" * 50)
        
        connection = self.get_connection()
        if not connection:
            return False
        
        try:
            cursor = connection.cursor(dictionary=True)
            backup_data = {
                "backup_date": datetime.now().isoformat(),
                "tables": {}
            }
            
            # Tüm tabloları listele
            cursor.execute("SHOW TABLES")
            tables = [table[list(table.keys())[0]] for table in cursor.fetchall()]
            
            print(f"📊 {len(tables)} tablo bulundu: {', '.join(tables)}")
            
            for table in tables:
                print(f"📋 {table} tablosu yedekleniyor...")
                
                # Tablo verilerini çek
                cursor.execute(f"SELECT * FROM {table}")
                table_data = cursor.fetchall()
                
                # JSON'a çevrilebilir hale getir
                for row in table_data:
                    for key, value in row.items():
                        if isinstance(value, datetime):
                            row[key] = value.isoformat()
                        elif isinstance(value, bytes):
                            row[key] = value.decode('utf-8')
                        elif hasattr(value, '__float__'):  # Decimal ve diğer sayısal tipler
                            row[key] = float(value)
                        elif value is None:
                            row[key] = None
                
                backup_data["tables"][table] = table_data
                print(f"✅ {table}: {len(table_data)} kayıt yedeklendi")
            
            # Yedek dosyasını kaydet
            backup_path = os.path.join(self.backup_dir, self.backup_file)
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Yedekleme tamamlandı!")
            print(f"📁 Yedek dosyası: {backup_path}")
            print(f"📊 Toplam kayıt sayısı: {sum(len(data) for data in backup_data['tables'].values())}")
            
            return True
            
        except mysql.connector.Error as e:
            print(f"❌ Yedekleme hatası: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def restore_all_data(self):
        """Yedeklenen verileri geri yükler"""
        print("🔄 MatchCatAI - Veritabanı Geri Yükleme Sistemi")
        print("=" * 50)
        
        backup_path = os.path.join(self.backup_dir, self.backup_file)
        
        if not os.path.exists(backup_path):
            print(f"❌ Yedek dosyası bulunamadı: {backup_path}")
            return False
        
        try:
            # Yedek dosyasını oku
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            print(f"📅 Yedek tarihi: {backup_data.get('backup_date', 'Bilinmiyor')}")
            print(f"📊 Tablo sayısı: {len(backup_data['tables'])}")
            
            connection = self.get_connection()
            if not connection:
                return False
            
            cursor = connection.cursor()
            
            for table_name, table_data in backup_data['tables'].items():
                if not table_data:
                    print(f"⚠️ {table_name}: Veri yok, atlanıyor")
                    continue
                
                print(f"📋 {table_name} tablosu geri yükleniyor...")
                
                # Mevcut verileri temizle
                cursor.execute(f"DELETE FROM {table_name}")
                print(f"🗑️ {table_name}: Mevcut veriler temizlendi")
                
                if table_data:
                    # Sütun isimlerini al
                    columns = list(table_data[0].keys())
                    placeholders = ', '.join(['%s'] * len(columns))
                    column_names = ', '.join(columns)
                    
                    # Verileri ekle
                    values = []
                    for row in table_data:
                        row_values = []
                        for col in columns:
                            value = row[col]
                            if value == 'None':
                                value = None
                            row_values.append(value)
                        values.append(tuple(row_values))
                    
                    insert_query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
                    cursor.executemany(insert_query, values)
                    
                    print(f"✅ {table_name}: {len(table_data)} kayıt geri yüklendi")
            
            connection.commit()
            print(f"\n✅ Geri yükleme tamamlandı!")
            print(f"📊 Toplam kayıt sayısı: {sum(len(data) for data in backup_data['tables'].values())}")
            
            return True
            
        except mysql.connector.Error as e:
            print(f"❌ Geri yükleme hatası: {e}")
            return False
        except Exception as e:
            print(f"❌ Dosya okuma hatası: {e}")
            return False
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
    
    def check_backup_exists(self):
        """Yedek dosyasının varlığını kontrol eder"""
        backup_path = os.path.join(self.backup_dir, self.backup_file)
        return os.path.exists(backup_path)
    
    def get_backup_info(self):
        """Yedek dosyası hakkında bilgi verir"""
        backup_path = os.path.join(self.backup_dir, self.backup_file)
        
        if not os.path.exists(backup_path):
            return None
        
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            return {
                "backup_date": backup_data.get('backup_date', 'Bilinmiyor'),
                "tables": list(backup_data['tables'].keys()),
                "total_records": sum(len(data) for data in backup_data['tables'].values()),
                "file_size": os.path.getsize(backup_path)
            }
        except Exception as e:
            print(f"❌ Yedek bilgisi okuma hatası: {e}")
            return None

def backup_database():
    """Veritabanını yedekler"""
    backup_system = DatabaseBackupRestore()
    return backup_system.backup_all_data()

def restore_database():
    """Veritabanını geri yükler"""
    backup_system = DatabaseBackupRestore()
    return backup_system.restore_all_data()

def auto_restore_on_startup():
    """Uygulama başladığında otomatik geri yükleme yapar"""
    backup_system = DatabaseBackupRestore()
    
    if backup_system.check_backup_exists():
        print("🔄 Veritabanı yedeği bulundu, otomatik geri yükleme başlatılıyor...")
        return backup_system.restore_all_data()
    else:
        print("⚠️ Veritabanı yedeği bulunamadı, geri yükleme atlanıyor.")
        return False

def show_backup_info():
    """Yedek dosyası hakkında bilgi gösterir"""
    backup_system = DatabaseBackupRestore()
    info = backup_system.get_backup_info()
    
    if info:
        print("📊 Yedek Dosyası Bilgileri:")
        print("=" * 30)
        print(f"📅 Yedek Tarihi: {info['backup_date']}")
        print(f"📋 Tablo Sayısı: {len(info['tables'])}")
        print(f"📊 Toplam Kayıt: {info['total_records']}")
        print(f"💾 Dosya Boyutu: {info['file_size']} bytes")
        print(f"📁 Tablolar: {', '.join(info['tables'])}")
    else:
        print("❌ Yedek dosyası bulunamadı veya okunamadı.")

def main():
    """Ana fonksiyon"""
    print("🐱 MatchCatAI - Veritabanı Yönetim Sistemi")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "backup":
            backup_database()
        elif command == "restore":
            restore_database()
        elif command == "info":
            show_backup_info()
        elif command == "auto":
            auto_restore_on_startup()
        else:
            print("❌ Geçersiz komut!")
            print("Kullanım:")
            print("  python data_backup_restore.py backup  - Veritabanını yedekle")
            print("  python data_backup_restore.py restore - Veritabanını geri yükle")
            print("  python data_backup_restore.py info    - Yedek bilgilerini göster")
            print("  python data_backup_restore.py auto    - Otomatik geri yükleme")
    else:
        print("📋 Kullanılabilir Komutlar:")
        print("  backup  - Veritabanını yedekle")
        print("  restore - Veritabanını geri yükle")
        print("  info    - Yedek bilgilerini göster")
        print("  auto    - Otomatik geri yükleme")

if __name__ == "__main__":
    main() 