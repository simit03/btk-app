from flask import Blueprint, request, jsonify, session
from app.services.user_service import UserService
from app.database.question_repository import QuestionRepository
import uuid

api_bp = Blueprint('api', __name__)
user_service = UserService()
question_repo = QuestionRepository()

@api_bp.route('/register', methods=['POST'])
def register():
    """Kullanıcı kaydı"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        grade = data.get('grade')
        
        if not all([username, password, first_name, last_name, grade]):
            return jsonify({
                'success': False,
                'message': 'Tüm alanlar gereklidir!'
            }), 400
        
        result = user_service.create_new_user(username, password, first_name, last_name, grade)
        
        if result['success']:
            return jsonify({
                'success': True,
                'message': 'Kayıt başarılı! Giriş yapabilirsiniz.'
            })
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Kayıt hatası: {str(e)}'
        }), 500

@api_bp.route('/login', methods=['POST'])
def login():
    """Kullanıcı girişi"""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({
                'success': False,
                'message': 'Kullanıcı adı ve şifre gereklidir!'
            }), 400
        
        result = user_service.login_user(username, password)
        
        if result['success']:
            # Session'a kullanıcı bilgilerini kaydet
            session['logged_in'] = True
            session['user_id'] = result['data']['id']
            session['username'] = result['data']['username']
            session['first_name'] = result['data']['first_name']
            session['last_name'] = result['data']['last_name']
            session['grade'] = result['data']['grade']
            
            return jsonify({
                'success': True,
                'message': 'Giriş başarılı!',
                'redirect': '/'
            })
        else:
            return jsonify(result), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Giriş hatası: {str(e)}'
        }), 500

@api_bp.route('/profile/update', methods=['POST'])
def update_profile():
    """Profil güncelleme"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        grade = data.get('grade')
        user_id = session.get('user_id')
        
        if not all([first_name, last_name, grade, user_id]):
            return jsonify({
                'success': False,
                'message': 'Tüm alanlar gereklidir!'
            }), 400
        
        result = user_service.update_user_profile(user_id, first_name, last_name, grade)
        
        if result['success']:
            # Session'ı güncelle
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['grade'] = grade
            
            return jsonify({
                'success': True,
                'message': 'Profil güncellendi!'
            })
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Profil güncelleme hatası: {str(e)}'
        }), 500

