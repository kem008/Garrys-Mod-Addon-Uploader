# Examples Directory

Example addon structures and templates for GMOD Workshop Manager.

## Purpose

This directory contains example addon structures and templates to help you get started with creating your own GMOD addons.

## Files

### `addon.json`
Example `addon.json` template file showing the correct structure and common ignore patterns.

You can copy this file to your addon folder and modify it for your needs.

## Example Structures

### Coming Soon

Example addons will be added here including:

- **Simple Gamemode** - Basic gamemode structure
- **Weapon Pack** - SWEP example
- **Model Pack** - Model addon example
- **Tool Example** - STOOL example
- **Map Addon** - Map with proper structure

## Creating Your Own Addon

### Basic Structure

```
YourAddon/
├── addon.json          # Required: Addon metadata
├── pic.jpg            # Required: Workshop thumbnail
├── lua/               # Lua code
│   ├── autorun/       # Auto-executed code
│   ├── entities/      # Custom entities
│   ├── weapons/       # Custom weapons
│   ├── effects/       # Custom effects
│   └── [...]
├── materials/         # Textures (.vmt, .vtf)
├── models/            # 3D models (.mdl, .vtx, .vvd, .phy)
├── sound/             # Audio files (.wav, .mp3)
├── particles/         # Particle effects (.pcf)
└── resource/          # Resource files (fonts, etc.)
```

### Gamemode Structure

```
MyGamemode/
├── addon.json
├── pic.jpg
└── gamemodes/
    └── mygamemode/
        ├── gamemode/
        │   ├── init.lua
        │   ├── cl_init.lua
        │   ├── shared.lua
        │   └── [...]
        ├── content/
        │   ├── materials/
        │   ├── models/
        │   └── sound/
        └── mygamemode.txt
```

### Weapon Structure

```
MyWeapon/
├── addon.json
├── pic.jpg
└── lua/
    └── weapons/
        └── weapon_mygun/
            ├── shared.lua
            ├── cl_init.lua
            └── init.lua
```

### Model Pack Structure

```
MyModels/
├── addon.json
├── pic.jpg
├── models/
│   ├── mymodel.mdl
│   ├── mymodel.vtx
│   ├── mymodel.vvd
│   └── mymodel.phy
└── materials/
    └── models/
        └── mymodel/
            ├── texture.vmt
            └── texture.vtf
```

## Example addon.json Files

### Gamemode

```json
{
    "title": "My Awesome Gamemode",
    "type": "gamemode",
    "tags": ["roleplay", "fun", "realism"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.psd",
        "*.blend",
        "dev/*"
    ]
}
```

### Weapon

```json
{
    "title": "Custom Weapons Pack",
    "type": "weapon",
    "tags": ["combat", "fun", "realism"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.psd"
    ]
}
```

### Model Pack

```json
{
    "title": "Realistic Props Pack",
    "type": "model",
    "tags": ["realism", "scenic", "build"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.blend",
        "*.max",
        "source/*"
    ]
}
```

## Quick Start Templates

### Template 1: Minimal Addon

```bash
mkdir MyAddon
cd MyAddon

# Create addon.json
cat > addon.json << 'EOF'
{
    "title": "My Addon",
    "type": "other",
    "tags": ["fun"],
    "ignore": [".git/*", "*.md"]
}
EOF

# Create folder structure
mkdir -p lua/autorun

# Generate placeholder image
cd ..
python scripts/create_workshop_image.py
mv pic.jpg MyAddon/
```

### Template 2: Complete Gamemode

```bash
mkdir MyGamemode
cd MyGamemode

# Create structure
mkdir -p gamemodes/mygm/gamemode
mkdir -p gamemodes/mygm/content/{materials,models,sound}

# Create addon.json
# (Use GUI addon.json Editor)

# Generate image
cd ..
python scripts/create_workshop_image.py
mv pic.jpg MyGamemode/
```

## Testing Your Addon

Before publishing:

1. **Copy to GMOD addons folder:**
   ```
   C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\garrysmod\addons\
   ```

2. **Launch GMOD**

3. **Check for errors** in console (`)

4. **Test functionality**

5. **Test with friends** if possible

## Best Practices

### File Organization

- Keep related files together
- Use descriptive names
- Follow GMOD conventions
- Document your code
- Include README for users

### addon.json

- Accurate title and type
- Relevant tags only
- Exclude development files
- Validate before publishing

### Workshop Image

- Clear and recognizable
- Represents addon content
- Professional appearance
- Proper dimensions (512x512)

## Contributing Examples

Want to add an example? Create a pull request with:

1. Complete addon structure
2. Working code
3. README explaining the example
4. Proper addon.json
5. Workshop image

## Resources

### GMOD Wiki
- https://wiki.facepunch.com/gmod/

### Learning Resources
- Lua tutorials
- GMOD Lua API
- Workshop best practices

### Community
- Facepunch Forums
- /r/gmod
- GMOD Discord servers

## Need Help?

1. Check [Usage Guide](../docs/USAGE.md)
2. Read [addon.json Reference](../docs/ADDON_JSON.md)
3. Ask in GMOD community
4. Create GitHub issue

---

[← Back to Main README](../README.md)
