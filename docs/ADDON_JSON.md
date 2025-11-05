# addon.json Reference

Complete reference guide for GMOD addon.json configuration file.

## Overview

The `addon.json` file is a required configuration file that must be present in the root of your addon folder. It tells Garry's Mod and the Workshop about your addon's metadata.

## Basic Structure

```json
{
    "title": "My Addon Name",
    "type": "gamemode",
    "tags": ["fun", "roleplay"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.psd"
    ]
}
```

## Required Fields

### title (string)

The display name of your addon as it appears in the Workshop and in-game.

**Requirements:**
- Must not be empty
- Maximum 128 characters recommended
- Should be descriptive and unique

**Examples:**
```json
"title": "Trouble in Terrorist Town"
"title": "Wire Mod"
"title": "PHX Models Pack"
```

**Best Practices:**
- Use proper capitalization
- Avoid special characters
- Make it searchable
- Keep it concise

### type (string)

The category/type of your addon. This determines how it's classified in the Workshop.

**Valid Types:**

| Type | Description | Examples |
|------|-------------|----------|
| `gamemode` | Custom game modes | TTT, DarkRP, Sandbox |
| `map` | Custom maps | RP maps, build maps |
| `weapon` | Weapons | SWEP, custom guns |
| `vehicle` | Vehicles | Cars, planes, boats |
| `npc` | NPCs and creatures | Custom enemies, allies |
| `tool` | Tools | Precision tool, axis tool |
| `effects` | Visual/sound effects | Particle effects, sounds |
| `model` | 3D models | Props, playermodels |
| `entity` | Entities | Interactive objects |
| `other` | Miscellaneous | Doesn't fit other categories |

**Example:**
```json
"type": "gamemode"
```

**Important:**
- Must be exactly one of the valid types
- Case-sensitive (use lowercase)
- Choose the most specific type

### tags (array)

An array of tags that help categorize and make your addon discoverable in the Workshop.

**Common Tags:**

| Category | Tags |
|----------|------|
| **Style** | fun, cartoon, realistic, scenic, comic, movie |
| **Gameplay** | roleplay, build, combat, pvp, pve, survival |
| **Theme** | sci-fi, fantasy, military, horror, medieval |
| **Content** | realism, scenic, atmospheric |

**Example:**
```json
"tags": ["fun", "roleplay", "realism"]
```

**Best Practices:**
- Use 2-5 tags
- Be accurate and honest
- Use common/popular tags
- Avoid tag spam
- Match content to tags

### ignore (array)

An array of file patterns to exclude from the GMA package. Uses glob pattern matching.

**Common Patterns:**

```json
"ignore": [
    ".git/*",              // Git repository files
    ".gitignore",          // Git ignore file
    ".gitattributes",      // Git attributes
    "*.md",                // Markdown docs
    "*.txt",               // Text files
    "*.bat",               // Batch scripts
    "*.sh",                // Shell scripts
    "*.psd",               // Photoshop files
    "*.xcf",               // GIMP files
    "*.blend",             // Blender files
    "*.max",               // 3DS Max files
    "*.zip",               // Zip archives
    "*.rar",               // RAR archives
    "*.7z",                // 7-Zip archives
    "*.gma",               // GMA files
    "*.bz2",               // Compressed files
    "*.old",               // Backup files
    "*~",                  // Temporary files
    "dev/*",               // Development folder
    "source/*",            // Source files folder
    "unused/*"             // Unused assets
]
```

**Wildcards:**
- `*` - Matches any characters
- `?` - Matches single character
- `**` - Matches directories recursively
- `*.ext` - All files with extension
- `folder/*` - All files in folder

**Examples:**

```json
// Exclude all markdown files
"*.md"

// Exclude specific folder
"development/*"

// Exclude by extension
"*.psd"

// Exclude hidden files
".*"

// Exclude specific file
"README.txt"
```

## Complete Example

### Simple Addon

```json
{
    "title": "My Simple Tool",
    "type": "tool",
    "tags": ["fun", "build"],
    "ignore": [
        "*.md",
        ".git/*"
    ]
}
```

### Complex Gamemode

```json
{
    "title": "My Roleplay Gamemode",
    "type": "gamemode",
    "tags": ["roleplay", "realism", "fun"],
    "ignore": [
        ".git/*",
        ".gitignore",
        ".gitattributes",
        "*.md",
        "*.txt",
        "*.bat",
        "*.sh",
        "*.psd",
        "*.xcf",
        "*.blend",
        "*.zip",
        "*.gma",
        "*.bz2",
        "dev/*",
        "source/*",
        "docs/*",
        "README.md",
        "LICENSE"
    ]
}
```

### Model Pack

```json
{
    "title": "Custom Props Pack",
    "type": "model",
    "tags": ["realism", "scenic", "build"],
    "ignore": [
        ".git/*",
        "*.md",
        "*.blend",
        "*.max",
        "*.psd",
        "source_files/*",
        "renders/*"
    ]
}
```

## Validation

### Required Checks

Your addon.json must pass these validations:

