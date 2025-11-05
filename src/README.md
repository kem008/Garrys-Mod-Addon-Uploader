# Source Code (src/)

This directory contains all source code for the GMOD Workshop Manager application.

## Directory Structure

```
src/
├── core/           # Core functionality modules
├── gui/            # GUI interface components
└── utils/          # Utility functions
```

## Modules Overview

### core/
Core business logic for Workshop operations, configuration, and addon.json management.

**Files:**
- `config.py` - Configuration management
- `workshop.py` - Workshop operations (create, publish, update)
- `addon_json.py` - addon.json file handling

**Usage:**
```python
from src.core import Config, WorkshopManager, AddonJSON
```

### gui/
GUI components built with tkinter, organized by tabs and functionality.

**Files:**
- `main.py` - Main application window
- `create_tab.py` - Create & Publish tab
- `update_tab.py` - Update addon tab
- `addon_json_tab.py` - addon.json editor tab
- `settings_tab.py` - Settings configuration tab

**Usage:**
```python
from src.gui import GMODWorkshopGUI
```

### utils/
Utility functions for file operations, image handling, and validation.

**Files:**
- `file_utils.py` - File and folder operations
- `image_utils.py` - Image generation and validation

**Usage:**
```python
from src.utils import validate_file_exists, create_placeholder_image
```

## Development

### Adding New Features

1. **Core functionality** → Add to `core/`
2. **GUI components** → Add to `gui/`
3. **Helper functions** → Add to `utils/`

### Code Style

- Follow PEP 8 guidelines
- Use docstrings for all functions/classes
- Type hints recommended
- Keep modules focused and cohesive

### Testing

When making changes, test:
1. Import modules successfully
2. All functions work as expected
3. GUI launches without errors
4. Integration with GMOD tools

## Documentation

For detailed API documentation, see [API.md](../docs/API.md)

For usage examples, see [USAGE.md](../docs/USAGE.md)
