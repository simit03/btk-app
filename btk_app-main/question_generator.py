#!/usr/bin/env python3
"""
MatchCatAI - Soru Oluşturucu
Tüm sınıflar için matematik soruları oluşturan merkezi dosya
"""

import mysql.connector
from config import DB_CONFIG

def insert_grade1_questions():
    """1. sınıf için matematik sorularını ekler"""
    grade1_questions = [
        # Sayı Sayma
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "5'ten sonra hangi sayı gelir?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "8'den önce hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "3'ten sonra hangi sayı gelir?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "10'dan önce hangi sayı gelir?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Sayma", "question_text": "7'den sonra hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        
        # Toplama İşlemi - Toplama işleminin anlamı
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "3 elma + 2 elma = kaç elma eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "2 kalem + 3 kalem = kaç kalem eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "1 top + 4 top = kaç top eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "5 çiçek + 2 çiçek = kaç çiçek eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama İşleminin Anlamı", "question_text": "3 kuş + 2 kuş = kaç kuş eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        
        # Toplama İşlemi - Nesnelerle toplama
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "4 kırmızı top + 3 mavi top = kaç top eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "2 büyük kutu + 3 küçük kutu = kaç kutu eder?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "5 uzun çubuk + 2 kısa çubuk = kaç çubuk eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "3 yuvarlak nesne + 4 köşeli nesne = kaç nesne eder?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Nesnelerle Toplama", "question_text": "1 ağır kutu + 5 hafif kutu = kaç kutu eder?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        
        # Toplama İşlemi - Toplama işlemi yapma (20'ye kadar)
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "8 + 7 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "9 + 6 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "7 + 8 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "6 + 9 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi (20'ye kadar)", "question_text": "5 + 10 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # Çıkarma İşlemi - Çıkarma işleminin anlamı
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "5 elma - 2 elma = kaç elma kalır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "7 kalem - 3 kalem = kaç kalem kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "8 top - 4 top = kaç top kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "6 çiçek - 2 çiçek = kaç çiçek kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Çıkarma İşleminin Anlamı", "question_text": "9 kuş - 5 kuş = kaç kuş kalır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        
        # Çıkarma İşlemi - Çıkarma işlemi yapma (20'ye kadar)
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "15 - 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "16 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "17 - 8 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "18 - 9 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi (20'ye kadar)", "question_text": "19 - 10 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        
        # Geometrik Şekiller
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 1, "topic": "Düzlemsel Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"}
    ]
    
    return grade1_questions

def insert_grade2_questions():
    """2. sınıf için matematik sorularını ekler"""
    grade2_questions = [
        # 3 Basamaklı Sayılar
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "234 sayısı kaç basamaklıdır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "789 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "456 sayısının onlar basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "0", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "123 sayısının birler basamağında hangi rakam vardır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "0", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Sayılar", "question_text": "999 sayısından sonra hangi sayı gelir?", "option_a": "998", "option_b": "999", "option_c": "1000", "option_d": "1001", "correct_answer": "C"},
        
        # 3 Basamaklı Toplama
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "234 + 123 = ?", "option_a": "345", "option_b": "356", "option_c": "357", "option_d": "367", "correct_answer": "C"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "456 + 234 = ?", "option_a": "680", "option_b": "690", "option_c": "700", "option_d": "710", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "567 + 123 = ?", "option_a": "680", "option_b": "690", "option_c": "700", "option_d": "710", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "789 + 111 = ?", "option_a": "890", "option_b": "900", "option_c": "910", "option_d": "920", "correct_answer": "B"},
        {"grade": 2, "topic": "3 Basamaklı Toplama", "question_text": "345 + 255 = ?", "option_a": "590", "option_b": "600", "option_c": "610", "option_d": "620", "correct_answer": "B"},
        
        # Çarpım Tablosu
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "7 x 8 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "6 x 9 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "8 x 7 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "9 x 6 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 2, "topic": "Çarpım Tablosu", "question_text": "5 x 8 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        
        # Eşit Gruplara Ayırma
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "12 elmayı 3 kişiye eşit paylaştırırsak her kişiye kaç elma düşer?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "15 kalemi 5 kişiye eşit paylaştırırsak her kişiye kaç kalem düşer?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "18 bisküviyi 6 kişiye eşit paylaştırırsak her kişiye kaç bisküvi düşer?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "20 çiçeği 4 vazoya eşit koyarsak her vazoda kaç çiçek olur?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 2, "topic": "Eşit Gruplara Ayırma", "question_text": "16 topu 2 gruba eşit paylaştırırsak her grupta kaç top olur?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"}
    ]
    
    return grade2_questions

def insert_grade3_questions():
    """3. sınıf için matematik sorularını ekler"""
    grade3_questions = [
        # 4 Basamaklı Doğal Sayılar
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "2345 sayısı kaç basamaklıdır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "7890 sayısının binler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "4567 sayısının yüzler basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "1234 sayısının onlar basamağında hangi rakam vardır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Doğal Sayılar", "question_text": "9999 sayısından sonra hangi sayı gelir?", "option_a": "9998", "option_b": "9999", "option_c": "10000", "option_d": "10001", "correct_answer": "C"},
        
        # 4 Basamaklı Toplama
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "2345 + 1234 = ?", "option_a": "3456", "option_b": "3567", "option_c": "3579", "option_d": "3679", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "4567 + 2345 = ?", "option_a": "6800", "option_b": "6900", "option_c": "6912", "option_d": "7000", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "5678 + 1234 = ?", "option_a": "6800", "option_b": "6900", "option_c": "6912", "option_d": "7000", "correct_answer": "C"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "7890 + 1110 = ?", "option_a": "8900", "option_b": "9000", "option_c": "9100", "option_d": "9200", "correct_answer": "B"},
        {"grade": 3, "topic": "4 Basamaklı Toplama", "question_text": "3456 + 2554 = ?", "option_a": "5900", "option_b": "6000", "option_c": "6010", "option_d": "6100", "correct_answer": "C"},
        
        # Çarpım Tablosu
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "8 x 9 = ?", "option_a": "70", "option_b": "72", "option_c": "74", "option_d": "76", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "7 x 8 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "9 x 7 = ?", "option_a": "61", "option_b": "63", "option_c": "65", "option_d": "67", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "6 x 9 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpım Tablosu", "question_text": "5 x 8 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        
        # Kalansız Bölme
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "24 ÷ 6 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "35 ÷ 7 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "48 ÷ 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "63 ÷ 9 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 3, "topic": "Kalansız Bölme", "question_text": "42 ÷ 6 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"}
    ]
    
    return grade3_questions

