@echo off
echo ========================================
echo GMOD Workshop Manager - Environment Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/4] Python found:
python --version
echo.

REM Check if virtual environment already exists
if exist ".venv\" (
    echo [2/4] Virtual environment already exists, skipping creation...
) else (
    echo [2/4] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo [SUCCESS] Virtual environment created!
)
echo.

REM Activate virtual environment
echo [3/4] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment!
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment activated!
echo.

REM Check if requirements.txt exists, create if it doesn't
if not exist "requirements.txt" (
    echo [INFO] requirements.txt not found, creating it...
    (
        echo # Requirements for GMOD Workshop Manager
        echo pillow^>=9.0.0
    ) > requirements.txt
    echo [SUCCESS] requirements.txt created!
    echo.
)

REM Install dependencies
echo [4/4] Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo.

echo ========================================
echo [SUCCESS] Environment setup complete!
echo ========================================
echo.
echo To activate the environment manually, run:
echo     .venv\Scripts\activate.bat
echo.
echo To run the application, use:
echo     run.bat
echo.
pause