@api_bp.route('/session/user', methods=['GET'])
def get_session_user():
    """Session kullanıcı bilgilerini getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        return jsonify({
            'success': True,
            'data': {
                'id': session.get('user_id'),
                'username': session.get('username'),
                'first_name': session.get('first_name'),
                'last_name': session.get('last_name'),
                'grade': session.get('grade')
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Session hatası: {str(e)}'
        }), 500

@api_bp.route('/quiz/questions', methods=['GET'])
def get_quiz_questions():
    """Quiz sorularını getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        grade = session.get('grade', 1)
        limit = request.args.get('limit', 20, type=int)
        
        # Kullanıcının sınıfına göre soruları getir
        questions = question_repo.get_questions_by_grade_with_topic_distribution(grade, limit)
        
        if not questions:
            return jsonify({
                'success': False,
                'message': 'Bu sınıf için soru bulunamadı!'
            }), 404
        
        # Soruları karıştır ve formatla
        import random
        random.shuffle(questions)
        
        formatted_questions = []
        for i, q in enumerate(questions[:limit]):
            # Şıkları karıştır
            options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
            correct_answer = q['correct_answer']
            correct_value = options[ord(correct_answer) - ord('A')]
            
            random.shuffle(options)
            
            # Yeni doğru cevabı bul
            new_correct_answer = chr(ord('A') + options.index(correct_value))
            
            formatted_questions.append({
                'id': q['id'],
                'number': i + 1,
                'question_text': q['question_text'],
                'topic': q['topic'],
                'options': {
                    'A': options[0],
                    'B': options[1],
                    'C': options[2],
                    'D': options[3]
                },
                'correct_answer': new_correct_answer
            })
        
        return jsonify({
            'success': True,
            'data': {
                'questions': formatted_questions,
                'total_questions': len(formatted_questions),
                'grade': grade
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Soru getirme hatası: {str(e)}'
        }), 500

@api_bp.route('/quiz/start', methods=['POST'])
def start_quiz():
    """Quiz oturumu başlat"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        grade = session.get('grade', 1)
        session_id = str(uuid.uuid4())
        
        # Quiz oturumu oluştur
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor()
            cursor.execute("""
                INSERT INTO quiz_sessions (id, user_id, grade, total_questions)
                VALUES (%s, %s, %s, %s)
            """, (session_id, user_id, grade, 20))
            db.connection.commit()
            cursor.close()
        
        return jsonify({
            'success': True,
            'data': {
                'session_id': session_id,
                'grade': grade
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Quiz başlatma hatası: {str(e)}'
        }), 500

@api_bp.route('/quiz/submit', methods=['POST'])
def submit_quiz_answer():
    """Quiz cevabını kaydet"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        data = request.get_json()
        user_id = session.get('user_id')
        question_id = data.get('question_id')
        user_answer = data.get('user_answer')
        is_correct = data.get('is_correct')
        session_id = data.get('session_id')
        
        # Cevabı kaydet
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor()
            cursor.execute("""
                INSERT INTO user_progress (user_id, question_id, user_answer, is_correct, quiz_session_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, question_id, user_answer, is_correct, session_id))
            db.connection.commit()
            cursor.close()
        
        return jsonify({
            'success': True,
            'message': 'Cevap kaydedildi!'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Cevap kaydetme hatası: {str(e)}'
        }), 500

@api_bp.route('/quiz/complete', methods=['POST'])
def complete_quiz():
    """Quiz'i tamamla"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        data = request.get_json()
        session_id = data.get('session_id')
        correct_answers = data.get('correct_answers', 0)
        total_questions = data.get('total_questions', 20)
        score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        user_id = session.get('user_id')
        
        # Quiz oturumunu güncelle
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor()
            cursor.execute("""
                UPDATE quiz_sessions 
                SET correct_answers = %s, score_percentage = %s, completed_at = NOW()
                WHERE id = %s
            """, (correct_answers, score_percentage, session_id))
            db.connection.commit()
            
            # Mükemmel skor kontrolü (tüm sorular doğru)
            achievement_earned = None
            if correct_answers == total_questions and total_questions > 0:
                # Mükemmel skor başarısını kontrol et
                cursor.execute("""
                    SELECT id FROM achievements 
                    WHERE user_id = %s AND achievement_type = 'perfect_score'
                """, (user_id,))
                
                if not cursor.fetchone():
                    # Yeni mükemmel skor başarısı ekle
                    cursor.execute("""
                        INSERT INTO achievements (user_id, achievement_type, achievement_name, achievement_description)
                        VALUES (%s, 'perfect_score', 'Mükemmel Skor', 'Tüm soruları doğru cevapladınız! 🏆')
                    """, (user_id,))
                    db.connection.commit()
                    achievement_earned = {
                        'type': 'perfect_score',
                        'name': 'Mükemmel Skor',
                        'description': 'Tüm soruları doğru cevapladınız! 🏆',
                        'icon': '🏆'
                    }
            
            cursor.close()
        
        return jsonify({
            'success': True,
            'data': {
                'score_percentage': score_percentage,
                'correct_answers': correct_answers,
                'total_questions': total_questions,
                'achievement_earned': achievement_earned
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Quiz tamamlama hatası: {str(e)}'
        }), 500

@api_bp.route('/achievements', methods=['GET'])
def get_user_achievements():
    """Kullanıcının başarılarını getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT achievement_type, achievement_name, achievement_description, earned_at
                FROM achievements 
                WHERE user_id = %s
                ORDER BY earned_at DESC
            """, (user_id,))
            
            achievements = cursor.fetchall()
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'achievements': achievements,
                    'total_achievements': len(achievements)
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Başarıları getirme hatası: {str(e)}'
        }), 500

