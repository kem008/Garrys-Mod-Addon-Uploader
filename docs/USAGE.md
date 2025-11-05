# Usage Guide

Comprehensive guide to using GMOD Workshop Manager for creating, publishing, and updating addons.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Creating a New Addon](#creating-a-new-addon)
3. [Publishing to Workshop](#publishing-to-workshop)
4. [Updating Existing Addon](#updating-existing-addon)
5. [Managing addon.json](#managing-addonjson)
6. [Workshop Images](#workshop-images)
7. [Command Line Usage](#command-line-usage)
8. [Best Practices](#best-practices)

## Getting Started

### Launch the Application

```bash
python main.py
```

The application window will open with four tabs:
- **Create & Publish** - For new addons
- **Update Addon** - For updating existing Workshop items
- **addon.json Editor** - For managing addon metadata
- **Settings** - For configuring application paths

### Initial Setup

1. Go to **Settings** tab
2. Configure paths to GMOD tools (see [Installation Guide](INSTALLATION.md))
3. Save settings

## Creating a New Addon

### Prepare Your Addon

1. **Create addon folder structure:**
   ```
   MyAddon/
   ├── addon.json          (Required)
   ├── pic.jpg            (Required for publishing)
   ├── lua/
   │   └── autorun/
   │       └── init.lua
   ├── materials/
   ├── models/
   └── sound/
   ```

2. **Create addon.json** (see [addon.json Reference](ADDON_JSON.md))
3. **Create workshop image** (512x512 JPG)

### Using the GUI

1. **Go to "addon.json Editor" tab:**
   - Select your addon folder
   - Fill in title, type, tags
   - Set ignore patterns
   - Click "Save addon.json"

2. **Create workshop image:**
   - Use external tool or run: `python scripts/create_workshop_image.py`
   - Save as `pic.jpg` in addon folder
   - Recommended size: 512x512 pixels

## Publishing to Workshop

### Method 1: GUI (Recommended)

1. **Open "Create & Publish" tab**

2. **Select addon folder:**
   - Click "Browse" next to "Addon Folder"
   - Navigate to your addon folder
   - Click "Select Folder"

3. **Select workshop image:**
   - Click "Browse" next to "Image"
   - Select your `pic.jpg` file
   - Or let it auto-detect if in addon folder

4. **Publish:**
   - Click **"Create & Publish"** button
   - Watch the output console for progress
   - Steam will open for final details

5. **Complete in Steam:**
   - Add description
   - Set visibility (Public/Friends/Private)
   - Add additional tags
   - Click "Publish"

### Method 2: Command Line

```bash
cd scripts
python createworkshop.py
```

Follow the prompts:
1. Enter addon folder name
2. Script will create GMA and open Steam

### Create GMA Only

If you want to create the GMA file without publishing:

1. Go to "Create & Publish" tab
2. Select addon folder
3. Click **"Create GMA Only"**
4. GMA file will be created in parent directory

## Updating Existing Addon

### Find Your Workshop ID

Your Workshop ID is in the URL of your addon page:
```
https://steamcommunity.com/sharedfiles/filedetails/?id=1234567890
                                                          ^^^^^^^^^^
                                                       Workshop ID
```

### Update via GUI

1. **Go to "Update Addon" tab**

2. **Select addon folder:**
   - Click "Browse"
   - Select your updated addon folder

3. **Enter Workshop ID:**
   - Paste your Workshop ID (numbers only)

4. **Add changelog (optional):**
   - Type changes in the changelog box
   - This is for your reference only

5. **Update:**
   - Click **"Update Workshop"** button
   - Watch progress in output console
   - Wait for success message

### Update via Command Line

```bash
cd scripts
python updateworkshop.py
```

Enter:
1. Addon folder name
2. Workshop ID

## Managing addon.json

### Using the Editor

1. **Go to "addon.json Editor" tab**

2. **Load existing addon.json:**
   - Click "Browse" to select folder
   - Click "Load"
   - Existing values will populate

3. **Edit fields:**
   - **Title**: Display name of your addon
   - **Type**: Select from dropdown
   - **Tags**: Comma-separated list
   - **Ignore**: File patterns to exclude

4. **Validate:**
   - Click "Validate" to check for errors
   - Fix any issues shown

5. **Save:**
   - Click "Save addon.json"
   - File is written to addon folder

### Common Types

- `gamemode` - Custom game modes
- `map` - Custom maps
- `weapon` - Weapons
- `vehicle` - Vehicles
- `npc` - NPCs and entities
- `tool` - Tools
- `effects` - Visual/sound effects
- `model` - 3D models
- `entity` - Entities

### Common Tags

- `fun` - Fun/casual content
- `roleplay` - Roleplay content
- `realism` - Realistic content
- `cartoon` - Cartoony style
- `scenic` - Scenic maps
- `combat` - Combat focused
- `building` - Building focused

## Workshop Images

### Requirements

- **Format**: JPEG (.jpg)
- **Size**: 512x512 pixels (recommended)
- **Max file size**: 1 MB
- **Filename**: `pic.jpg`

### Creating Images

**Option 1: Generate Placeholder**
```bash
python scripts/create_workshop_image.py
```

**Option 2: Use Graphics Software**
- Photoshop, GIMP, Paint.NET, etc.
- Create 512x512 canvas
- Design your image
- Save as JPEG (pic.jpg)

**Option 3: Screenshot**
1. Take in-game screenshot
2. Crop to 512x512
3. Save as pic.jpg

### Image Tips

- Use clear, recognizable imagery
- Include addon name/logo
- Use high contrast
- Avoid too much text
- Test how it looks at small sizes

## Command Line Usage

### Create and Publish

```bash
cd scripts
python createworkshop.py
```

**Input:**
- Addon folder name (relative to base path)

**Output:**
- Creates GMA file
- Opens Steam Workshop upload

### Update Addon

```bash
cd scripts
python updateworkshop.py
```

**Input:**
- Addon folder name
- Workshop ID

**Output:**
- Creates GMA file
- Updates Workshop item

### Generate Image

```bash
cd scripts
python create_workshop_image.py
```

**Output:**
- Creates `pic.jpg` in current directory

## Best Practices

### Before Publishing

✅ **Checklist:**
- [ ] Test addon locally in GMOD
- [ ] Create proper addon.json
- [ ] Add workshop image (pic.jpg)
- [ ] Test with friends if possible
- [ ] Check console for errors
- [ ] Verify all required files are included

### addon.json Tips

- Use descriptive title
- Choose correct type
- Add relevant tags (3-5 tags)
- Exclude development files in ignore
- Don't include executable files

### Workshop Tips

- Write clear description
- Add screenshots/videos
- Update regularly
- Respond to comments
- Credit others' work
- Follow Steam Workshop rules

### File Organization

```
Your_Addons/
├── MyGamemode/
│   ├── addon.json
│   ├── pic.jpg
│   └── [addon files]
├── MyWeapon/
│   ├── addon.json
│   ├── pic.jpg
│   └── [addon files]
└── [more addons]
```

### Version Control

- Use Git for your addons
- Add `.gma` files to `.gitignore`
- Keep backup before updating
- Document changes

## Troubleshooting

### Common Issues

**"addon.json not found"**
- Create one in addon root folder
- Use addon.json Editor tab

**"Failed to create GMA"**
- Check addon.json is valid JSON
- Verify folder structure
- Check console output for specific errors

**"Failed to publish"**
- Ensure Steam is running
- Check you're logged in
- Verify pic.jpg exists and is valid
- Confirm you own Garry's Mod

**"Workshop ID invalid"**
- Use numbers only
- Get from Workshop URL
- Must be your own addon to update

### Getting Help

1. Check output console for error details
2. Verify all requirements are met
3. Read error messages carefully
4. Check [Installation Guide](INSTALLATION.md)
5. Report issues on GitHub

## Advanced Usage

### Batch Processing

Create multiple addons:
```python
# Create custom script
from src.core import WorkshopManager

manager = WorkshopManager(gmad_path, gmpublish_path)

for addon in addon_list:
    manager.create_and_publish(addon.folder, addon.image)
```

### Automation

Integrate into build pipeline:
```bash
# Example build script
python build_addon.py
cd scripts
python createworkshop.py
```

### Custom Configuration

Edit `config.json` directly:
```json
{
    "gmad_path": "C:\\..\\gmad.exe",
    "gmpublish_path": "C:\\..\\gmpublish.exe",
    "base_path": "D:\\Addons"
}
```

## Examples

### Example 1: Simple Weapon Addon

```
my_weapon/
├── addon.json
├── pic.jpg
└── lua/
    └── weapons/
        └── weapon_mygun.lua
```

**addon.json:**
```json
{
    "title": "My Awesome Gun",
    "type": "weapon",
    "tags": ["fun", "combat"],
    "ignore": ["*.md", "*.bat"]
}
```

### Example 2: Gamemode

```
my_gamemode/
├── addon.json
├── pic.jpg
└── gamemodes/
    └── mygm/
        ├── gamemode/
        └── mygm.txt
```

**addon.json:**
```json
{
    "title": "My Gamemode",
    "type": "gamemode",
    "tags": ["roleplay", "fun"],
    "ignore": [".git/*", "*.md", "*.psd"]
}
```

## Next Steps

- Read [addon.json Reference](ADDON_JSON.md) for detailed configuration
- Check [API Documentation](API.md) for programmatic usage
- Explore example addons in `examples/` folder

---

[← Back to Installation](INSTALLATION.md) | [Next: addon.json Reference →](ADDON_JSON.md)
