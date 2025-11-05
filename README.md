# GMOD Workshop Manager

A comprehensive GUI application and toolkit for managing Garry's Mod Workshop addons. Create, publish, and update addons with ease!

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Features

- **Modern GUI Interface** - User-friendly interface built with tkinter
- **Create & Publish** - Create GMA files and publish new addons to Workshop
- **Update Addons** - Update existing Workshop items with new versions
- **addon.json Editor** - Visual editor for addon metadata
- **Settings Manager** - Configure paths to GMOD tools
- **Modular Architecture** - Clean, maintainable codebase
- **CLI Scripts** - Command-line alternatives for automation

## 📁 Project Structure

```
Garrys-Mod-Addon-Uploader/
├── src/                    # Source code
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration management
│   │   ├── workshop.py    # Workshop operations
│   │   └── addon_json.py  # addon.json handling
│   ├── gui/               # GUI components
│   │   ├── main.py        # Main application
│   │   ├── create_tab.py  # Create & Publish tab
│   │   ├── update_tab.py  # Update tab
│   │   ├── addon_json_tab.py  # JSON editor tab
│   │   └── settings_tab.py    # Settings tab
│   └── utils/             # Utility functions
│       ├── file_utils.py  # File operations
│       └── image_utils.py # Image handling
├── scripts/               # CLI scripts
│   ├── createworkshop.py  # Original create script
│   ├── updateworkshop.py  # Original update script
│   └── create_workshop_image.py  # Image generator
├── docs/                  # Documentation
│   ├── INSTALLATION.md    # Installation guide
│   ├── USAGE.md          # Usage guide
│   ├── ADDON_JSON.md     # addon.json reference
│   ├── API.md            # API documentation
│   ├── QUICKSTART.md     # Quick reference
│   ├── BATCH_FILES.md    # Batch files guide
│   ├── RESTRUCTURE.md    # Project structure details
│   └── PROJECT_SUMMARY.md # Complete summary
├── examples/              # Example addons
│   └── addon.json        # Example addon.json template
├── assets/                # Assets (images, etc.)
├── old/                   # Deprecated files (for reference)
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Garry's Mod installed
- Steam account with Garry's Mod ownership

### Installation

#### Windows Quick Setup

1. **Clone or download this repository**

2. **Run the setup script:**
```cmd
env.bat
```
This will automatically:
- Create a virtual environment
- Create requirements.txt if needed
- Install all dependencies

3. **Run the application:**
```cmd
run.bat
```

#### Manual Installation (All Platforms)

1. **Clone or download this repository**

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the GUI application:**
```bash
python main.py
```

4. **Configure settings:**
   - Go to the "Settings" tab
   - Set paths to `gmad.exe` and `gmpublish.exe`
   - Save settings

## 📖 Documentation

- **[Quick Start](docs/QUICKSTART.md)** - Quick reference guide
- **[Installation Guide](docs/INSTALLATION.md)** - Detailed installation instructions
- **[Usage Guide](docs/USAGE.md)** - How to use the application
- **[addon.json Reference](docs/ADDON_JSON.md)** - Complete addon.json documentation
- **[API Documentation](docs/API.md)** - For developers using the core modules
- **[Batch Files Guide](docs/BATCH_FILES.md)** - Windows batch files documentation
- **[Project Structure](docs/RESTRUCTURE.md)** - Project organization details

## 🎮 Quick Usage

### Publishing a New Addon

1. Open the application
2. Go to **"Create & Publish"** tab
3. Select your addon folder
4. Select your workshop image (pic.jpg)
5. Click **"Create & Publish"**

### Updating an Existing Addon

1. Go to **"Update Addon"** tab
2. Select your addon folder
3. Enter your Workshop ID
4. Click **"Update Workshop"**

### Creating addon.json

1. Go to **"addon.json Editor"** tab
2. Select your addon folder
3. Fill in the details
4. Click **"Save addon.json"**

## 🛠️ Command Line Usage

For automation and scripting, use the CLI scripts:

```bash
# Create and publish (original script)
cd scripts
python createworkshop.py

# Update existing addon
python updateworkshop.py

# Generate workshop image
python create_workshop_image.py
```

## 📦 Requirements

- **Python**: 3.7+
- **Pillow**: For image generation and manipulation
- **tkinter**: For GUI (usually included with Python)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available for free use.

## 🐛 Troubleshooting

### "gmad.exe not found"
Configure the correct path in Settings. Default location:
```
C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe
```

### "Failed to create GMA"
- Ensure `addon.json` exists in your addon folder
- Check that addon.json is valid JSON
- Verify folder contains valid GMOD addon structure

### "Failed to publish"
- Ensure Steam is running and you're logged in
- Verify `pic.jpg` exists and is valid JPG format
- Check that you own Garry's Mod on Steam

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the [documentation](docs/)

## 🎯 Roadmap

- [ ] Batch processing for multiple addons
- [ ] Workshop statistics viewer
- [ ] Addon validation and testing tools
- [ ] Multi-language support
- [ ] Auto-update checker

## ⭐ Acknowledgments

- Built for the Garry's Mod community
- Uses Valve's Workshop tools
- Inspired by the need for better addon management

---

**Made with ❤️ for the GMOD Community**
