from flask import Flask, render_template
from config import Config
from app.database.db_connection import DatabaseConnection
import os

def create_app(config_class=Config):
    """Create and configure the Flask application."""
    # Get the directory where main.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'app', 'templates')
    static_dir = os.path.join(base_dir, 'app', 'static')
    app = Flask(__name__, 
               template_folder=template_dir,
               static_folder=static_dir,
               static_url_path='/static')
    app.config.from_object(config_class)
    
    # Session secret key
    app.secret_key = 'your-secret-key-here'  # Production'da güvenli bir key kullanın
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        app.logger.error(f"Failed to create instance directory: {e}")
    
    # Initialize database
    db_connection = None
    try:
        # Create database connection
        db_connection = DatabaseConnection()
        
        # Store the database connection in the app context
        app.config['DB_CONNECTION'] = db_connection
        
        app.logger.info("Database initialized successfully")
    except Exception as e:
        app.logger.error(f"Failed to initialize database: {e}")
        if db_connection:
            db_connection.close()
        # Don't raise the exception, just log it for now
        # raise
    
    # Register blueprints
    try:
        from app.routes import api_bp, pages_bp
        
        app.register_blueprint(api_bp, url_prefix='/api')
        app.register_blueprint(pages_bp)
        app.logger.info("Blueprints registered successfully")
    except ImportError as e:
        app.logger.error(f"Failed to import blueprints: {e}")
        raise
    except Exception as e:
        app.logger.error(f"Failed to register blueprints: {e}")
        raise
    
    return app

# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)