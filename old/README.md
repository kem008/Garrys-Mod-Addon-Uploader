# Old Files

This folder contains deprecated files from the original project structure that have been replaced by the new modular application.

## Files

### `gmod_workshop_gui.py`
- **Status**: Deprecated
- **Replaced By**: `main.py` + modular architecture in `src/`
- **Description**: Original monolithic GUI application before restructuring

### `gma_create.bat`
- **Status**: Deprecated
- **Replaced By**: GUI application (`main.py`) with Create & Publish tab
- **Description**: Old batch file for creating GMA files

### `publish_create.bat`
- **Status**: Deprecated
- **Replaced By**: GUI application (`main.py`) with Create & Publish tab
- **Description**: Old batch file for publishing addons to Workshop

### `update_to_workshop.bat`
- **Status**: Deprecated
- **Replaced By**: GUI application (`main.py`) with Update tab
- **Description**: Old batch file for updating existing Workshop items

## Why Were These Files Moved?

The project was restructured to provide:
- Better maintainability through modular code organization
- Professional folder structure with separation of concerns
- Comprehensive documentation
- Modern GUI with tabbed interface
- Automated environment setup

These files are kept for reference purposes but should not be used in production.

## Migration Guide

If you were using the old batch files or `gmod_workshop_gui.py`, please:

1. Run `env.bat` to set up the new environment
2. Run `run.bat` to launch the new GUI application
3. See [../docs/QUICKSTART.md](../docs/QUICKSTART.md) for quick reference
4. See [../docs/USAGE.md](../docs/USAGE.md) for detailed usage instructions
