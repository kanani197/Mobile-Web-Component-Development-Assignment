@echo off
REM DKN System Startup Script

echo ============================================
echo   Digital Knowledge Network System
echo ============================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Initialize database
echo Initializing database...
python -c "from app import create_app; from extensions import db; app = create_app(); ctx = app.app_context(); ctx.push(); db.create_all(); print('Database initialized!')"

REM Create sample data
echo.
echo Do you want to create sample data? (y/n)
set /p create_sample=Enter choice: 
if /i "%create_sample%"=="y" (
    echo Creating sample data...
    python seed_data.py
    echo.
    echo Test users created:
    echo - consultant / password123
    echo - champion / password123
    echo - governance / password123
    echo - admin / password123
)

REM Run the application
echo.
echo ============================================
echo   Starting DKN System...
echo ============================================
echo.
echo Access the application at: http://localhost:5000
echo.
python app.py

pause
