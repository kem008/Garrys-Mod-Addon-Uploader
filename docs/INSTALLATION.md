# Installation Guide

Complete guide to installing and setting up GMOD Workshop Manager.

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 7/8/10/11
- **Python**: 3.7 or higher
- **RAM**: 512 MB
- **Disk Space**: 50 MB (plus space for your addons)
- **Internet**: Required for Workshop uploads

### Required Software
- **Garry's Mod**: Must be installed via Steam
- **Steam Client**: Must be running when publishing/updating
- **Python 3.7+**: [Download here](https://www.python.org/downloads/)

## Step-by-Step Installation

### 1. Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```bash
   python --version
   ```

### 2. Download GMOD Workshop Manager

**Option A: Clone with Git**
```bash
git clone https://github.com/yourusername/Garrys-Mod-Addon-Uploader.git
cd Garrys-Mod-Addon-Uploader
```

**Option B: Download ZIP**
1. Download the ZIP file from GitHub
2. Extract to your desired location
3. Open command prompt/terminal in that folder

### 3. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- **Pillow** - For image generation and manipulation

### 4. First Run Configuration

1. **Launch the application:**
   ```bash
   python main.py
   ```

2. **Configure Settings:**
   - Click the **"Settings"** tab
   - Set the paths to GMOD tools

3. **Find GMOD Tools:**

   Default Steam installation:
   ```
   GMAD.exe:
   C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe
   
   GMPUBLISH.exe:
   C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe
   ```

   If Steam is in a different location, browse to:
   ```
   [Steam Install Location]\steamapps\common\GarrysMod\bin\
   ```

4. **Set Base Addons Path:**
   - Choose where you keep your addon development folders
   - Example: `D:\Projects\GMOD\Addons`

5. **Save Settings:**
   - Click **"Save Settings"** button
   - Settings are stored in `config.json`

## Verification

### Test the Installation

1. **Check Python:**
   ```bash
   python --version
   # Should show: Python 3.7.x or higher
   ```

2. **Check Dependencies:**
   ```bash
   pip show pillow
   # Should display package information
   ```

3. **Launch GUI:**
   ```bash
   python main.py
   # Should open the application window
   ```

4. **Verify GMOD Tools:**
   - Open Settings tab
   - Paths should point to existing files
   - If not, browse to correct locations

## Troubleshooting Installation

### Python Not Found

**Error:** `'python' is not recognized as an internal or external command`

**Solution:**
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to PATH:
   - Windows: System Properties → Environment Variables → PATH
   - Add: `C:\Python3X\` and `C:\Python3X\Scripts\`

### Pip Not Found

**Solution:**
```bash
python -m ensurepip --upgrade
```

### Pillow Installation Fails

**Solution:**
```bash
pip install --upgrade pip
pip install pillow --upgrade
```

### Can't Find gmad.exe or gmpublish.exe

**Solution:**
1. Open Steam
2. Right-click Garry's Mod → Properties
3. Local Files → Browse
4. Navigate to `bin` folder
5. Copy the full path to gmad.exe and gmpublish.exe

### Application Won't Start

**Check:**
1. Python version: `python --version`
2. Required packages: `pip list`
3. Error messages in console
4. Try running: `python -m src.gui.main`

## Alternative Installation Methods

### Using Virtual Environment (Recommended for Developers)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Portable Installation

Create a portable version:

1. Install Python portable edition
2. Copy GMOD Workshop Manager folder
3. Install dependencies to local folder:
   ```bash
   pip install -r requirements.txt --target=./lib
   ```
4. Modify `main.py` to add `lib` to Python path

## Updating

### Update to Latest Version

```bash
# If using Git
git pull origin main

# Or download new ZIP and replace files

# Update dependencies
pip install -r requirements.txt --upgrade
```

## Uninstallation

### Remove Application

1. Delete the application folder
2. Delete `config.json` if present
3. (Optional) Uninstall Python packages:
   ```bash
   pip uninstall pillow
   ```

## Next Steps

After successful installation:

1. **Read [Usage Guide](USAGE.md)** - Learn how to use the application
2. **Check [addon.json Reference](ADDON_JSON.md)** - Understand addon configuration
3. **Try the examples** - Test with sample addon

## Getting Help

If you encounter issues:

1. Check [Troubleshooting section](#troubleshooting-installation)
2. Read the error message carefully
3. Check GitHub Issues
4. Create a new issue with:
   - Python version
   - Operating system
   - Error message
   - Steps to reproduce

---

[← Back to README](../README.md) | [Next: Usage Guide →](USAGE.md)
