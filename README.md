# Digital Knowledge Network (DKN) System

A Flask-based web application for managing, validating, and discovering organizational knowledge assets with AI-powered recommendations.

## Features

- **User Authentication & Authorization**
  - Multiple user roles: Consultant, Champion, Admin, Governance
  - Secure password hashing with bcrypt
  - Session management with Flask-Login

- **Knowledge Asset Management**
  - Upload and store knowledge assets (PDF, DOCX, XLSX, etc.)
  - Automatic text extraction from files
  - AI-powered tag suggestions using TF-IDF
  - Asset metadata and relationships

- **Validation Workflow**
  - Champions review and validate assets
  - Governance compliance review
  - Multi-stage approval process
  - Audit logging for compliance

- **Search & Discovery**
  - Full-text search of published assets
  - Filter by tags, file type, uploader
  - Advanced search with multiple criteria
  - Related assets recommendations

- **Admin & Governance**
  - User management and role assignment
  - System reports and analytics
  - Comprehensive audit logs
  - Compliance tracking

- **Workspace Collaboration**
  - Create and manage team workspaces
  - Add/remove members with roles
  - Collaborative asset organization

## Technology Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate
- **Database**: SQLite (configurable)
- **Authentication**: bcrypt, PyJWT
- **AI/ML**: scikit-learn, NLTK, sentence-transformers
- **File Handling**: PyPDF2, python-docx, openpyxl
- **Frontend**: Bootstrap 5, JavaScript
- **Testing**: pytest, pytest-flask
- **Other**: WTForms, Pillow, Werkzeug

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. **Clone the repository** (or extract the provided files)
```bash
cd dkn_system
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Initialize database**
```bash
python
>>> from app import create_app
>>> from extensions import db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

5. **Create seed data (optional)**
```bash
python -c "from seed_data import create_sample_data; create_sample_data()"
```

6. **Run the application**
```bash
python app.py
```

Access the application at `http://localhost:5000`

## Default Test Users

After running seed data:
- **Consultant**: `consultant` / `password123`
- **Champion**: `champion` / `password123`
- **Governance**: `governance` / `password123`
- **Admin**: `admin` / `password123`

## Project Structure

```
dkn_system/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── extensions.py         # Flask extensions initialization
├── requirements.txt      # Python dependencies
├── models/              # Database models
│   ├── user.py
│   ├── knowledge_asset.py
│   ├── metadata.py
│   ├── workspace.py
│   ├── audit.py
│   └── expertise.py
├── services/            # Business logic
│   ├── recommendation_engine.py
│   ├── upload_service.py
│   ├── validation_service.py
│   ├── search_service.py
│   ├── audit_service.py
│   └── notification_service.py
├── routes/              # API endpoints
│   ├── auth.py
│   ├── main.py
│   ├── consultant.py
│   ├── champion.py
│   ├── governance.py
│   ├── admin.py
│   └── search.py
├── templates/           # HTML templates
├── static/              # CSS, JavaScript, images
├── utils/               # Utility functions
│   ├── decorators.py
│   └── file_handler.py
├── tests/               # Unit and integration tests
└── uploads/             # Uploaded files directory
```

## User Roles & Permissions

### Consultant
- Upload knowledge assets
- View own assets
- Search published assets
- Manage personal workspaces
- View asset validation feedback

### Champion (Knowledge Champion)
- View pending assets for validation
- Approve/reject assets
- Send assets to governance
- View validation statistics

### Governance
- Review assets pending governance
- Approve/reject for compliance
- View audit logs
- Generate compliance reports

### Admin
- Manage system users
- Assign/modify user roles
- View system reports
- Access all system features

## Key Workflows

### Asset Upload & Publication
1. Consultant uploads asset
2. System extracts text and suggests tags
3. Champion reviews and validates
4. Asset sent to Governance (if required)
5. Governance approves for compliance
6. Asset published and discoverable

### Asset Search
1. User searches by keyword
2. System returns published assets
3. User filters by tags/type
4. Asset views and downloads tracked
5. Audit log records activity

### User Management
1. New user registers
2. Admin assigns role
3. User gains role-specific permissions
4. Activity logged in audit trail

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/logout` - Logout user

### Consultant
- `GET /consultant/dashboard` - View consultant dashboard
- `POST /consultant/upload` - Upload asset
- `GET /consultant/asset/<id>` - View asset details
- `POST /consultant/asset/<id>/delete` - Delete asset
- `GET /consultant/asset/<id>/download` - Download asset

### Champion
- `GET /champion/dashboard` - View pending validations
- `POST /champion/validate/<id>` - Validate asset
- `GET /champion/pending` - View all pending assets

### Governance
- `GET /governance/dashboard` - View governance dashboard
- `POST /governance/review/<id>` - Review asset
- `GET /governance/audit-logs` - View audit logs

### Admin
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/users` - Manage users
- `POST /admin/user/<id>/edit` - Edit user
- `GET /admin/reports` - View reports

### Search
- `GET /search/` - Search published assets
- `GET /search/advanced` - Advanced search
- `GET /search/asset/<id>` - View asset details

## Testing

Run tests with pytest:
```bash
pytest
# With coverage
pytest --cov=. --cov-report=html
```

## Configuration

Edit `config.py` to customize:
- Database URI
- Upload folder location
- Max file size
- Pagination settings
- AI/ML parameters

## Deployment

For production deployment:
1. Set environment variables
2. Use production config
3. Use secure database (PostgreSQL recommended)
4. Deploy with gunicorn/waitress
5. Set up HTTPS/SSL
6. Configure reverse proxy (nginx)

## Troubleshooting

**Database issues:**
```bash
# Reset database
rm instance/dkn_system.db
python app.py
```

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**File upload issues:**
- Check `uploads/` folder permissions
- Verify file size is under 50MB limit
- Ensure file type is in allowed list

## Future Enhancements

- Email notifications
- Advanced search with Elasticsearch
- Machine learning recommendations
- Workflow automation
- Mobile app
- API rate limiting
- Two-factor authentication

## Contributing

1. Create feature branch
2. Make changes
3. Add tests
4. Submit pull request

## License

Proprietary - Digital Knowledge Network System

## Support

For issues or questions, contact the development team.

---

**Last Updated**: January 2026