1. **Valid JSON** - Must be properly formatted JSON
2. **Has title** - Title field must exist and not be empty
3. **Has type** - Type must be one of the valid types
4. **Has tags** - Tags must be an array (can be empty)
5. **Has ignore** - Ignore must be an array (can be empty)

### Using the Validator

**Via GUI:**
1. Open addon.json Editor tab
2. Load or create addon.json
3. Click "Validate" button

**Via Code:**
```python
from src.core import AddonJSON

addon = AddonJSON()
addon.load("path/to/addon/folder")
valid, errors = addon.validate()

if valid:
    print("Valid!")
else:
    for error in errors:
        print(f"Error: {error}")
```

## Common Mistakes

### ❌ Invalid Type

```json
{
    "type": "Gamemode"  // Wrong: Should be lowercase
}
```

```json
{
    "type": "addon"  // Wrong: Not a valid type
}
```

### ❌ Missing Quotes

```json
{
    "tags": [fun, roleplay]  // Wrong: Strings need quotes
}
```

### ❌ Trailing Comma

```json
{
    "title": "My Addon",
    "type": "gamemode",  // Wrong: Last item has comma
}
```

### ❌ Empty Title

```json
{
    "title": "",  // Wrong: Title can't be empty
}
```

## Tips and Best Practices

### Choosing a Type

1. Choose the **most specific** type that fits
2. If it's a gamemode, use `gamemode` not `other`
3. Use `other` only if nothing else fits
4. Consider what players will search for

### Selecting Tags

1. **Be honest** - Don't use misleading tags
2. **Be relevant** - Tags should match content
3. **Be specific** - Use descriptive tags
4. **Check popular** - See what similar addons use
5. **Limit yourself** - 3-5 tags is ideal

### Ignore Patterns

**Always exclude:**
- Version control files (`.git/`, `.svn/`)
- Documentation (`.md`, `.txt`)
- Source files (`.psd`, `.blend`, `.max`)
- Archives (`.zip`, `.rar`)
- Build artifacts (`.gma`)
- Development tools

**Never exclude:**
- Lua files (`.lua`)
- Models (`.mdl`, `.vtx`, `.vvd`, `.phy`)
- Materials (`.vmt`, `.vtf`)
- Sounds (`.wav`, `.mp3`)
- Particles (`.pcf`)

### File Size Optimization

Use ignore patterns to reduce GMA size:

```json
"ignore": [
    "unused/*",        // Unused assets
    "*.psd",          // Large source files
    "textures_src/*", // Original texture files
    "*.blend",        // 3D source files
    "dev/*"          // Development files
]
```

## Advanced Usage

### Environment-Specific Ignore

Development version:
```json
{
    "ignore": [
        ".git/*",
        "*.md"
    ]
}
```

Release version:
```json
{
    "ignore": [
        ".git/*",
        "*.md",
        "dev/*",
        "tests/*",
        "debug/*",
        "*.log"
    ]
}
```

### Conditional Patterns

```json
"ignore": [
    "**/.DS_Store",     // Mac files
    "**/Thumbs.db",     // Windows thumbnails
    "**/__pycache__",   // Python cache
    "**/node_modules",  // Node modules (if using)
]
```

## JSON Format Reference

### Data Types

- **String**: `"text"` - Enclosed in quotes
- **Array**: `["item1", "item2"]` - List of values
- **Object**: `{"key": "value"}` - Key-value pairs

### Escaping Special Characters

```json
{
    "title": "My \"Quoted\" Addon",  // Escape quotes
    "ignore": ["path\\to\\file"]     // Escape backslashes
}
```

### Comments

JSON doesn't support comments officially. Remove any comments before saving:

```json
// This won't work in JSON
{
    "title": "My Addon"  // This will cause an error
}
```

Use this format instead:
```json
{
    "title": "My Addon"
}
```

## Tools and Resources

### Validation Tools

- **Online**: [JSONLint](https://jsonlint.com/)
- **Built-in**: Use addon.json Editor in GUI
- **Command**: `python -m json.tool addon.json`

### Template Generator

Use the GUI addon.json Editor to generate templates automatically.

### Example Templates

Available in `examples/` folder:
- Gamemode template
- Weapon template
- Model pack template
- Tool template

## FAQ

**Q: Can I have multiple types?**  
A: No, only one type is allowed per addon.

**Q: Are tags case-sensitive?**  
A: No, but use lowercase for consistency.

**Q: How many tags can I use?**  
A: Technically unlimited, but 3-5 is recommended.

**Q: Can I change addon.json after publishing?**  
A: Yes, changes will apply on next update.

**Q: What happens if addon.json is invalid?**  
A: GMA creation will fail with an error.

**Q: Can I use Unicode characters in title?**  
A: Yes, but ASCII characters are safer for compatibility.

## Related Documentation

- [Usage Guide](USAGE.md) - How to use the editor
- [Installation Guide](INSTALLATION.md) - Setup instructions
- [API Documentation](API.md) - Programmatic access

---

[← Back to Usage Guide](USAGE.md) | [Next: API Documentation →](API.md)
