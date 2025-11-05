# Batch Files Guide

Windows batch files for easy setup and running of GMOD Workshop Manager.

## Available Scripts

### 🔧 env.bat - Environment Setup

Automatically sets up your development environment.

**Usage:**
```cmd
env.bat
```

**What it does:**
1. ✅ Checks if Python is installed
2. ✅ Creates virtual environment (`.venv`)
3. ✅ Creates `requirements.txt` if missing
4. ✅ Installs all dependencies
5. ✅ Shows success message

**When to run:**
- First time setting up the project
- After cloning the repository
- If dependencies get corrupted
- When starting fresh

**Output:**
```
========================================
GMOD Workshop Manager - Environment Setup
========================================

[1/4] Python found:
Python 3.9.0

[2/4] Creating virtual environment...
[SUCCESS] Virtual environment created!

[3/4] Activating virtual environment...
[SUCCESS] Virtual environment activated!

[4/4] Installing dependencies from requirements.txt...
[SUCCESS] Dependencies installed!

========================================
[SUCCESS] Environment setup complete!
========================================
```

---

### 🚀 run.bat - Run Application

Starts the GMOD Workshop Manager GUI application.

**Usage:**
```cmd
run.bat
```

**What it does:**
1. ✅ Checks if virtual environment exists
2. ✅ Activates virtual environment
3. ✅ Verifies dependencies are installed
4. ✅ Launches the GUI application
5. ✅ Shows any errors that occur

**When to run:**
- Every time you want to use the application
- After running `env.bat` setup

**Output:**
```
========================================
GMOD Workshop Manager - Starting Application
========================================

[1/2] Activating virtual environment...
[SUCCESS] Virtual environment activated!

[2/2] Starting GMOD Workshop Manager...
========================================

[GUI window opens]
```

## 📋 Quick Workflow

### First Time Setup

```cmd
REM 1. Open Command Prompt in project folder
cd D:\Github\Garrys-Mod-Addon-Uploader

REM 2. Run environment setup (one time only)
env.bat

REM 3. Run the application
run.bat
```

### Daily Use

```cmd
REM Just run this each time
run.bat
```

### After Updates

```cmd
REM If new dependencies were added
env.bat

REM Then run normally
run.bat
```

## 🔍 Troubleshooting

### "Python is not installed or not in PATH"

**Problem:** Python not found

**Solution:**
1. Install Python from https://python.org
2. During installation, check "Add Python to PATH"
3. Restart Command Prompt
4. Run `env.bat` again

---

### "Virtual environment not found"

**Problem:** `.venv` folder doesn't exist

**Solution:**
```cmd
REM Run setup first
env.bat

REM Then run application
run.bat
```

---

### "Failed to create virtual environment"

**Problem:** Permission issues or disk space

**Solution:**
1. Run Command Prompt as Administrator
2. Ensure you have disk space
3. Check antivirus isn't blocking
4. Try: `python -m venv .venv` manually

---

### "Failed to install dependencies"

**Problem:** Network issues or pip problems

**Solution:**
```cmd
REM Upgrade pip first
.venv\Scripts\activate.bat
python -m pip install --upgrade pip

REM Then install requirements
pip install -r requirements.txt
```

---

### "Application exited with an error"

**Problem:** Python error in application

**Solution:**
1. Check error message in console
2. Verify config.json settings
3. Ensure GMOD tools paths are correct
4. Run manually to see full error:
   ```cmd
   .venv\Scripts\activate.bat
   python main.py
   ```

## 🎯 Advanced Usage

### Manual Virtual Environment Activation

```cmd
REM Activate environment manually
.venv\Scripts\activate.bat

REM Your prompt will change to show (.venv)

REM Run commands
python main.py
python scripts/createworkshop.py

REM Deactivate when done
deactivate
```

### Run Without Batch Files

```cmd
REM Create virtual environment
python -m venv .venv

REM Activate it
.venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Run application
python main.py
```

### Update Dependencies

```cmd
REM Activate environment
.venv\Scripts\activate.bat

REM Update all packages
pip install --upgrade -r requirements.txt

REM Or update specific package
pip install --upgrade pillow
```

### Clean Install

```cmd
REM Delete virtual environment
rmdir /s /q .venv

REM Run setup again
env.bat
```

## 📦 What Gets Created

When you run `env.bat`:

```
Garrys-Mod-Addon-Uploader/
├── .venv/                    # Virtual environment (created)
│   ├── Scripts/
│   │   ├── python.exe       # Isolated Python
│   │   ├── pip.exe          # Package installer
│   │   └── activate.bat     # Activation script
│   └── Lib/                 # Installed packages
├── requirements.txt          # Created if missing
├── env.bat                   # Setup script
└── run.bat                   # Run script
```

## 🔒 Virtual Environment Benefits

### Why Use Virtual Environment?

✅ **Isolation** - Dependencies don't affect system Python
✅ **Clean** - Easy to delete and recreate
✅ **Portable** - Share project without conflicts
✅ **Safe** - No admin rights needed for packages
✅ **Version Control** - `.venv` excluded from git

### Virtual Environment vs Global Install

| Aspect | Virtual Env (.venv) | Global Install |
|--------|---------------------|----------------|
| Location | Project folder | System-wide |
| Isolation | ✅ Yes | ❌ No |
| Conflicts | ✅ None | ⚠️ Possible |
| Admin Rights | ✅ Not needed | ⚠️ Often needed |
| Clean Remove | ✅ Delete folder | ❌ Complex |
| Best Practice | ✅ Recommended | ❌ Not ideal |

## 🎨 Customization

### Modify env.bat

Edit `env.bat` to:
- Change Python version check
- Add pre-install steps
- Configure environment variables
- Add post-install tasks

### Modify run.bat

Edit `run.bat` to:
- Add startup checks
- Set environment variables
- Run pre-launch scripts
- Change error handling

## 🐧 Linux/Mac Alternative

For Linux/Mac users, create similar shell scripts:

**setup.sh:**
```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**run.sh:**
```bash
#!/bin/bash
source .venv/bin/activate
python main.py
```

Make executable:
```bash
chmod +x setup.sh run.sh
```

## 📚 Related Documentation

- [Installation Guide](INSTALLATION.md) - Detailed setup
- [Usage Guide](USAGE.md) - How to use the app
- [QUICKSTART.md](QUICKSTART.md) - Quick reference

## ❓ FAQ

**Q: Do I need to run env.bat every time?**  
A: No, only once. Then use `run.bat` for daily use.

**Q: Can I delete .venv folder?**  
A: Yes, run `env.bat` again to recreate it.

**Q: Does this work on Windows 11?**  
A: Yes, works on Windows 7/8/10/11.

**Q: Can I use without batch files?**  
A: Yes, see "Manual Installation" in [Main README](../README.md).

**Q: What if I don't use virtual environment?**  
A: You can install globally with `pip install -r requirements.txt` but virtual environment is recommended.

## 🎉 Summary

**For 99% of users:**
1. Run `env.bat` once
2. Use `run.bat` always
3. Enjoy! 🎮

---

[← Back to Main README](../README.md)