@api_bp.route('/user/stats', methods=['GET'])
def get_user_stats():
    """Kullanıcının istatistiklerini getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            # Toplam çözülen soru sayısı
            cursor.execute("""
                SELECT COUNT(*) as total_questions
                FROM user_progress 
                WHERE user_id = %s
            """, (user_id,))
            total_questions = cursor.fetchone()['total_questions']
            
            # Doğru çözülen soru sayısı
            cursor.execute("""
                SELECT COUNT(*) as correct_questions
                FROM user_progress 
                WHERE user_id = %s AND is_correct = 1
            """, (user_id,))
            correct_questions = cursor.fetchone()['correct_questions']
            
            # Yanlış çözülen soru sayısı
            cursor.execute("""
                SELECT COUNT(*) as incorrect_questions
                FROM user_progress 
                WHERE user_id = %s AND is_correct = 0
            """, (user_id,))
            incorrect_questions = cursor.fetchone()['incorrect_questions']
            
            # Toplam puan (her soru 10 puan)
            total_points = correct_questions * 10
            
            # Kupa sayısı
            cursor.execute("""
                SELECT COUNT(*) as total_achievements
                FROM achievements 
                WHERE user_id = %s
            """, (user_id,))
            total_achievements = cursor.fetchone()['total_achievements']
            
            # Quiz tamamlanma sayısı
            cursor.execute("""
                SELECT COUNT(*) as completed_quizzes
                FROM quiz_sessions 
                WHERE user_id = %s AND completed_at IS NOT NULL
            """, (user_id,))
            completed_quizzes = cursor.fetchone()['completed_quizzes']
            
            # Başarı yüzdesi
            success_percentage = (correct_questions / total_questions * 100) if total_questions > 0 else 0
            
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'total_questions': total_questions,
                    'correct_questions': correct_questions,
                    'incorrect_questions': incorrect_questions,
                    'total_points': total_points,
                    'total_achievements': total_achievements,
                    'completed_quizzes': completed_quizzes,
                    'success_percentage': round(success_percentage, 1)
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'İstatistikleri getirme hatası: {str(e)}'
        }), 500

@api_bp.route('/progress/daily', methods=['GET'])
def get_daily_progress():
    """Günlük ilerleme verilerini getir"""
    try:
        print(f"DEBUG: get_daily_progress started")
        print(f"DEBUG: session data: {dict(session)}")
        
        if not session.get('logged_in'):
            print(f"DEBUG: User not logged in")
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        print(f"DEBUG: user_id = {user_id}")
        
        # Period parametresini al (varsayılan: 30 gün)
        period = request.args.get('period', 30, type=int)
        
        print(f"DEBUG: get_daily_progress called with user_id={user_id}, period={period}")
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        print(f"DEBUG: Database connection: {db.connection is not None}")
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            # Önce user_progress tablosunda veri var mı kontrol et
            cursor.execute("""
                SELECT COUNT(*) as total_records
                FROM user_progress 
                WHERE user_id = %s
            """, (user_id,))
            
            total_records = cursor.fetchone()['total_records']
            
            print(f"DEBUG: User {user_id} has {total_records} progress records")
            
            if total_records == 0:
                # Veri yoksa boş sonuç döndür (yeni kullanıcılar için)
                print(f"DEBUG: No progress data for user {user_id}, returning empty data")
                return jsonify({
                    'success': True,
                    'data': {
                        'daily_data': [],
                        'summary': {
                            'study_days': 0,
                            'average_daily': 0,
                            'most_active_day': None,
                            'total_study_time': 0
                        }
                    }
                })
            
            # Period'a göre günlük veri
            cursor.execute("""
                SELECT 
                    DATE(answered_at) as date,
                    COUNT(*) as solved,
                    SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as correct
                FROM user_progress 
                WHERE user_id = %s 
                AND answered_at >= DATE_SUB(NOW(), INTERVAL %s DAY)
                GROUP BY DATE(answered_at)
                ORDER BY date DESC
            """, (user_id, period))
            
            daily_data = cursor.fetchall()
            
            # Özet istatistikler
            cursor.execute("""
                SELECT 
                    COUNT(DISTINCT DATE(answered_at)) as study_days,
                    AVG(daily_solved) as average_daily
                FROM (
                    SELECT 
                        DATE(answered_at) as study_date,
                        COUNT(*) as daily_solved
                    FROM user_progress 
                    WHERE user_id = %s 
                    AND answered_at >= DATE_SUB(NOW(), INTERVAL %s DAY)
                    GROUP BY DATE(answered_at)
                ) as daily_stats
            """, (user_id, period))
            
            summary = cursor.fetchone()
            
            # Eğer veri yoksa varsayılan değerler
            if not summary:
                summary = {
                    'study_days': 0,
                    'average_daily': 0,
                    'most_active_day': None,
                    'total_study_time': 0
                }
            else:
                # En aktif gün
                cursor.execute("""
                    SELECT DATE(answered_at) as most_active_day
                    FROM user_progress 
                    WHERE user_id = %s 
                    AND answered_at >= DATE_SUB(NOW(), INTERVAL %s DAY)
                    GROUP BY DATE(answered_at)
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                """, (user_id, period))
                
                most_active = cursor.fetchone()
                summary['most_active_day'] = most_active['most_active_day'] if most_active else None
                
                # Toplam çalışma süresi (dakika cinsinden)
                cursor.execute("""
                    SELECT COUNT(*) as total_questions
                    FROM user_progress 
                    WHERE user_id = %s 
                    AND answered_at >= DATE_SUB(NOW(), INTERVAL %s DAY)
                """, (user_id, period))
                
                total_questions = cursor.fetchone()['total_questions']
                summary['total_study_time'] = total_questions * 2  # Her soru için 2 dakika varsayımı
            
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'daily_data': daily_data,
                    'summary': summary
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Günlük ilerleme hatası: {str(e)}'
        }), 500

@api_bp.route('/progress/topics', methods=['GET'])
def get_topic_performance():
    """Konu bazlı performans verilerini getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            # Önce user_progress tablosunda veri var mı kontrol et
            cursor.execute("""
                SELECT COUNT(*) as total_records
                FROM user_progress 
                WHERE user_id = %s
            """, (user_id,))
            
            total_records = cursor.fetchone()['total_records']
            
            if total_records == 0:
                # Veri yoksa boş sonuç döndür
                cursor.close()
                return jsonify({
                    'success': True,
                    'data': {
                        'topics': []
                    }
                })
            
            cursor.execute("""
                SELECT 
                    q.topic,
                    COUNT(*) as total_questions,
                    SUM(CASE WHEN up.is_correct = 1 THEN 1 ELSE 0 END) as correct_questions
                FROM user_progress up
                JOIN questions q ON up.question_id = q.id
                WHERE up.user_id = %s
                GROUP BY q.topic
                ORDER BY total_questions DESC
            """, (user_id,))
            
            topics = cursor.fetchall()
            
            # Konu isimlerini düzenle
            for topic in topics:
                topic['topic_name'] = topic['topic']
            
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'topics': topics
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Konu performans hatası: {str(e)}'
        }), 500

