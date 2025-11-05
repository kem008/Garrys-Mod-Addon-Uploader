# GMOD Workshop Manager GUI

A modern GUI application for managing Garry's Mod Workshop addons - create, publish, and update addons with ease!

## Features

✨ **4 Powerful Tabs:**
1. **Create & Publish** - Create GMA and publish new addons to Workshop
2. **Update Addon** - Update existing Workshop items
3. **addon.json Editor** - Edit addon metadata with a visual interface
4. **Settings** - Configure paths to GMOD tools

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- Garry's Mod installed with Workshop tools (`gmad.exe` and `gmpublish.exe`)
- Steam account and Garry's Mod ownership

## Installation

1. Install Python dependencies:
```bash
pip install pillow
```

2. Run the GUI:
```bash
python gmod_workshop_gui.py
```

## Quick Start

### Publishing a New Addon

1. Go to **"Create & Publish"** tab
2. Click **Browse** to select your addon folder
3. Click **Browse** to select your workshop image (pic.jpg)
4. Click **"Create & Publish"** button
5. Steam will open - fill in description, tags, and publish!

### Updating an Existing Addon

1. Go to **"Update Addon"** tab
2. Select your addon folder
3. Enter your Workshop ID (found in the addon's Steam Workshop URL)
4. Click **"Update Workshop"**

### Creating addon.json

1. Go to **"addon.json Editor"** tab
2. Select your addon folder
3. Fill in:
   - **Title**: Your addon name
   - **Type**: gamemode, map, weapon, vehicle, npc, tool, effects, model, entity, or other
   - **Tags**: Comma-separated (e.g., fun, roleplay, realism)
   - **Ignore Patterns**: Files to exclude from GMA
4. Click **"Save addon.json"**

## addon.json Basics

The `addon.json` file is required in your addon folder. Here's what each field means:

```json
{
    "title": "My Awesome Addon",
    "type": "gamemode",
    "tags": ["fun", "roleplay"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.bat",
        "*.psd"
    ]
}
```

### Field Descriptions:

- **title** (string): Display name of your addon
- **type** (string): Addon category
  - Common types: `gamemode`, `map`, `weapon`, `vehicle`, `npc`, `tool`, `effects`, `model`, `entity`
- **tags** (array): Workshop tags for discoverability
  - Popular tags: `fun`, `roleplay`, `realism`, `cartoon`, `scenic`, `combat`
- **ignore** (array): File patterns to exclude from the GMA package
  - Use wildcards: `*.txt`, `*.psd`, `.git/*`
  - Recommended to exclude: source files, documentation, development tools

## Workshop Image Requirements

- **Format**: JPG (JPEG)
- **Recommended Size**: 512x512 pixels
- **Max File Size**: 1 MB
- **Filename**: `pic.jpg` (place in addon root folder)

Use the included `create_workshop_image.py` to generate a placeholder:
```bash
python create_workshop_image.py
```

## Configuration

On first run, configure paths in the **Settings** tab:

- **GMAD.exe Path**: Usually `C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe`
- **GMPUBLISH.exe Path**: Usually `C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe`
- **Base Addons Path**: Your addons development folder

Settings are saved in `config.json` for future use.

## Folder Structure Example

```
MyAddon/
├── addon.json          (Required - addon metadata)
├── pic.jpg            (Required for publishing - workshop image)
├── lua/
│   └── autorun/
│       └── init.lua
├── materials/
├── models/
└── sound/
```

## Common Issues

### "gmad.exe not found"
- Go to Settings tab and browse to your Garry's Mod installation
- Default: `C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\`

### "Failed to create GMA"
- Ensure `addon.json` exists in your addon folder
- Check that addon.json is valid JSON
- Verify folder contains valid GMOD addon structure

### "Failed to publish"
- Ensure Steam is running and you're logged in
- Verify `pic.jpg` exists and is valid JPG format
- Check that you own Garry's Mod on Steam

## Tips

- **Always test locally** before publishing to Workshop
- Use descriptive titles and tags for better discoverability
- Keep your workshop image professional and relevant
- Read Steam Workshop rules before publishing
- Update changelog when updating existing addons

## Original Scripts

This GUI is based on the original Python scripts:
- `createworkshop.py` - Create and publish addons
- `updateworkshop.py` - Update existing addons

The GUI provides a more user-friendly interface with the same functionality!

## License

Free to use and modify for Garry's Mod addon development.

---

**Happy Modding! 🎮**
