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
        # DOĞAL SAYILAR - Sayıları Tanıma ve Yazma (0'dan 20'ye kadar)
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "15 sayısından sonra hangi sayı gelir?", "option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "8 sayısından önce hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "12 sayısı kaç basamaklıdır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "20 sayısından önce hangi sayı gelir?", "option_a": "18", "option_b": "19", "option_c": "20", "option_d": "21", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "0 sayısından sonra hangi sayı gelir?", "option_a": "0", "option_b": "1", "option_c": "2", "option_d": "3", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "19 sayısından sonra hangi sayı gelir?", "option_a": "18", "option_b": "19", "option_c": "20", "option_d": "21", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "10 sayısından önce hangi sayı gelir?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "5 sayısından sonra hangi sayı gelir?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "13 sayısından önce hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "17 sayısından sonra hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - Sayıları Karşılaştırma ve Sıralama
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 15 mi 12 mi?", "option_a": "12", "option_b": "15", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 8 mi 13 mi?", "option_a": "8", "option_b": "13", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 20 mi 18 mi?", "option_a": "18", "option_b": "20", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 5 mi 9 mi?", "option_a": "5", "option_b": "9", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 16 mi 14 mi?", "option_a": "14", "option_b": "16", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 3 mi 7 mi?", "option_a": "3", "option_b": "7", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 19 mi 17 mi?", "option_a": "17", "option_b": "19", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 2 mi 6 mi?", "option_a": "2", "option_b": "6", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 11 mi 9 mi?", "option_a": "9", "option_b": "11", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 1 mi 4 mi?", "option_a": "1", "option_b": "4", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        
        # DOĞAL SAYILAR - Ritmik Saymalar
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 8'den sonra hangi sayı gelir?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "B"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 15'ten sonra hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "20", "correct_answer": "D"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Onar ritmik sayarken 10'dan sonra hangi sayı gelir?", "option_a": "11", "option_b": "15", "option_c": "20", "option_d": "25", "correct_answer": "C"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 6'dan sonra hangi sayı gelir?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "B"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 5'ten sonra hangi sayı gelir?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "10", "correct_answer": "D"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Onar ritmik sayarken 0'dan sonra hangi sayı gelir?", "option_a": "1", "option_b": "5", "option_c": "10", "option_d": "15", "correct_answer": "C"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 4'ten sonra hangi sayı gelir?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 10'dan sonra hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "15", "correct_answer": "D"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Onar ritmik sayarken 20'den sonra hangi sayı gelir?", "option_a": "21", "option_b": "25", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 2'den sonra hangi sayı gelir?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Basamak Değeri
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "15 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "5", "option_d": "15", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "18 sayısında kaç tane birlik vardır?", "option_a": "1", "option_b": "8", "option_c": "10", "option_d": "18", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "12 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "2", "option_d": "12", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "19 sayısında kaç tane birlik vardır?", "option_a": "1", "option_b": "9", "option_c": "10", "option_d": "19", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "13 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "3", "option_d": "13", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "16 sayısında kaç tane birlik vardır?", "option_a": "1", "option_b": "6", "option_c": "10", "option_d": "16", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "14 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "4", "option_d": "14", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "17 sayısında kaç tane birlik vardır?", "option_a": "1", "option_b": "7", "option_c": "10", "option_d": "17", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "11 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "11", "option_d": "12", "correct_answer": "B"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "20 sayısında kaç tane birlik vardır?", "option_a": "0", "option_b": "2", "option_c": "10", "option_d": "20", "correct_answer": "A"},
        
        # DOĞAL SAYILAR - Sayı Örüntüleri
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "2, 4, 6, 8, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "5, 10, 15, 20, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "25", "option_d": "30", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "1, 3, 5, 7, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "10, 20, 30, 40, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "41", "option_b": "45", "option_c": "50", "option_d": "60", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "3, 6, 9, 12, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "0, 5, 10, 15, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "20", "correct_answer": "D"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "4, 8, 12, 16, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "17", "option_b": "18", "option_c": "19", "option_d": "20", "correct_answer": "D"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "2, 5, 8, 11, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "1, 4, 7, 10, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "6, 12, 18, 24, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "25", "option_b": "26", "option_c": "28", "option_d": "30", "correct_answer": "D"},
        
        # İŞLEMLER - Toplama İşlemi (20'ye kadar)
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "8 + 7 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "9 + 6 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "7 + 8 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "6 + 9 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "5 + 10 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "4 + 11 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "3 + 12 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "2 + 13 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "1 + 14 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "0 + 15 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # İŞLEMLER - Çıkarma İşlemi (20'ye kadar)
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "15 - 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "16 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "17 - 8 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "18 - 9 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "19 - 10 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "20 - 11 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "14 - 7 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "13 - 6 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "12 - 5 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "11 - 4 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        
        # İŞLEMLER - Toplama ve Çıkarma Arasındaki İlişki
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "8 + 7 = 15 ise 15 - 8 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "9 + 6 = 15 ise 15 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "7 + 8 = 15 ise 15 - 7 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "6 + 9 = 15 ise 15 - 6 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "5 + 10 = 15 ise 15 - 5 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "4 + 11 = 15 ise 15 - 4 = ?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "3 + 12 = 15 ise 15 - 3 = ?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "2 + 13 = 15 ise 15 - 2 = ?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "1 + 14 = 15 ise 15 - 1 = ?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "0 + 15 = 15 ise 15 - 0 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # GEOMETRİ - Temel Geometrik Şekiller
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 kenarlı ama köşeli değildir?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "B"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlı ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil yuvarlak ve köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 kenarlı ve 4 köşelidir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Kare", "option_d": "Hiçbiri", "correct_answer": "C"},
        
        # ÖLÇME - Uzunluk Ölçme
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: kalem mi silgi mi?", "option_a": "Kalem", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: defter mi kitap mı?", "option_a": "Defter", "option_b": "Kitap", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: silgi mi kalem mi?", "option_a": "Silgi", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: tahta mi sıra mı?", "option_a": "Tahta", "option_b": "Sıra", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: defter mi kitap mı?", "option_a": "Defter", "option_b": "Kitap", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: cetvel mi silgi mi?", "option_a": "Cetvel", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: tahta mi sıra mı?", "option_a": "Tahta", "option_b": "Sıra", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: kalem mi silgi mi?", "option_a": "Kalem", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # ÖLÇME - Zaman Ölçme
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç gün vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir günde kaç saat vardır?", "option_a": "12", "option_b": "18", "option_c": "24", "option_d": "30", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç ay vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir ayda kaç hafta vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir saatte kaç dakika vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir dakikada kaç saniye vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç mevsim vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç saat vardır?", "option_a": "120", "option_b": "144", "option_c": "168", "option_d": "180", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir ayda kaç gün vardır?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç gün vardır?", "option_a": "300", "option_b": "350", "option_c": "365", "option_d": "400", "correct_answer": "C"},
        
        # ÖLÇME - Para Ölçme
        {"grade": 1, "topic": "Para Ölçme", "question_text": "1 TL kaç kuruştur?", "option_a": "50", "option_b": "75", "option_c": "100", "option_d": "150", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "5 TL kaç kuruştur?", "option_a": "250", "option_b": "400", "option_c": "500", "option_d": "600", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "10 TL kaç kuruştur?", "option_a": "500", "option_b": "750", "option_c": "1000", "option_d": "1200", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "50 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "B"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "100 kuruş kaç TL'dir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "25 kuruş kaç TL'dir?", "option_a": "0.10", "option_b": "0.25", "option_c": "0.50", "option_d": "0.75", "correct_answer": "B"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "75 kuruş kaç TL'dir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "B"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "200 kuruş kaç TL'dir?", "option_a": "1.00", "option_b": "1.50", "option_c": "2.00", "option_d": "2.50", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "150 kuruş kaç TL'dir?", "option_a": "0.75", "option_b": "1.00", "option_c": "1.50", "option_d": "2.00", "correct_answer": "C"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "300 kuruş kaç TL'dir?", "option_a": "1.50", "option_b": "2.00", "option_c": "2.50", "option_d": "3.00", "correct_answer": "D"},
        
        # EK SORULAR - 40 adet rastgele dağıtılmış
        # Sayıları Tanıma ve Yazma - 6 soru
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "4 sayısından sonra hangi sayı gelir?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "9 sayısından önce hangi sayı gelir?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "14 sayısından sonra hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "6 sayısından önce hangi sayı gelir?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "11 sayısından sonra hangi sayı gelir?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayıları Tanıma ve Yazma", "question_text": "18 sayısından önce hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "B"},
        
        # Sayıları Karşılaştırma ve Sıralama - 5 soru
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 7 mi 4 mi?", "option_a": "4", "option_b": "7", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 10 mi 6 mi?", "option_a": "6", "option_b": "10", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 13 mi 9 mi?", "option_a": "9", "option_b": "13", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 2 mi 8 mi?", "option_a": "2", "option_b": "8", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 17 mi 12 mi?", "option_a": "12", "option_b": "17", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Ritmik Saymalar - 4 soru
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 10'dan sonra hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "B"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 20'den sonra hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "25", "correct_answer": "D"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "Onar ritmik sayarken 30'dan sonra hangi sayı gelir?", "option_a": "31", "option_b": "35", "option_c": "40", "option_d": "45", "correct_answer": "C"},
        {"grade": 1, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 12'den sonra hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "B"},
        
        # Basamak Değeri - 3 soru
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "20 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "2", "option_d": "20", "correct_answer": "C"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "10 sayısında kaç tane birlik vardır?", "option_a": "0", "option_b": "1", "option_c": "10", "option_d": "11", "correct_answer": "A"},
        {"grade": 1, "topic": "Basamak Değeri", "question_text": "19 sayısında kaç tane onluk vardır?", "option_a": "0", "option_b": "1", "option_c": "9", "option_d": "19", "correct_answer": "B"},
        
        # Sayı Örüntüleri - 4 soru
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "1, 2, 3, 4, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "3, 6, 9, 12, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "5, 10, 15, 20, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "25", "correct_answer": "D"},
        {"grade": 1, "topic": "Sayı Örüntüleri", "question_text": "2, 4, 6, 8, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "B"},
        
        # Toplama İşlemi - 5 soru
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "3 + 4 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "5 + 5 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "7 + 3 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "4 + 6 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 1, "topic": "Toplama İşlemi", "question_text": "2 + 8 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        
        # Çıkarma İşlemi - 4 soru
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "10 - 3 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "12 - 5 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "15 - 7 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 1, "topic": "Çıkarma İşlemi", "question_text": "18 - 9 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        
        # Toplama ve Çıkarma Arasındaki İlişki - 3 soru
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "3 + 4 = 7 ise 7 - 3 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "5 + 3 = 8 ise 8 - 5 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 1, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "6 + 4 = 10 ise 10 - 6 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        
        # Temel Geometrik Şekiller - 3 soru
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 1, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        
        # Uzunluk Ölçme - 2 soru
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: kalem mi silgi mi?", "option_a": "Kalem", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 1, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Zaman Ölçme - 2 soru
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç gün vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 1, "topic": "Zaman Ölçme", "question_text": "Bir günde kaç saat vardır?", "option_a": "12", "option_b": "18", "option_c": "24", "option_d": "30", "correct_answer": "C"},
        
        # Para Ölçme - 2 soru
        {"grade": 1, "topic": "Para Ölçme", "question_text": "3 TL + 2 TL = ?", "option_a": "4 TL", "option_b": "5 TL", "option_c": "6 TL", "option_d": "7 TL", "correct_answer": "B"},
        {"grade": 1, "topic": "Para Ölçme", "question_text": "8 TL - 3 TL = ?", "option_a": "3 TL", "option_b": "4 TL", "option_c": "5 TL", "option_d": "6 TL", "correct_answer": "C"}
    ]
    
    return grade1_questions

