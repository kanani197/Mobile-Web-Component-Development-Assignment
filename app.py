"""Main Flask application entry point."""
import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from config import config
from extensions import init_extensions, db
from models import User
from routes import auth, consultant, champion, governance, admin, search, main

def create_app(config_name=None):
    """Application factory."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    init_extensions(app)
    
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(consultant.bp)
    app.register_blueprint(champion.bp)
    app.register_blueprint(governance.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(search.bp)
    
    # Context processor for user
    @app.context_processor
    def inject_user():
        return {'current_user': current_user}
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403
    
    @app.errorhandler(500)
    def server_error(error):
        return render_template('errors/500.html'), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