@api_bp.route('/progress/weekly', methods=['GET'])
def get_weekly_summary():
    """Haftalık özet verilerini getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            # Son 4 haftalık veri
            cursor.execute("""
                SELECT 
                    YEARWEEK(answered_at) as week_number,
                    MIN(DATE(answered_at)) as week_start,
                    MAX(DATE(answered_at)) as week_end,
                    COUNT(*) as total_questions,
                    SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as correct_questions,
                    SUM(CASE WHEN is_correct = 1 THEN 10 ELSE 0 END) as points_earned
                FROM user_progress 
                WHERE user_id = %s 
                AND answered_at >= DATE_SUB(NOW(), INTERVAL 4 WEEK)
                GROUP BY YEARWEEK(answered_at)
                ORDER BY week_number DESC
            """, (user_id,))
            
            weeks = cursor.fetchall()
            
            # Hafta bilgilerini düzenle
            for week in weeks:
                week['week_title'] = f"{week['week_start']} - {week['week_end']}"
                week['date_range'] = f"{week['week_start']} - {week['week_end']}"
            
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'weeks': weeks
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Haftalık özet hatası: {str(e)}'
        }), 500

@api_bp.route('/progress/detailed', methods=['GET'])
def get_detailed_progress():
    """Detaylı ilerleme tablosu verilerini getir"""
    try:
        if not session.get('logged_in'):
            return jsonify({
                'success': False,
                'message': 'Giriş yapmanız gerekiyor!'
            }), 401
        
        user_id = session.get('user_id')
        
        from app.database.db_connection import DatabaseConnection
        db = DatabaseConnection()
        
        if db.connection:
            cursor = db.connection.cursor(dictionary=True)
            
            # Günlük detaylı veriler
            cursor.execute("""
                SELECT 
                    DATE(up.answered_at) as date,
                    COUNT(*) as total_questions,
                    SUM(CASE WHEN up.is_correct = 1 THEN 1 ELSE 0 END) as correct_questions,
                    SUM(CASE WHEN up.is_correct = 0 THEN 1 ELSE 0 END) as incorrect_questions,
                    SUM(CASE WHEN up.is_correct = 1 THEN 10 ELSE 0 END) as points_earned
                FROM user_progress up
                WHERE up.user_id = %s
                GROUP BY DATE(up.answered_at)
                ORDER BY date DESC
                LIMIT 50
            """, (user_id,))
            
            records = cursor.fetchall()
            
            # Her gün için konular ve başarılar
            for record in records:
                # Konular
                cursor.execute("""
                    SELECT DISTINCT q.topic
                    FROM user_progress up
                    JOIN questions q ON up.question_id = q.id
                    WHERE up.user_id = %s AND DATE(up.answered_at) = %s
                """, (user_id, record['date']))
                
                topics = [row['topic'] for row in cursor.fetchall()]
                record['topics'] = topics
                
                # Başarılar
                cursor.execute("""
                    SELECT a.achievement_name
                    FROM achievements a
                    WHERE a.user_id = %s AND DATE(a.earned_at) = %s
                """, (user_id, record['date']))
                
                achievements = [row['achievement_name'] for row in cursor.fetchall()]
                record['achievements'] = achievements
            
            cursor.close()
            
            return jsonify({
                'success': True,
                'data': {
                    'daily_data': records
                }
            })
        
        return jsonify({
            'success': False,
            'message': 'Veritabanı bağlantı hatası'
        }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Detaylı ilerleme hatası: {str(e)}'
        }), 500