def insert_grade2_questions():
    """2. sınıf için matematik sorularını ekler"""
    grade2_questions = [
        # DOĞAL SAYILAR - 100 İçinde Sayılar
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "67 sayısından sonra hangi sayı gelir?", "option_a": "66", "option_b": "67", "option_c": "68", "option_d": "69", "correct_answer": "C"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "89 sayısından önce hangi sayı gelir?", "option_a": "87", "option_b": "88", "option_c": "89", "option_d": "90", "correct_answer": "B"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "45 sayısı kaç basamaklıdır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "99 sayısından sonra hangi sayı gelir?", "option_a": "98", "option_b": "99", "option_c": "100", "option_d": "101", "correct_answer": "C"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "23 sayısından önce hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "24", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Basamak Değeri
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "67 sayısında kaç tane onluk vardır?", "option_a": "6", "option_b": "7", "option_c": "60", "option_d": "70", "correct_answer": "A"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "89 sayısında kaç tane birlik vardır?", "option_a": "8", "option_b": "9", "option_c": "80", "option_d": "90", "correct_answer": "B"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "45 sayısında kaç tane onluk vardır?", "option_a": "4", "option_b": "5", "option_c": "40", "option_d": "50", "correct_answer": "A"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "78 sayısında kaç tane birlik vardır?", "option_a": "7", "option_b": "8", "option_c": "70", "option_d": "80", "correct_answer": "B"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "56 sayısında kaç tane onluk vardır?", "option_a": "5", "option_b": "6", "option_c": "50", "option_d": "60", "correct_answer": "A"},
        
        # DOĞAL SAYILAR - Ritmik Saymalar
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 24'ten sonra hangi sayı gelir?", "option_a": "25", "option_b": "26", "option_c": "27", "option_d": "28", "correct_answer": "B"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Üçer ritmik sayarken 15'ten sonra hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "C"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 35'ten sonra hangi sayı gelir?", "option_a": "36", "option_b": "37", "option_c": "38", "option_d": "40", "correct_answer": "D"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Onar ritmik sayarken 50'den sonra hangi sayı gelir?", "option_a": "51", "option_b": "55", "option_c": "60", "option_d": "65", "correct_answer": "C"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Dörder ritmik sayarken 20'den sonra hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "24", "correct_answer": "D"},
        
        # DOĞAL SAYILAR - Sayı Örüntüleri
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "2, 6, 10, 14, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "15", "option_b": "16", "option_c": "17", "option_d": "18", "correct_answer": "D"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "5, 10, 15, 20, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "25", "correct_answer": "D"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "1, 3, 5, 7, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "10, 20, 30, 40, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "41", "option_b": "45", "option_c": "50", "option_d": "55", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "3, 6, 9, 12, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "0, 5, 10, 15, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "20", "correct_answer": "D"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "4, 8, 12, 16, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "17", "option_b": "18", "option_c": "19", "option_d": "20", "correct_answer": "D"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "2, 5, 8, 11, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "1, 4, 7, 10, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "6, 12, 18, 24, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "25", "option_b": "26", "option_c": "28", "option_d": "30", "correct_answer": "D"},
        
        # İŞLEMLER - Toplama İşlemi (20'ye kadar)
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "8 + 7 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "9 + 6 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "7 + 8 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "6 + 9 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "5 + 10 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "4 + 11 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "3 + 12 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "2 + 13 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "1 + 14 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "0 + 15 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # İŞLEMLER - Çıkarma İşlemi (20'ye kadar)
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "15 - 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "16 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "17 - 8 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "18 - 9 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "19 - 10 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "20 - 11 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "14 - 7 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "13 - 6 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "12 - 5 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "11 - 4 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        
        # İŞLEMLER - Toplama ve Çıkarma Arasındaki İlişki
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "8 + 7 = 15 ise 15 - 8 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "9 + 6 = 15 ise 15 - 9 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "7 + 8 = 15 ise 15 - 7 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "6 + 9 = 15 ise 15 - 6 = ?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "5 + 10 = 15 ise 15 - 5 = ?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "4 + 11 = 15 ise 15 - 4 = ?", "option_a": "9", "option_b": "10", "option_c": "11", "option_d": "12", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "3 + 12 = 15 ise 15 - 3 = ?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "2 + 13 = 15 ise 15 - 2 = ?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "1 + 14 = 15 ise 15 - 1 = ?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama ve Çıkarma Arasındaki İlişki", "question_text": "0 + 15 = 15 ise 15 - 0 = ?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        
        # GEOMETRİ - Temel Geometrik Şekiller
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 kenarlı ama köşeli değildir?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 3 kenarlıdır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "B"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlı ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil yuvarlak ve köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 2, "topic": "Temel Geometrik Şekiller", "question_text": "Hangi şekil 4 kenarlı ve 4 köşelidir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Kare", "option_d": "Hiçbiri", "correct_answer": "C"},
        
        # ÖLÇME - Uzunluk Ölçme
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: kalem mi silgi mi?", "option_a": "Kalem", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: defter mi kitap mı?", "option_a": "Defter", "option_b": "Kitap", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: silgi mi kalem mi?", "option_a": "Silgi", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: tahta mi sıra mı?", "option_a": "Tahta", "option_b": "Sıra", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: defter mi kitap mı?", "option_a": "Defter", "option_b": "Kitap", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: cetvel mi silgi mi?", "option_a": "Cetvel", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: tahta mi sıra mı?", "option_a": "Tahta", "option_b": "Sıra", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: kalem mi silgi mi?", "option_a": "Kalem", "option_b": "Silgi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # ÖLÇME - Zaman Ölçme
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç gün vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir günde kaç saat vardır?", "option_a": "12", "option_b": "18", "option_c": "24", "option_d": "30", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç ay vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir ayda kaç hafta vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir saatte kaç dakika vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir dakikada kaç saniye vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç mevsim vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç saat vardır?", "option_a": "120", "option_b": "144", "option_c": "168", "option_d": "180", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir ayda kaç gün vardır?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "35", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç gün vardır?", "option_a": "300", "option_b": "350", "option_c": "365", "option_d": "400", "correct_answer": "C"},
        
        # ÖLÇME - Para Ölçme
        {"grade": 2, "topic": "Para Ölçme", "question_text": "1 TL kaç kuruştur?", "option_a": "50", "option_b": "75", "option_c": "100", "option_d": "150", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "5 TL kaç kuruştur?", "option_a": "250", "option_b": "400", "option_c": "500", "option_d": "600", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "10 TL kaç kuruştur?", "option_a": "500", "option_b": "750", "option_c": "1000", "option_d": "1200", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "50 kuruş kaç TL'dir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "B"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "100 kuruş kaç TL'dir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "25 kuruş kaç TL'dir?", "option_a": "0.10", "option_b": "0.25", "option_c": "0.50", "option_d": "0.75", "correct_answer": "B"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "75 kuruş kaç TL'dir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "B"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "200 kuruş kaç TL'dir?", "option_a": "1.00", "option_b": "1.50", "option_c": "2.00", "option_d": "2.50", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "150 kuruş kaç TL'dir?", "option_a": "0.75", "option_b": "1.00", "option_c": "1.50", "option_d": "2.00", "correct_answer": "C"},
        {"grade": 2, "topic": "Para Ölçme", "question_text": "300 kuruş kaç TL'dir?", "option_a": "1.50", "option_b": "2.00", "option_c": "2.50", "option_d": "3.00", "correct_answer": "D"},
        
        # EK SORULAR - 40 adet rastgele dağıtılmış
        # 100 İçinde Sayılar - 4 soru
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "34 sayısından sonra hangi sayı gelir?", "option_a": "33", "option_b": "34", "option_c": "35", "option_d": "36", "correct_answer": "C"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "78 sayısından önce hangi sayı gelir?", "option_a": "76", "option_b": "77", "option_c": "78", "option_d": "79", "correct_answer": "B"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "56 sayısından sonra hangi sayı gelir?", "option_a": "55", "option_b": "56", "option_c": "57", "option_d": "58", "correct_answer": "C"},
        {"grade": 2, "topic": "100 İçinde Sayılar", "question_text": "89 sayısından önce hangi sayı gelir?", "option_a": "87", "option_b": "88", "option_c": "89", "option_d": "90", "correct_answer": "B"},
        
        # Basamak Değeri - 3 soru
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "34 sayısında kaç tane onluk vardır?", "option_a": "3", "option_b": "4", "option_c": "30", "option_d": "40", "correct_answer": "A"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "67 sayısında kaç tane birlik vardır?", "option_a": "6", "option_b": "7", "option_c": "60", "option_d": "70", "correct_answer": "B"},
        {"grade": 2, "topic": "Basamak Değeri", "question_text": "89 sayısında kaç tane onluk vardır?", "option_a": "8", "option_b": "9", "option_c": "80", "option_d": "90", "correct_answer": "A"},
        
        # Ritmik Saymalar - 3 soru
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "İkişer ritmik sayarken 28'den sonra hangi sayı gelir?", "option_a": "29", "option_b": "30", "option_c": "31", "option_d": "32", "correct_answer": "B"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Üçer ritmik sayarken 18'den sonra hangi sayı gelir?", "option_a": "19", "option_b": "20", "option_c": "21", "option_d": "22", "correct_answer": "C"},
        {"grade": 2, "topic": "Ritmik Saymalar", "question_text": "Beşer ritmik sayarken 25'ten sonra hangi sayı gelir?", "option_a": "26", "option_b": "27", "option_c": "28", "option_d": "30", "correct_answer": "D"},
        
        # Sayı Örüntüleri - 3 soru
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "1, 4, 7, 10, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "2, 5, 8, 11, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 2, "topic": "Sayı Örüntüleri", "question_text": "3, 7, 11, 15, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "D"},
        
        # Sayıları Karşılaştırma ve Sıralama - 3 soru
        {"grade": 2, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 67 mi 45 mi?", "option_a": "45", "option_b": "67", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 2, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 34 mi 78 mi?", "option_a": "34", "option_b": "78", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 89 mi 56 mi?", "option_a": "56", "option_b": "89", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # En Yakın Onluğa Yuvarlama - 2 soru
        {"grade": 2, "topic": "En Yakın Onluğa Yuvarlama", "question_text": "67 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "60", "option_b": "65", "option_c": "70", "option_d": "75", "correct_answer": "C"},
        {"grade": 2, "topic": "En Yakın Onluğa Yuvarlama", "question_text": "34 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "30", "option_b": "35", "option_c": "40", "option_d": "45", "correct_answer": "A"},
        
        # Toplama İşlemi - 4 soru
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "45 + 23 = ?", "option_a": "66", "option_b": "67", "option_c": "68", "option_d": "69", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "67 + 12 = ?", "option_a": "77", "option_b": "78", "option_c": "79", "option_d": "80", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "34 + 45 = ?", "option_a": "77", "option_b": "78", "option_c": "79", "option_d": "80", "correct_answer": "C"},
        {"grade": 2, "topic": "Toplama İşlemi", "question_text": "56 + 23 = ?", "option_a": "77", "option_b": "78", "option_c": "79", "option_d": "80", "correct_answer": "C"},
        
        # Çıkarma İşlemi - 3 soru
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "67 - 23 = ?", "option_a": "42", "option_b": "43", "option_c": "44", "option_d": "45", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "89 - 34 = ?", "option_a": "53", "option_b": "54", "option_c": "55", "option_d": "56", "correct_answer": "C"},
        {"grade": 2, "topic": "Çıkarma İşlemi", "question_text": "78 - 45 = ?", "option_a": "31", "option_b": "32", "option_c": "33", "option_d": "34", "correct_answer": "C"},
        
        # Çarpma İşlemi - 3 soru
        {"grade": 2, "topic": "Çarpma İşlemi", "question_text": "6 x 4 = ?", "option_a": "20", "option_b": "22", "option_c": "24", "option_d": "26", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşlemi", "question_text": "7 x 3 = ?", "option_a": "18", "option_b": "20", "option_c": "21", "option_d": "24", "correct_answer": "C"},
        {"grade": 2, "topic": "Çarpma İşlemi", "question_text": "5 x 5 = ?", "option_a": "20", "option_b": "22", "option_c": "24", "option_d": "25", "correct_answer": "D"},
        
        # Bölme İşlemi - 2 soru
        {"grade": 2, "topic": "Bölme İşlemi", "question_text": "12 ÷ 3 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 2, "topic": "Bölme İşlemi", "question_text": "15 ÷ 5 = ?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        
        # Geometrik Cisimler - 2 soru
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Küre", "correct_answer": "B"},
        {"grade": 2, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küre şeklindedir?", "option_a": "Küp", "option_b": "Top", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        
        # Geometrik Şekiller - 2 soru
        {"grade": 2, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 2, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "C"},
        
        # Uzamsal İlişkiler - 2 soru
        {"grade": 2, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetriktir?", "option_a": "Düzensiz şekil", "option_b": "Kare", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 2, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetri eksenine sahiptir?", "option_a": "Düzensiz şekil", "option_b": "Dikdörtgen", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        
        # Geometrik Örüntüler - 2 soru
        {"grade": 2, "topic": "Geometrik Örüntüler", "question_text": "Kare, daire, kare, daire, ? örüntüsünde ? yerine hangi şekil gelir?", "option_a": "Kare", "option_b": "Daire", "option_c": "Üçgen", "option_d": "Dikdörtgen", "correct_answer": "A"},
        {"grade": 2, "topic": "Geometrik Örüntüler", "question_text": "Üçgen, kare, üçgen, kare, ? örüntüsünde ? yerine hangi şekil gelir?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        
        # Uzunluk Ölçme - 2 soru
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: silgi mi kalem mi?", "option_a": "Silgi", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        
        # Zaman Ölçme - 2 soru
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir saatte kaç dakika vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 2, "topic": "Zaman Ölçme", "question_text": "Bir dakikada kaç saniye vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        
        # Paralarımız - 2 soru
        {"grade": 2, "topic": "Paralarımız", "question_text": "5 TL + 3 TL = ?", "option_a": "6 TL", "option_b": "7 TL", "option_c": "8 TL", "option_d": "9 TL", "correct_answer": "C"},
        {"grade": 2, "topic": "Paralarımız", "question_text": "10 TL - 4 TL = ?", "option_a": "4 TL", "option_b": "5 TL", "option_c": "6 TL", "option_d": "7 TL", "correct_answer": "C"},
        
        # Sıvı Ölçme - 2 soru
        {"grade": 2, "topic": "Sıvı Ölçme", "question_text": "Hangi kap daha fazla su alır: bardak mı kova mı?", "option_a": "Bardak", "option_b": "Kova", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 2, "topic": "Sıvı Ölçme", "question_text": "Hangi kap daha az su alır: fincan mı sürahi mi?", "option_a": "Fincan", "option_b": "Sürahi", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        
        # Tartma - 2 soru
        {"grade": 2, "topic": "Tartma", "question_text": "Hangi nesne daha ağırdır: kitap mı kalem mi?", "option_a": "Kitap", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 2, "topic": "Tartma", "question_text": "Hangi nesne daha hafiftir: tüy mü taş mı?", "option_a": "Taş", "option_b": "Tüy", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Basit Grafikler - 2 soru
        {"grade": 2, "topic": "Basit Grafikler", "question_text": "Bir grafikte en yüksek çubuk hangi veriyi gösterir?", "option_a": "En düşük değer", "option_b": "En yüksek değer", "option_c": "Ortalama değer", "option_d": "Toplam değer", "correct_answer": "B"},
        {"grade": 2, "topic": "Basit Grafikler", "question_text": "Grafikte en kısa çubuk hangi veriyi gösterir?", "option_a": "En düşük değer", "option_b": "En yüksek değer", "option_c": "Ortalama değer", "option_d": "Toplam değer", "correct_answer": "A"}
    ]
    
    return grade2_questions

def insert_grade3_questions():
    """3. sınıf için matematik sorularını ekler"""
    grade3_questions = [
        # DOĞAL SAYILAR - 1000 İçinde Sayılar
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "567 sayısından sonra hangi sayı gelir?", "option_a": "566", "option_b": "567", "option_c": "568", "option_d": "569", "correct_answer": "C"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "789 sayısından önce hangi sayı gelir?", "option_a": "787", "option_b": "788", "option_c": "789", "option_d": "790", "correct_answer": "B"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "456 sayısı kaç basamaklıdır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "B"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "999 sayısından sonra hangi sayı gelir?", "option_a": "998", "option_b": "999", "option_c": "1000", "option_d": "1001", "correct_answer": "C"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "234 sayısından önce hangi sayı gelir?", "option_a": "232", "option_b": "233", "option_c": "234", "option_d": "235", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Basamak Değeri
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "567 sayısında kaç tane yüzlük vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "500", "correct_answer": "A"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "789 sayısında kaç tane onluk vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "80", "correct_answer": "B"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "456 sayısında kaç tane birlik vardır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "456", "correct_answer": "C"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "345 sayısında kaç tane yüzlük vardır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "300", "correct_answer": "A"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "678 sayısında kaç tane onluk vardır?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "70", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Sayıları Karşılaştırma ve Sıralama
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 567 mi 789 mi?", "option_a": "567", "option_b": "789", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 456 mi 678 mi?", "option_a": "456", "option_b": "678", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 892 mi 876 mi?", "option_a": "876", "option_b": "892", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 345 mi 567 mi?", "option_a": "345", "option_b": "567", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 734 mi 729 mi?", "option_a": "729", "option_b": "734", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Ritmik Saymalar
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Altışar ritmik sayarken 24'ten sonra hangi sayı gelir?", "option_a": "25", "option_b": "28", "option_c": "30", "option_d": "32", "correct_answer": "C"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Yedişer ritmik sayarken 21'den sonra hangi sayı gelir?", "option_a": "22", "option_b": "25", "option_c": "28", "option_d": "30", "correct_answer": "C"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Sekizer ritmik sayarken 32'den sonra hangi sayı gelir?", "option_a": "33", "option_b": "36", "option_c": "38", "option_d": "40", "correct_answer": "D"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Dokuzar ritmik sayarken 27'den sonra hangi sayı gelir?", "option_a": "28", "option_b": "30", "option_c": "33", "option_d": "36", "correct_answer": "D"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Altışar ritmik sayarken 18'den sonra hangi sayı gelir?", "option_a": "19", "option_b": "22", "option_c": "24", "option_d": "26", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - Tek ve Çift Sayılar
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı tektir?", "option_a": "24", "option_b": "36", "option_c": "47", "option_d": "58", "correct_answer": "C"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı çifttir?", "option_a": "35", "option_b": "47", "option_c": "52", "option_d": "61", "correct_answer": "C"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı tektir?", "option_a": "42", "option_b": "56", "option_c": "63", "option_d": "78", "correct_answer": "C"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı çifttir?", "option_a": "31", "option_b": "45", "option_c": "53", "option_d": "64", "correct_answer": "D"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı tektir?", "option_a": "28", "option_b": "39", "option_c": "46", "option_d": "54", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Romen Rakamları
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "I sayısı kaçtır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "A"},
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "V sayısı kaçtır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "C"},
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "X sayısı kaçtır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "III sayısı kaçtır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "C"},
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "VII sayısı kaçtır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - Sayı Örüntüleri
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "3, 6, 9, 12, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "5, 10, 15, 20, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "21", "option_b": "22", "option_c": "23", "option_d": "25", "correct_answer": "D"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "2, 6, 10, 14, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "15", "option_b": "16", "option_c": "17", "option_d": "18", "correct_answer": "D"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "10, 20, 30, 40, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "41", "option_b": "45", "option_c": "50", "option_d": "55", "correct_answer": "C"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "4, 8, 12, 16, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "17", "option_b": "18", "option_c": "19", "option_d": "20", "correct_answer": "D"},
        
        # DOĞAL SAYILAR - En Yakın Onluğa ve Yüzlüğe Yuvarlama
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "567 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "560", "option_b": "565", "option_c": "570", "option_d": "575", "correct_answer": "C"},
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "456 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "400", "option_b": "450", "option_c": "500", "option_d": "550", "correct_answer": "C"},
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "789 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "780", "option_b": "785", "option_c": "790", "option_d": "795", "correct_answer": "C"},
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "234 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "200", "option_b": "230", "option_c": "250", "option_d": "300", "correct_answer": "A"},
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "678 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "670", "option_b": "675", "option_c": "680", "option_d": "685", "correct_answer": "C"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Toplama İşlemi
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "456 + 234 = ?", "option_a": "680", "option_b": "685", "option_c": "690", "option_d": "695", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "567 + 123 = ?", "option_a": "680", "option_b": "685", "option_c": "690", "option_d": "695", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "789 + 111 = ?", "option_a": "890", "option_b": "895", "option_c": "900", "option_d": "905", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "345 + 255 = ?", "option_a": "590", "option_b": "595", "option_c": "600", "option_d": "605", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "678 + 222 = ?", "option_a": "890", "option_b": "895", "option_c": "900", "option_d": "905", "correct_answer": "C"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Çıkarma İşlemi
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "567 - 234 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "789 - 456 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "678 - 345 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "456 - 123 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "789 - 456 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Çarpma İşlemi
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "8 x 7 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "9 x 6 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "7 x 8 = ?", "option_a": "54", "option_b": "56", "option_c": "58", "option_d": "60", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "6 x 9 = ?", "option_a": "52", "option_b": "54", "option_c": "56", "option_d": "58", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "5 x 8 = ?", "option_a": "35", "option_b": "40", "option_c": "45", "option_d": "50", "correct_answer": "B"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Bölme İşlemi
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "24 ÷ 6 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "35 ÷ 7 = ?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "48 ÷ 8 = ?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "63 ÷ 9 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "42 ÷ 6 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        
        # KESİRLER - Bütün, Yarım ve Çeyrek
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün yarısı kaç çeyrek eder?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün çeyreği kaç yarım eder?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "A"},
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "İki yarım kaç bütün eder?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "B"},
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Dört çeyrek kaç bütün eder?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "B"},
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün yarısı kaç bütün eder?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        
        # GEOMETRİ - Geometrik Cisimler
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi geometrik cisim 6 yüzeyi olan küp şeklindedir?", "option_a": "Küre", "option_b": "Küp", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi geometrik cisim yuvarlak ve küre şeklindedir?", "option_a": "Küp", "option_b": "Silindir", "option_c": "Küre", "option_d": "Koni", "correct_answer": "C"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi geometrik cisim silindir şeklindedir?", "option_a": "Küp", "option_b": "Silindir", "option_c": "Küre", "option_d": "Koni", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi geometrik cisim koni şeklindedir?", "option_a": "Küp", "option_b": "Silindir", "option_c": "Küre", "option_d": "Koni", "correct_answer": "D"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi geometrik cisim dikdörtgen prizma şeklindedir?", "option_a": "Küp", "option_b": "Dikdörtgen Prizma", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        
        # GEOMETRİ - Geometrik Şekiller
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 3 köşeli ve 3 kenarlıdır?", "option_a": "Kare", "option_b": "Dikdörtgen", "option_c": "Üçgen", "option_d": "Daire", "correct_answer": "C"},
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ama kare değildir?", "option_a": "Üçgen", "option_b": "Daire", "option_c": "Dikdörtgen", "option_d": "Kare", "correct_answer": "C"},
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil köşesi yoktur?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Dikdörtgen", "option_d": "Daire", "correct_answer": "D"},
        
        # GEOMETRİ - Kenar Çeşitleri
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi kenar türü düzdür?", "option_a": "Eğri", "option_b": "Düz", "option_c": "Açık", "option_d": "Kapalı", "correct_answer": "B"},
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi kenar türü eğridir?", "option_a": "Düz", "option_b": "Eğri", "option_c": "Açık", "option_d": "Kapalı", "correct_answer": "B"},
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi kenar türü açıktır?", "option_a": "Düz", "option_b": "Eğri", "option_c": "Açık", "option_d": "Kapalı", "correct_answer": "C"},
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi kenar türü kapalıdır?", "option_a": "Düz", "option_b": "Eğri", "option_c": "Açık", "option_d": "Kapalı", "correct_answer": "D"},
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi kenar türü doğru parçasıdır?", "option_a": "Düz", "option_b": "Eğri", "option_c": "Açık", "option_d": "Kapalı", "correct_answer": "A"},
        
        # GEOMETRİ - Uzamsal İlişkiler
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetriktir?", "option_a": "Düzensiz şekil", "option_b": "Kare", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetri ekseni vardır?", "option_a": "Düzensiz şekil", "option_b": "Daire", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetriktir?", "option_a": "Düzensiz şekil", "option_b": "Üçgen", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetri ekseni vardır?", "option_a": "Düzensiz şekil", "option_b": "Dikdörtgen", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetriktir?", "option_a": "Düzensiz şekil", "option_b": "Kare", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        
        # ÖLÇME - Uzunluk Ölçme
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "1 metre kaç santimetredir?", "option_a": "50", "option_b": "75", "option_c": "100", "option_d": "150", "correct_answer": "C"},
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "50 santimetre kaç metredir?", "option_a": "0.25", "option_b": "0.50", "option_c": "0.75", "option_d": "1.00", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "100 santimetre kaç metredir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "C"},
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "25 santimetre kaç metredir?", "option_a": "0.10", "option_b": "0.25", "option_c": "0.50", "option_d": "0.75", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "75 santimetre kaç metredir?", "option_a": "0.50", "option_b": "0.75", "option_c": "1.00", "option_d": "1.25", "correct_answer": "B"},
        
        # ÖLÇME - Zaman Ölçme
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir haftada kaç gün vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "C"},
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir günde kaç saat vardır?", "option_a": "12", "option_b": "18", "option_c": "24", "option_d": "30", "correct_answer": "C"},
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir yılda kaç ay vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir ayda kaç hafta vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_answer": "C"},
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir saatte kaç dakika vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        
        # ÖLÇME - Paralarımız
        {"grade": 3, "topic": "Paralarımız", "question_text": "5 TL + 3 TL = ?", "option_a": "6 TL", "option_b": "7 TL", "option_c": "8 TL", "option_d": "9 TL", "correct_answer": "C"},
        {"grade": 3, "topic": "Paralarımız", "question_text": "10 TL - 4 TL = ?", "option_a": "4 TL", "option_b": "5 TL", "option_c": "6 TL", "option_d": "7 TL", "correct_answer": "C"},
        {"grade": 3, "topic": "Paralarımız", "question_text": "2 TL + 7 TL = ?", "option_a": "7 TL", "option_b": "8 TL", "option_c": "9 TL", "option_d": "10 TL", "correct_answer": "C"},
        {"grade": 3, "topic": "Paralarımız", "question_text": "15 TL - 6 TL = ?", "option_a": "7 TL", "option_b": "8 TL", "option_c": "9 TL", "option_d": "10 TL", "correct_answer": "C"},
        {"grade": 3, "topic": "Paralarımız", "question_text": "8 TL + 5 TL = ?", "option_a": "11 TL", "option_b": "12 TL", "option_c": "13 TL", "option_d": "14 TL", "correct_answer": "C"},
        
        # PROBLEM ÇÖZME
        {"grade": 3, "topic": "Problem Çözme", "question_text": "5 elma, 3 portakal, 2 muz varsa toplam kaç meyve vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 3, "topic": "Problem Çözme", "question_text": "4 kırmızı, 6 mavi, 3 yeşil top varsa toplam kaç top vardır?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 3, "topic": "Problem Çözme", "question_text": "7 kedi, 5 köpek, 3 kuş varsa toplam kaç hayvan vardır?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 3, "topic": "Problem Çözme", "question_text": "2 kare, 5 üçgen, 3 daire varsa toplam kaç şekil vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 3, "topic": "Problem Çözme", "question_text": "6 kalem, 4 silgi, 2 cetvel varsa toplam kaç eşya vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        
        # EK SORULAR - 40 adet rastgele dağıtılmış
        # 1000 İçinde Sayılar - 4 soru
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "234 sayısından sonra hangi sayı gelir?", "option_a": "233", "option_b": "234", "option_c": "235", "option_d": "236", "correct_answer": "C"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "567 sayısından önce hangi sayı gelir?", "option_a": "565", "option_b": "566", "option_c": "567", "option_d": "568", "correct_answer": "B"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "789 sayısından sonra hangi sayı gelir?", "option_a": "788", "option_b": "789", "option_c": "790", "option_d": "791", "correct_answer": "C"},
        {"grade": 3, "topic": "1000 İçinde Sayılar", "question_text": "456 sayısından önce hangi sayı gelir?", "option_a": "454", "option_b": "455", "option_c": "456", "option_d": "457", "correct_answer": "B"},
        
        # Basamak Değeri - 3 soru
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "234 sayısında kaç tane yüzlük vardır?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "200", "correct_answer": "A"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "567 sayısında kaç tane onluk vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "60", "correct_answer": "B"},
        {"grade": 3, "topic": "Basamak Değeri", "question_text": "789 sayısında kaç tane birlik vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "789", "correct_answer": "C"},
        
        # Sayıları Karşılaştırma ve Sıralama - 3 soru
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 456 mi 567 mi?", "option_a": "456", "option_b": "567", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 234 mi 345 mi?", "option_a": "234", "option_b": "345", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 3, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 678 mi 789 mi?", "option_a": "678", "option_b": "789", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Ritmik Saymalar - 3 soru
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Altışar ritmik sayarken 30'dan sonra hangi sayı gelir?", "option_a": "31", "option_b": "34", "option_c": "36", "option_d": "38", "correct_answer": "C"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Yedişer ritmik sayarken 28'den sonra hangi sayı gelir?", "option_a": "29", "option_b": "32", "option_c": "35", "option_d": "38", "correct_answer": "C"},
        {"grade": 3, "topic": "Ritmik Saymalar", "question_text": "Sekizer ritmik sayarken 40'dan sonra hangi sayı gelir?", "option_a": "41", "option_b": "44", "option_c": "46", "option_d": "48", "correct_answer": "D"},
        
        # Tek ve Çift Sayılar - 3 soru
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı tektir?", "option_a": "246", "option_b": "357", "option_c": "468", "option_d": "579", "correct_answer": "B"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı çifttir?", "option_a": "135", "option_b": "246", "option_c": "357", "option_d": "468", "correct_answer": "B"},
        {"grade": 3, "topic": "Tek ve Çift Sayılar", "question_text": "Hangi sayı tektir?", "option_a": "234", "option_b": "345", "option_c": "456", "option_d": "567", "correct_answer": "B"},
        
        # Romen Rakamları - 2 soru
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "II sayısı kaçtır?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 3, "topic": "Romen Rakamları", "question_text": "IV sayısı kaçtır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        
        # Sayı Örüntüleri - 3 soru
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "2, 5, 8, 11, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "3, 7, 11, 15, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "16", "option_b": "17", "option_c": "18", "option_d": "19", "correct_answer": "D"},
        {"grade": 3, "topic": "Sayı Örüntüleri", "question_text": "4, 9, 14, 19, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "20", "option_b": "21", "option_c": "22", "option_d": "24", "correct_answer": "D"},
        
        # En Yakın Onluğa ve Yüzlüğe Yuvarlama - 2 soru
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "234 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "230", "option_b": "235", "option_c": "240", "option_d": "245", "correct_answer": "A"},
        {"grade": 3, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "567 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "500", "option_b": "550", "option_c": "600", "option_d": "650", "correct_answer": "C"},
        
        # Toplama İşlemi - 4 soru
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "234 + 123 = ?", "option_a": "355", "option_b": "356", "option_c": "357", "option_d": "358", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "456 + 234 = ?", "option_a": "688", "option_b": "689", "option_c": "690", "option_d": "691", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "567 + 123 = ?", "option_a": "688", "option_b": "689", "option_c": "690", "option_d": "691", "correct_answer": "C"},
        {"grade": 3, "topic": "Toplama İşlemi", "question_text": "789 + 111 = ?", "option_a": "898", "option_b": "899", "option_c": "900", "option_d": "901", "correct_answer": "C"},
        
        # Çıkarma İşlemi - 3 soru
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "567 - 234 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "789 - 456 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        {"grade": 3, "topic": "Çıkarma İşlemi", "question_text": "678 - 345 = ?", "option_a": "331", "option_b": "332", "option_c": "333", "option_d": "334", "correct_answer": "C"},
        
        # Çarpma İşlemi - 3 soru
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "6 x 8 = ?", "option_a": "46", "option_b": "48", "option_c": "50", "option_d": "52", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "7 x 9 = ?", "option_a": "61", "option_b": "63", "option_c": "65", "option_d": "67", "correct_answer": "B"},
        {"grade": 3, "topic": "Çarpma İşlemi", "question_text": "8 x 6 = ?", "option_a": "46", "option_b": "48", "option_c": "50", "option_d": "52", "correct_answer": "B"},
        
        # Bölme İşlemi - 2 soru
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "32 ÷ 8 = ?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 3, "topic": "Bölme İşlemi", "question_text": "42 ÷ 6 = ?", "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_answer": "B"},
        
        # Bütün, Yarım ve Çeyrek - 2 soru
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün çeyreği kaç yarım eder?", "option_a": "1/2", "option_b": "1", "option_c": "2", "option_d": "4", "correct_answer": "A"},
        {"grade": 3, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "İki yarım kaç bütün eder?", "option_a": "1/2", "option_b": "1", "option_c": "2", "option_d": "4", "correct_answer": "B"},
        
        # Geometrik Cisimler - 2 soru
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küp şeklindedir?", "option_a": "Top", "option_b": "Zar", "option_c": "Silindir", "option_d": "Küre", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Cisimler", "question_text": "Hangi cisim küre şeklindedir?", "option_a": "Küp", "option_b": "Top", "option_c": "Silindir", "option_d": "Koni", "correct_answer": "B"},
        
        # Geometrik Şekiller - 2 soru
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil 4 köşeli ve 4 kenarlıdır?", "option_a": "Üçgen", "option_b": "Kare", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Geometrik Şekiller", "question_text": "Hangi şekil yuvarlaktır?", "option_a": "Kare", "option_b": "Üçgen", "option_c": "Daire", "option_d": "Dikdörtgen", "correct_answer": "C"},
        
        # Kenar Çeşitleri - 2 soru
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi çizgi düzdür?", "option_a": "Dalgalı çizgi", "option_b": "Düz çizgi", "option_c": "Kıvrımlı çizgi", "option_d": "Zikzak çizgi", "correct_answer": "B"},
        {"grade": 3, "topic": "Kenar Çeşitleri", "question_text": "Hangi çizgi eğridir?", "option_a": "Düz çizgi", "option_b": "Dalgalı çizgi", "option_c": "Dikey çizgi", "option_d": "Yatay çizgi", "correct_answer": "B"},
        
        # Uzamsal İlişkiler - 2 soru
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetriktir?", "option_a": "Düzensiz şekil", "option_b": "Kare", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        {"grade": 3, "topic": "Uzamsal İlişkiler", "question_text": "Hangi şekil simetri eksenine sahiptir?", "option_a": "Düzensiz şekil", "option_b": "Dikdörtgen", "option_c": "Asimetrik şekil", "option_d": "Düzensiz üçgen", "correct_answer": "B"},
        
        # Uzunluk Ölçme - 2 soru
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha uzundur: cetvel mi kalem mi?", "option_a": "Cetvel", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 3, "topic": "Uzunluk Ölçme", "question_text": "Hangi nesne daha kısadır: silgi mi kalem mi?", "option_a": "Silgi", "option_b": "Kalem", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        
        # Zaman Ölçme - 2 soru
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir saatte kaç dakika vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 3, "topic": "Zaman Ölçme", "question_text": "Bir dakikada kaç saniye vardır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        
        # Paralarımız - 2 soru
        {"grade": 3, "topic": "Paralarımız", "question_text": "5 TL + 3 TL = ?", "option_a": "6 TL", "option_b": "7 TL", "option_c": "8 TL", "option_d": "9 TL", "correct_answer": "C"},
        {"grade": 3, "topic": "Paralarımız", "question_text": "10 TL - 4 TL = ?", "option_a": "4 TL", "option_b": "5 TL", "option_c": "6 TL", "option_d": "7 TL", "correct_answer": "C"},
        
        # Problem Çözme - 2 soru
        {"grade": 3, "topic": "Problem Çözme", "question_text": "3 kalem, 2 silgi, 1 cetvel varsa toplam kaç eşya vardır?", "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_answer": "B"},
        {"grade": 3, "topic": "Problem Çözme", "question_text": "4 kitap, 3 defter, 2 kalem varsa toplam kaç eşya vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"}
    ]
    
    return grade3_questions

