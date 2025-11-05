# Quick Reference Guide

Fast reference for common tasks and commands.

## 🚀 Quick Start

### Windows (Recommended)
```cmd
# First time setup
env.bat

# Run application
run.bat
```

### Manual / Cross-Platform
```bash
# Install
pip install -r requirements.txt

# Run GUI
python main.py

# Run CLI scripts
cd scripts
python createworkshop.py
```

## 📁 Project Structure

```
├── main.py              # Run this to start GUI
├── src/                 # Source code
│   ├── core/           # Core functionality
│   ├── gui/            # GUI components
│   └── utils/          # Utilities
├── scripts/            # CLI scripts
├── docs/               # Documentation
├── assets/             # Images, etc.
└── examples/           # Example addons
```

## 🎯 Common Tasks

### Publish New Addon
1. Create `addon.json` in addon folder
2. Create `pic.jpg` (512x512)
3. Run GUI → "Create & Publish" tab
4. Select folder and image
5. Click "Create & Publish"

### Update Existing Addon
1. Make changes to addon
2. Run GUI → "Update Addon" tab
3. Select folder
4. Enter Workshop ID
5. Click "Update Workshop"

### Create addon.json
1. Run GUI → "addon.json Editor" tab
2. Select folder
3. Fill in details
4. Click "Save addon.json"

### Generate Workshop Image
```bash
cd scripts
python create_workshop_image.py
```

## ⌨️ Command Line

### Create and Publish
```bash
cd scripts
python createworkshop.py
# Enter addon folder name
```

### Update Addon
```bash
cd scripts
python updateworkshop.py
# Enter addon folder name
# Enter Workshop ID
```

## 📝 addon.json Template

```json
{
    "title": "Addon Name",
    "type": "gamemode",
    "tags": ["fun", "roleplay"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.psd",
        "*.bat"
    ]
}
```

### Valid Types
`gamemode`, `map`, `weapon`, `vehicle`, `npc`, `tool`, `effects`, `model`, `entity`, `other`

### Popular Tags
`fun`, `roleplay`, `realism`, `cartoon`, `scenic`, `combat`, `build`

## 🔧 Configuration

### Settings Location
```
config.json  (in project root)
```

### Default Paths
```
gmad.exe:
C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe

gmpublish.exe:
C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe
```

## 🐍 Python API

### Basic Usage
```python
from src.core import Config, WorkshopManager, AddonJSON

# Config
config = Config()
gmad_path = config.get('gmad_path')

# Workshop Manager
manager = WorkshopManager(gmad_path, gmpublish_path)
success, messages = manager.create_and_publish(folder, image)

# addon.json
addon = AddonJSON()
addon.set_title("My Addon")
addon.set_type("gamemode")
addon.set_tags(["fun", "roleplay"])
addon.save(folder)
```

## 🖼️ Workshop Image

### Requirements
- Format: JPEG (.jpg)
- Size: 512x512 pixels
- Max: 1 MB
- Name: pic.jpg

### Quick Generate
```bash
python scripts/create_workshop_image.py
```

## 🆘 Troubleshooting

### "gmad.exe not found"
→ Go to Settings tab and set correct path

### "Failed to create GMA"
→ Check addon.json exists and is valid JSON

### "Failed to publish"
→ Ensure Steam is running and pic.jpg exists

### "Workshop ID invalid"
→ Use numbers only from Workshop URL

## 📚 Full Documentation

- [Installation](docs/INSTALLATION.md) - Setup guide
- [Usage](docs/USAGE.md) - User guide
- [addon.json](docs/ADDON_JSON.md) - Config reference
- [API](docs/API.md) - Developer reference

## 🔗 File Extensions

| Extension | Description |
|-----------|-------------|
| `.lua` | Lua script files |
| `.vmt` | Material definition |
| `.vtf` | Texture file |
| `.mdl` | Model file |
| `.vtx` | Model vertex data |
| `.vvd` | Model vertex data |
| `.phy` | Physics data |
| `.pcf` | Particle effects |
| `.wav/.mp3` | Audio files |
| `.gma` | Garry's Mod Addon |

## ⚡ Keyboard Shortcuts

In GUI:
- `Ctrl+Tab` - Switch tabs
- `Ctrl+S` - Save (when in editor)
- `F5` - Refresh (if applicable)

## 🎓 Learning Resources

### Official
- GMOD Wiki: https://wiki.facepunch.com/gmod/
- Lua Reference: https://www.lua.org/manual/5.1/

### Community
- Facepunch Forums
- /r/gmod subreddit
- GMOD Discord servers

## 📊 Addon Structure Examples

### Minimal
```
MyAddon/
├── addon.json
├── pic.jpg
└── lua/
    └── autorun/
        └── init.lua
```

### Gamemode
```
MyGamemode/
├── addon.json
├── pic.jpg
└── gamemodes/
    └── mygm/
        ├── gamemode/
        │   ├── init.lua
        │   ├── cl_init.lua
        │   └── shared.lua
        └── mygm.txt
```

### Weapon
```
MyWeapon/
├── addon.json
├── pic.jpg
└── lua/
    └── weapons/
        └── weapon_mygun/
            └── shared.lua
```

## 🔍 Finding Workshop ID

Your Workshop ID is in the URL:
```
https://steamcommunity.com/sharedfiles/filedetails/?id=1234567890
                                                          ^^^^^^^^^^
                                                       Workshop ID
```

## ⚙️ Environment Variables

Optional environment variables:
```bash
# Windows
set GMOD_WORKSHOP_PATH=D:\Addons
set GMOD_TOOLS_PATH=C:\...\GarrysMod\bin

# Linux/Mac
export GMOD_WORKSHOP_PATH="/path/to/addons"
export GMOD_TOOLS_PATH="/path/to/gmod/bin"
```

## 💾 Backup

Before updates:
```bash
# Backup addon
xcopy MyAddon MyAddon_backup /E /I

# Backup GMA
copy MyAddon.gma MyAddon_backup.gma
```

## 🎯 Checklist: Before Publishing

- [ ] Tested locally in GMOD
- [ ] addon.json exists and is valid
- [ ] pic.jpg created (512x512)
- [ ] No console errors
- [ ] All required files included
- [ ] Development files excluded
- [ ] Description written
- [ ] Screenshots/videos ready

---

**Quick Links:**
[Main README](../README.md) | [Installation](INSTALLATION.md) | [Full Usage](USAGE.md) | [API](API.md)