def insert_grade4_questions():
    """4. sınıf için matematik sorularını ekler"""
    grade4_questions = [
        # 6 Basamaklı Sayılar
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "123456 sayısı kaç basamaklıdır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "789012 sayısının yüz binler basamağında hangi rakam vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "0", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "456789 sayısının on binler basamağında hangi rakam vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "234567 sayısının binler basamağında hangi rakam vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 4, "topic": "6 Basamaklı Sayılar", "question_text": "999999 sayısından sonra hangi sayı gelir?", "option_a": "999998", "option_b": "999999", "option_c": "1000000", "option_d": "1000001", "correct_answer": "C"},
        
        # 6 Basamaklı Toplama
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "123456 + 234567 = ?", "option_a": "357023", "option_b": "358023", "option_c": "359023", "option_d": "360023", "correct_answer": "B"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "456789 + 123456 = ?", "option_a": "580245", "option_b": "581245", "option_c": "582245", "option_d": "583245", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "789012 + 210987 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "345678 + 654321 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        {"grade": 4, "topic": "6 Basamaklı Toplama", "question_text": "567890 + 432109 = ?", "option_a": "999999", "option_b": "1000000", "option_c": "1000001", "option_d": "1000002", "correct_answer": "A"},
        
        # 4 Basamaklı Çarpma
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "2345 x 67 = ?", "option_a": "157115", "option_b": "158115", "option_c": "159115", "option_d": "160115", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "4567 x 89 = ?", "option_a": "406463", "option_b": "407463", "option_c": "408463", "option_d": "409463", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "5678 x 123 = ?", "option_a": "698394", "option_b": "699394", "option_c": "700394", "option_d": "701394", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "6789 x 456 = ?", "option_a": "3095784", "option_b": "3096784", "option_c": "3097784", "option_d": "3098784", "correct_answer": "A"},
        {"grade": 4, "topic": "4 Basamaklı Çarpma", "question_text": "7890 x 234 = ?", "option_a": "1846260", "option_b": "1847260", "option_c": "1848260", "option_d": "1849260", "correct_answer": "A"},
        
        # Bölme İşlemi
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "123456 ÷ 12 = ?", "option_a": "10288", "option_b": "10289", "option_c": "10290", "option_d": "10291", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "456789 ÷ 23 = ?", "option_a": "19860", "option_b": "19861", "option_c": "19862", "option_d": "19863", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "567890 ÷ 34 = ?", "option_a": "16702", "option_b": "16703", "option_c": "16704", "option_d": "16705", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "678901 ÷ 45 = ?", "option_a": "15086", "option_b": "15087", "option_c": "15088", "option_d": "15089", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "789012 ÷ 56 = ?", "option_a": "14089", "option_b": "14090", "option_c": "14091", "option_d": "14092", "correct_answer": "A"}
    ]
    
    return grade4_questions

def save_questions_to_database(questions, grade):
    """Soruları veritabanına kaydeder"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Mevcut soruları sil
            cursor.execute("DELETE FROM questions WHERE grade = %s", (grade,))
            print(f"Mevcut {grade}. sınıf soruları silindi.")
            
            # Yeni soruları ekle
            for question in questions:
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
            print(f"Toplam {len(questions)} soru başarıyla eklendi!")
            print(f"{grade}. Sınıf: Sorular hazırlandı")
            
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as e:
        print(f"Veritabanı hatası: {e}")
    except Exception as e:
        print(f"Genel hata: {e}")

def main():
    """Ana fonksiyon - tüm sınıflar için soruları oluşturur"""
    print("🐱 MatchCatAI - Soru Oluşturucu")
    print("=" * 50)
    
    # 1. Sınıf soruları
    print("\n📚 1. Sınıf soruları oluşturuluyor...")
    grade1_questions = insert_grade1_questions()
    save_questions_to_database(grade1_questions, 1)
    
    # 2. Sınıf soruları
    print("\n📚 2. Sınıf soruları oluşturuluyor...")
    grade2_questions = insert_grade2_questions()
    save_questions_to_database(grade2_questions, 2)
    
    # 3. Sınıf soruları
    print("\n📚 3. Sınıf soruları oluşturuluyor...")
    grade3_questions = insert_grade3_questions()
    save_questions_to_database(grade3_questions, 3)
    
    # 4. Sınıf soruları
    print("\n📚 4. Sınıf soruları oluşturuluyor...")
    grade4_questions = insert_grade4_questions()
    save_questions_to_database(grade4_questions, 4)
    
    print("\n✅ Tüm sorular başarıyla oluşturuldu!")
    print("🎯 Toplam soru sayısı:", len(grade1_questions) + len(grade2_questions) + len(grade3_questions) + len(grade4_questions))

if __name__ == "__main__":
    main() 