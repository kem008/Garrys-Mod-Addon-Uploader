# Scripts Directory

Legacy and utility scripts for GMOD Workshop management.

## Available Scripts

### createworkshop.py
Original CLI script for creating and publishing new addons to Workshop.

**Usage:**
```bash
cd scripts
python createworkshop.py
```

**Prompts:**
- Addon folder name
- Automatically creates GMA
- Opens Steam Workshop for publishing

**Features:**
- Simple command-line interface
- Auto-detects pic.jpg in addon folder
- Suitable for automation and scripting

---

### updateworkshop.py
Original CLI script for updating existing Workshop addons.

**Usage:**
```bash
cd scripts
python updateworkshop.py
```

**Prompts:**
- Addon folder name
- Workshop ID
- Creates GMA and updates Workshop item

**Features:**
- Quick updates from command line
- No GUI required
- Good for batch scripts

---

### create_workshop_image.py
Generates placeholder workshop images (pic.jpg).

**Usage:**
```bash
cd scripts
python create_workshop_image.py
```

**Output:**
- Creates `pic.jpg` in current directory
- 512x512 pixels
- Steam-styled template

**Features:**
- Generates professional-looking placeholders
- Customizable text (edit script)
- No external image editor needed

## Migration from Scripts to GUI

The GUI application provides a more user-friendly interface with the same functionality:

| Script | GUI Equivalent |
|--------|---------------|
| `createworkshop.py` | "Create & Publish" tab |
| `updateworkshop.py` | "Update Addon" tab |
| `create_workshop_image.py` | Integrated image tools |

## When to Use Scripts vs GUI

### Use Scripts When:
- ✅ Automating builds
- ✅ Batch processing multiple addons
- ✅ Integrating into CI/CD pipelines
- ✅ Running on headless servers
- ✅ Quick one-off operations

### Use GUI When:
- ✅ Interactive development
- ✅ Managing multiple projects
- ✅ Editing addon.json
- ✅ First-time users
- ✅ Visual feedback needed

## Automation Example

Create a batch file or shell script:

**Windows (batch.bat):**
```batch
@echo off
cd scripts
echo Publishing addon...
python createworkshop.py
pause
```

**Linux/Mac (publish.sh):**
```bash
#!/bin/bash
cd scripts
echo "Publishing addon..."
python3 createworkshop.py
```

## Configuration

Scripts read from the same `config.json` as the GUI application, but have hardcoded paths as fallback:

```python
gmad_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe"
gmpublish_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe"
base_path = r"D:\Steam\GarrysMod\Garrys-Mod-Addon-Uploader"
```

Edit these paths in the script files if needed.

## Advanced Usage

### Custom Script Example

```python
import subprocess
import os

# Paths
gmad_path = r"C:\...\gmad.exe"
gmpublish_path = r"C:\...\gmpublish.exe"

# Your addon
addon_folder = "D:\\Addons\\MyAddon"
output_gma = "D:\\Addons\\MyAddon.gma"
pic_path = "D:\\Addons\\MyAddon\\pic.jpg"

# Create GMA
subprocess.run([gmad_path, "create", "-folder", addon_folder, "-out", output_gma])

# Publish
subprocess.run([gmpublish_path, "create", "-addon", output_gma, "-icon", pic_path])
```

## Requirements

All scripts require:
- Python 3.7+
- Pillow (for create_workshop_image.py)
- GMOD installed with Workshop tools

Install dependencies:
```bash
pip install -r ../requirements.txt
```

## Troubleshooting

### Script Errors

**"gmad.exe not found"**
- Edit paths in script
- Or use config.json

**"pic.jpg not found"**
- Create pic.jpg in addon folder
- Or use create_workshop_image.py

**"Permission denied"**
- Run as administrator (Windows)
- Check file permissions (Linux/Mac)

## Documentation

For more information:
- [Installation Guide](../docs/INSTALLATION.md)
- [Usage Guide](../docs/USAGE.md)
- [API Documentation](../docs/API.md)
