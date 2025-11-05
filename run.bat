@echo off
echo ========================================
echo GMOD Workshop Manager - Starting Application
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo [ERROR] Virtual environment not found!
    echo Please run env.bat first to set up the environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/2] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment!
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment activated!
echo.

REM Check if Pillow is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Dependencies may not be installed.
    echo Installing requirements...
    pip install -r requirements.txt
    echo.
)

REM Run the application
echo [2/2] Starting GMOD Workshop Manager...
echo ========================================
echo.
python main.py

REM Check if application exited with error
if errorlevel 1 (
    echo.
    echo ========================================
    echo [ERROR] Application exited with an error!
    echo ========================================
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Application closed.
echo ========================================
