"""Create initial database and tables."""
from app import create_app
from extensions import db

def init_db():
    """Initialize database."""
    app = create_app()
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