def insert_grade4_questions():
    """4. sınıf için matematik sorularını ekler"""
    grade4_questions = [
        # DOĞAL SAYILAR - Dört, Beş ve Altı Basamaklı Doğal Sayılar
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "1234 sayısı kaç basamaklıdır?", "option_a": "3", "option_b": "4", "option_c": "5", "option_d": "6", "correct_answer": "B"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "56789 sayısı kaç basamaklıdır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "B"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "123456 sayısı kaç basamaklıdır?", "option_a": "4", "option_b": "5", "option_c": "6", "option_d": "7", "correct_answer": "C"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "9999 sayısından sonra hangi sayı gelir?", "option_a": "9998", "option_b": "9999", "option_c": "10000", "option_d": "10001", "correct_answer": "C"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "99999 sayısından sonra hangi sayı gelir?", "option_a": "99998", "option_b": "99999", "option_c": "100000", "option_d": "100001", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - Basamak Değeri ve Sayı Değeri
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "5678 sayısında 6'nın basamak değeri kaçtır?", "option_a": "6", "option_b": "60", "option_c": "600", "option_d": "6000", "correct_answer": "C"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "12345 sayısında 3'ün basamak değeri kaçtır?", "option_a": "3", "option_b": "30", "option_c": "300", "option_d": "3000", "correct_answer": "C"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "98765 sayısında 8'in basamak değeri kaçtır?", "option_a": "8", "option_b": "80", "option_c": "800", "option_d": "8000", "correct_answer": "D"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "45678 sayısında 7'nin sayı değeri kaçtır?", "option_a": "7", "option_b": "70", "option_c": "700", "option_d": "7000", "correct_answer": "A"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "34567 sayısında 4'ün basamak değeri kaçtır?", "option_a": "4", "option_b": "40", "option_c": "400", "option_d": "4000", "correct_answer": "D"},
        
        # DOĞAL SAYILAR - Sayıları Karşılaştırma ve Sıralama
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 5678 mi 6789 mi?", "option_a": "5678", "option_b": "6789", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 12345 mi 23456 mi?", "option_a": "12345", "option_b": "23456", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 98765 mi 87654 mi?", "option_a": "87654", "option_b": "98765", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 45678 mi 56789 mi?", "option_a": "45678", "option_b": "56789", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 65432 mi 54321 mi?", "option_a": "54321", "option_b": "65432", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # DOĞAL SAYILAR - Sayı Örüntüleri
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "2, 6, 10, 14, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "15", "option_b": "16", "option_c": "17", "option_d": "18", "correct_answer": "D"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "5, 15, 25, 35, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "40", "option_b": "45", "option_c": "50", "option_d": "55", "correct_answer": "B"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "10, 20, 30, 40, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "41", "option_b": "45", "option_c": "50", "option_d": "55", "correct_answer": "C"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "3, 9, 15, 21, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "24", "option_b": "25", "option_c": "26", "option_d": "27", "correct_answer": "D"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "4, 12, 20, 28, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "32", "option_b": "34", "option_c": "36", "option_d": "38", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - En Yakın Onluğa ve Yüzlüğe Yuvarlama
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "5678 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "5670", "option_b": "5675", "option_c": "5680", "option_d": "5685", "correct_answer": "C"},
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "12345 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "12300", "option_b": "12350", "option_c": "12400", "option_d": "12450", "correct_answer": "C"},
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "45678 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "45670", "option_b": "45675", "option_c": "45680", "option_d": "45685", "correct_answer": "C"},
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "78901 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "78900", "option_b": "78950", "option_c": "79000", "option_d": "79050", "correct_answer": "C"},
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "34567 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "34560", "option_b": "34565", "option_c": "34570", "option_d": "34575", "correct_answer": "C"},
        
        # DOĞAL SAYILAR - Romen Rakamları
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XV sayısı kaçtır?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XIX sayısı kaçtır?", "option_a": "17", "option_b": "18", "option_c": "19", "option_d": "20", "correct_answer": "C"},
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XVI sayısı kaçtır?", "option_a": "14", "option_b": "15", "option_c": "16", "option_d": "17", "correct_answer": "C"},
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XVII sayısı kaçtır?", "option_a": "15", "option_b": "16", "option_c": "17", "option_d": "18", "correct_answer": "C"},
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XX sayısı kaçtır?", "option_a": "18", "option_b": "19", "option_c": "20", "option_d": "21", "correct_answer": "C"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Toplama İşlemi
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "5678 + 2345 = ?", "option_a": "8000", "option_b": "8023", "option_c": "8024", "option_d": "8025", "correct_answer": "B"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "12345 + 67890 = ?", "option_a": "80000", "option_b": "80235", "option_c": "80236", "option_d": "80237", "correct_answer": "B"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "45678 + 54321 = ?", "option_a": "99999", "option_b": "100000", "option_c": "100001", "option_d": "100002", "correct_answer": "A"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "98765 + 1234 = ?", "option_a": "99999", "option_b": "100000", "option_c": "100001", "option_d": "100002", "correct_answer": "A"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "34567 + 65432 = ?", "option_a": "99999", "option_b": "100000", "option_c": "100001", "option_d": "100002", "correct_answer": "A"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Çıkarma İşlemi
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "9876 - 5432 = ?", "option_a": "4444", "option_b": "4445", "option_c": "4446", "option_d": "4447", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "56789 - 12345 = ?", "option_a": "44444", "option_b": "44445", "option_c": "44446", "option_d": "44447", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "87654 - 43210 = ?", "option_a": "44444", "option_b": "44445", "option_c": "44446", "option_d": "44447", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "65432 - 21098 = ?", "option_a": "44334", "option_b": "44335", "option_c": "44336", "option_d": "44337", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "54321 - 12345 = ?", "option_a": "41976", "option_b": "41977", "option_c": "41978", "option_d": "41979", "correct_answer": "A"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Çarpma İşlemi
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "234 x 56 = ?", "option_a": "13104", "option_b": "13105", "option_c": "13106", "option_d": "13107", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "345 x 67 = ?", "option_a": "23115", "option_b": "23116", "option_c": "23117", "option_d": "23118", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "456 x 78 = ?", "option_a": "35568", "option_b": "35569", "option_c": "35570", "option_d": "35571", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "567 x 89 = ?", "option_a": "50463", "option_b": "50464", "option_c": "50465", "option_d": "50466", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "678 x 90 = ?", "option_a": "61020", "option_b": "61021", "option_c": "61022", "option_d": "61023", "correct_answer": "A"},
        
        # DOĞAL SAYILARLA İŞLEMLER - Bölme İşlemi
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "1234 ÷ 2 = ?", "option_a": "615", "option_b": "616", "option_c": "617", "option_d": "618", "correct_answer": "C"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "5678 ÷ 4 = ?", "option_a": "1419", "option_b": "1420", "option_c": "1421", "option_d": "1422", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "9876 ÷ 6 = ?", "option_a": "1646", "option_b": "1647", "option_c": "1648", "option_d": "1649", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "5432 ÷ 8 = ?", "option_a": "679", "option_b": "680", "option_c": "681", "option_d": "682", "correct_answer": "A"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "8765 ÷ 5 = ?", "option_a": "1753", "option_b": "1754", "option_c": "1755", "option_d": "1756", "correct_answer": "A"},
        
        # KESİRLER - Bütün, Yarım ve Çeyrek
        {"grade": 4, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün yarısı kaç çeyrek eder?", "option_a": "1", "option_b": "2", "option_c": "3", "option_d": "4", "correct_answer": "B"},
        {"grade": 4, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün çeyreği kaç yarım eder?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "A"},
        {"grade": 4, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "İki yarım kaç bütün eder?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "B"},
        {"grade": 4, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Dört çeyrek kaç bütün eder?", "option_a": "0.5", "option_b": "1", "option_c": "1.5", "option_d": "2", "correct_answer": "B"},
        {"grade": 4, "topic": "Bütün, Yarım ve Çeyrek", "question_text": "Bir bütünün yarısı kaç bütün eder?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        
        # KESİRLER - Basit Kesirler
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "2/3 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "3/4 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "4/5 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "5/6 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "6/7 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        
        # KESİRLER - Tam Sayılı Kesirler ve Bileşik Kesirler
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "1 1/2 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "2 1/3 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "3 1/4 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "4 1/5 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "5 1/6 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        
        # KESİRLER - Kesirleri Karşılaştırma ve Sıralama
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha büyüktür: 1/2 mi 1/3 mü?", "option_a": "1/2", "option_b": "1/3", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha küçüktür: 1/4 mü 1/5 mi?", "option_a": "1/4", "option_b": "1/5", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha büyüktür: 2/3 mü 2/4 mü?", "option_a": "2/3", "option_b": "2/4", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha küçüktür: 3/4 mü 3/5 mi?", "option_a": "3/4", "option_b": "3/5", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha büyüktür: 4/5 mi 4/6 mı?", "option_a": "4/5", "option_b": "4/6", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        
        # KESİRLER - Kesirlerle Toplama ve Çıkarma
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/2 + 1/2 = ?", "option_a": "1/4", "option_b": "1/2", "option_c": "1", "option_d": "2", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/3 + 1/3 = ?", "option_a": "1/6", "option_b": "1/3", "option_c": "2/3", "option_d": "1", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/4 + 1/4 = ?", "option_a": "1/8", "option_b": "1/4", "option_c": "1/2", "option_d": "1", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/5 + 1/5 = ?", "option_a": "1/10", "option_b": "1/5", "option_c": "2/5", "option_d": "1", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/6 + 1/6 = ?", "option_a": "1/12", "option_b": "1/6", "option_c": "1/3", "option_d": "1", "correct_answer": "C"},
        
        # GEOMETRİ - Açı Çeşitleri
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "90 derece hangi açı türüdür?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "B"},
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "45 derece hangi açı türüdür?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "A"},
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "135 derece hangi açı türüdür?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "C"},
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "30 derece hangi açı türüdür?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "A"},
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "150 derece hangi açı türüdür?", "option_a": "Dar açı", "option_b": "Dik açı", "option_c": "Geniş açı", "option_d": "Doğru açı", "correct_answer": "C"},
        
        # GEOMETRİ - Alan ve Çevre
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarı 5 cm olan karenin çevresi kaç cm'dir?", "option_a": "15", "option_b": "20", "option_c": "25", "option_d": "30", "correct_answer": "B"},
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarları 4 cm ve 6 cm olan dikdörtgenin çevresi kaç cm'dir?", "option_a": "16", "option_b": "18", "option_c": "20", "option_d": "24", "correct_answer": "C"},
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarı 3 cm olan karenin alanı kaç cm²'dir?", "option_a": "6", "option_b": "9", "option_c": "12", "option_d": "15", "correct_answer": "B"},
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarları 5 cm ve 8 cm olan dikdörtgenin alanı kaç cm²'dir?", "option_a": "26", "option_b": "32", "option_c": "40", "option_d": "48", "correct_answer": "C"},
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarı 6 cm olan karenin çevresi kaç cm'dir?", "option_a": "18", "option_b": "24", "option_c": "30", "option_d": "36", "correct_answer": "B"},
        
        # ÖLÇME - Uzunluk, Çevre ve Alan Ölçme
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "1 kilometre kaç metredir?", "option_a": "100", "option_b": "500", "option_c": "1000", "option_d": "2000", "correct_answer": "C"},
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "1 metre kaç santimetredir?", "option_a": "10", "option_b": "50", "option_c": "100", "option_d": "200", "correct_answer": "C"},
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "1 santimetre kaç milimetredir?", "option_a": "5", "option_b": "10", "option_c": "15", "option_d": "20", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "500 metre kaç kilometredir?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "50 santimetre kaç metredir?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        
        # ÖLÇME - Zaman Ölçme
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "1 saat kaç dakikadır?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "1 dakika kaç saniyedir?", "option_a": "30", "option_b": "45", "option_c": "60", "option_d": "90", "correct_answer": "C"},
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "1 saat kaç saniyedir?", "option_a": "1800", "option_b": "2400", "option_c": "3000", "option_d": "3600", "correct_answer": "D"},
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "30 dakika kaç saattir?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "45 dakika kaç saattir?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "C"},
        
        # ÖLÇME - Tartma ve Sıvı Ölçme
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "1 kilogram kaç gramdır?", "option_a": "500", "option_b": "750", "option_c": "1000", "option_d": "1500", "correct_answer": "C"},
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "500 gram kaç kilogramdır?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "1 litre kaç mililitredir?", "option_a": "500", "option_b": "750", "option_c": "1000", "option_d": "1500", "correct_answer": "C"},
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "500 mililitre kaç litredir?", "option_a": "0.25", "option_b": "0.5", "option_c": "0.75", "option_d": "1", "correct_answer": "B"},
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "2 kilogram kaç gramdır?", "option_a": "1500", "option_b": "1800", "option_c": "2000", "option_d": "2500", "correct_answer": "C"},
        
        # VERİ TOPLAMA VE DEĞERLENDİRME - Sıklık Tablosu ve Çetele Tablosu
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "5 elma, 3 portakal, 2 muz varsa toplam kaç meyve vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "4 kırmızı, 6 mavi, 3 yeşil top varsa toplam kaç top vardır?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "7 kedi, 5 köpek, 3 kuş varsa toplam kaç hayvan vardır?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "2 kare, 5 üçgen, 3 daire varsa toplam kaç şekil vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "6 kalem, 4 silgi, 2 cetvel varsa toplam kaç eşya vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        
        # VERİ TOPLAMA VE DEĞERLENDİRME - Problem Çözme
        {"grade": 4, "topic": "Problem Çözme", "question_text": "5 elma, 3 portakal, 2 muz varsa toplam kaç meyve vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Problem Çözme", "question_text": "4 kırmızı, 6 mavi, 3 yeşil top varsa toplam kaç top vardır?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"},
        {"grade": 4, "topic": "Problem Çözme", "question_text": "7 kedi, 5 köpek, 3 kuş varsa toplam kaç hayvan vardır?", "option_a": "13", "option_b": "14", "option_c": "15", "option_d": "16", "correct_answer": "C"},
        {"grade": 4, "topic": "Problem Çözme", "question_text": "2 kare, 5 üçgen, 3 daire varsa toplam kaç şekil vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Problem Çözme", "question_text": "6 kalem, 4 silgi, 2 cetvel varsa toplam kaç eşya vardır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        
        # EK SORULAR - 40 adet rastgele dağıtılmış
        # Dört, Beş ve Altı Basamaklı Doğal Sayılar - 4 soru
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "2345 sayısından sonra hangi sayı gelir?", "option_a": "2344", "option_b": "2345", "option_c": "2346", "option_d": "2347", "correct_answer": "C"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "56789 sayısından önce hangi sayı gelir?", "option_a": "56787", "option_b": "56788", "option_c": "56789", "option_d": "56790", "correct_answer": "B"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "123456 sayısından sonra hangi sayı gelir?", "option_a": "123455", "option_b": "123456", "option_c": "123457", "option_d": "123458", "correct_answer": "C"},
        {"grade": 4, "topic": "Dört, Beş ve Altı Basamaklı Doğal Sayılar", "question_text": "98765 sayısından önce hangi sayı gelir?", "option_a": "98763", "option_b": "98764", "option_c": "98765", "option_d": "98766", "correct_answer": "B"},
        
        # Basamak Değeri ve Sayı Değeri - 3 soru
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "2345 sayısında 3'ün basamak değeri kaçtır?", "option_a": "3", "option_b": "30", "option_c": "300", "option_d": "3000", "correct_answer": "C"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "56789 sayısında 8'in sayı değeri kaçtır?", "option_a": "8", "option_b": "80", "option_c": "800", "option_d": "8000", "correct_answer": "A"},
        {"grade": 4, "topic": "Basamak Değeri ve Sayı Değeri", "question_text": "123456 sayısında 4'ün basamak değeri kaçtır?", "option_a": "4", "option_b": "40", "option_c": "400", "option_d": "4000", "correct_answer": "C"},
        
        # Sayıları Karşılaştırma ve Sıralama - 3 soru
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 2345 mi 3456 mi?", "option_a": "2345", "option_b": "3456", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha küçüktür: 12345 mi 23456 mi?", "option_a": "12345", "option_b": "23456", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "A"},
        {"grade": 4, "topic": "Sayıları Karşılaştırma ve Sıralama", "question_text": "Hangi sayı daha büyüktür: 56789 mi 67890 mi?", "option_a": "56789", "option_b": "67890", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Sayı Örüntüleri - 3 soru
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "3, 8, 13, 18, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "20", "option_b": "21", "option_c": "22", "option_d": "23", "correct_answer": "D"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "4, 10, 16, 22, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "26", "option_b": "27", "option_c": "28", "option_d": "29", "correct_answer": "C"},
        {"grade": 4, "topic": "Sayı Örüntüleri", "question_text": "5, 12, 19, 26, ? örüntüsünde ? yerine hangi sayı gelir?", "option_a": "30", "option_b": "31", "option_c": "32", "option_d": "33", "correct_answer": "D"},
        
        # En Yakın Onluğa ve Yüzlüğe Yuvarlama - 2 soru
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "2345 sayısı en yakın onluğa yuvarlanırsa kaç olur?", "option_a": "2340", "option_b": "2345", "option_c": "2350", "option_d": "2355", "correct_answer": "A"},
        {"grade": 4, "topic": "En Yakın Onluğa ve Yüzlüğe Yuvarlama", "question_text": "56789 sayısı en yakın yüzlüğe yuvarlanırsa kaç olur?", "option_a": "56700", "option_b": "56750", "option_c": "56800", "option_d": "56850", "correct_answer": "C"},
        
        # Romen Rakamları - 2 soru
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XII sayısı kaçtır?", "option_a": "10", "option_b": "11", "option_c": "12", "option_d": "13", "correct_answer": "C"},
        {"grade": 4, "topic": "Romen Rakamları", "question_text": "XIV sayısı kaçtır?", "option_a": "12", "option_b": "13", "option_c": "14", "option_d": "15", "correct_answer": "C"},
        
        # Toplama İşlemi - 4 soru
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "2345 + 1234 = ?", "option_a": "3567", "option_b": "3568", "option_c": "3569", "option_d": "3570", "correct_answer": "C"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "5678 + 2345 = ?", "option_a": "8000", "option_b": "8012", "option_c": "8013", "option_d": "8014", "correct_answer": "C"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "12345 + 67890 = ?", "option_a": "80000", "option_b": "80235", "option_c": "80236", "option_d": "80237", "correct_answer": "B"},
        {"grade": 4, "topic": "Toplama İşlemi", "question_text": "45678 + 54321 = ?", "option_a": "99999", "option_b": "100000", "option_c": "100001", "option_d": "100002", "correct_answer": "A"},
        
        # Çıkarma İşlemi - 3 soru
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "5678 - 2345 = ?", "option_a": "3333", "option_b": "3334", "option_c": "3335", "option_d": "3336", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "9876 - 5432 = ?", "option_a": "4444", "option_b": "4445", "option_c": "4446", "option_d": "4447", "correct_answer": "A"},
        {"grade": 4, "topic": "Çıkarma İşlemi", "question_text": "12345 - 6789 = ?", "option_a": "5556", "option_b": "5557", "option_c": "5558", "option_d": "5559", "correct_answer": "A"},
        
        # Çarpma İşlemi - 3 soru
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "123 x 45 = ?", "option_a": "5535", "option_b": "5536", "option_c": "5537", "option_d": "5538", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "234 x 56 = ?", "option_a": "13104", "option_b": "13105", "option_c": "13106", "option_d": "13107", "correct_answer": "A"},
        {"grade": 4, "topic": "Çarpma İşlemi", "question_text": "345 x 67 = ?", "option_a": "23115", "option_b": "23116", "option_c": "23117", "option_d": "23118", "correct_answer": "A"},
        
        # Bölme İşlemi - 2 soru
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "1234 ÷ 2 = ?", "option_a": "615", "option_b": "616", "option_c": "617", "option_d": "618", "correct_answer": "C"},
        {"grade": 4, "topic": "Bölme İşlemi", "question_text": "5678 ÷ 4 = ?", "option_a": "1419", "option_b": "1420", "option_c": "1421", "option_d": "1422", "correct_answer": "A"},
        
        # Birim Kesirler - 2 soru
        {"grade": 4, "topic": "Birim Kesirler", "question_text": "1/7 birim kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Birim Kesirler", "question_text": "1/8 birim kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        
        # Basit Kesirler - 2 soru
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "7/8 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Basit Kesirler", "question_text": "8/9 basit kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        
        # Tam Sayılı Kesirler ve Bileşik Kesirler - 2 soru
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "6 1/7 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        {"grade": 4, "topic": "Tam Sayılı Kesirler ve Bileşik Kesirler", "question_text": "7 1/8 tam sayılı kesir midir?", "option_a": "Evet", "option_b": "Hayır", "option_c": "Bilmiyorum", "option_d": "Belki", "correct_answer": "A"},
        
        # Kesirleri Karşılaştırma ve Sıralama - 2 soru
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha büyüktür: 3/4 mü 2/3 mü?", "option_a": "2/3", "option_b": "3/4", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        {"grade": 4, "topic": "Kesirleri Karşılaştırma ve Sıralama", "question_text": "Hangi kesir daha küçüktür: 1/2 mi 1/3 mü?", "option_a": "1/2", "option_b": "1/3", "option_c": "Eşit", "option_d": "Bilmiyorum", "correct_answer": "B"},
        
        # Kesirlerle Toplama ve Çıkarma - 2 soru
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "1/4 + 1/4 = ?", "option_a": "1/8", "option_b": "1/4", "option_c": "1/2", "option_d": "2/4", "correct_answer": "C"},
        {"grade": 4, "topic": "Kesirlerle Toplama ve Çıkarma", "question_text": "3/4 - 1/4 = ?", "option_a": "1/4", "option_b": "1/2", "option_c": "2/4", "option_d": "3/4", "correct_answer": "B"},
        
        # Açı Çeşitleri - 2 soru
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "Hangi açı dik açıdır?", "option_a": "45°", "option_b": "90°", "option_c": "120°", "option_d": "180°", "correct_answer": "B"},
        {"grade": 4, "topic": "Açı Çeşitleri", "question_text": "Hangi açı dar açıdır?", "option_a": "45°", "option_b": "90°", "option_c": "120°", "option_d": "180°", "correct_answer": "A"},
        
        # Alan ve Çevre - 2 soru
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarı 5 cm olan karenin çevresi kaç cm'dir?", "option_a": "15", "option_b": "20", "option_c": "25", "option_d": "30", "correct_answer": "B"},
        {"grade": 4, "topic": "Alan ve Çevre", "question_text": "Kenarları 4 cm ve 6 cm olan dikdörtgenin çevresi kaç cm'dir?", "option_a": "16", "option_b": "18", "option_c": "20", "option_d": "24", "correct_answer": "C"},
        
        # Uzunluk, Çevre ve Alan Ölçme - 2 soru
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "1 metre kaç santimetredir?", "option_a": "10", "option_b": "50", "option_c": "100", "option_d": "1000", "correct_answer": "C"},
        {"grade": 4, "topic": "Uzunluk, Çevre ve Alan Ölçme", "question_text": "1 kilometre kaç metredir?", "option_a": "100", "option_b": "500", "option_c": "1000", "option_d": "10000", "correct_answer": "C"},
        
        # Zaman Ölçme - 2 soru
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "2 saat kaç dakikadır?", "option_a": "60", "option_b": "90", "option_c": "120", "option_d": "180", "correct_answer": "C"},
        {"grade": 4, "topic": "Zaman Ölçme", "question_text": "3 dakika kaç saniyedir?", "option_a": "120", "option_b": "150", "option_c": "180", "option_d": "210", "correct_answer": "C"},
        
        # Tartma ve Sıvı Ölçme - 2 soru
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "3 kilogram kaç gramdır?", "option_a": "1500", "option_b": "2000", "option_c": "3000", "option_d": "3500", "correct_answer": "C"},
        {"grade": 4, "topic": "Tartma ve Sıvı Ölçme", "question_text": "2 litre kaç mililitredir?", "option_a": "1500", "option_b": "2000", "option_c": "2500", "option_d": "3000", "correct_answer": "B"},
        
        # Sıklık Tablosu ve Çetele Tablosu - 2 soru
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "3 elma, 5 portakal, 2 muz varsa toplam kaç meyve vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Sıklık Tablosu ve Çetele Tablosu", "question_text": "4 kırmızı, 3 mavi, 2 yeşil top varsa toplam kaç top vardır?", "option_a": "7", "option_b": "8", "option_c": "9", "option_d": "10", "correct_answer": "C"},
        
        # Problem Çözme - 2 soru
        {"grade": 4, "topic": "Problem Çözme", "question_text": "5 kalem, 3 silgi, 2 cetvel varsa toplam kaç eşya vardır?", "option_a": "8", "option_b": "9", "option_c": "10", "option_d": "11", "correct_answer": "C"},
        {"grade": 4, "topic": "Problem Çözme", "question_text": "6 kitap, 4 defter, 3 kalem varsa toplam kaç eşya vardır?", "option_a": "11", "option_b": "12", "option_c": "13", "option_d": "14", "correct_answer": "C"}
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