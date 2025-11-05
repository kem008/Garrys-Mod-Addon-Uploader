# Documentation (docs/)

Complete documentation for GMOD Workshop Manager.

## Available Documentation

### � [QUICKSTART.md](QUICKSTART.md)
Fast reference for common tasks and commands.

**Contents:**
- Quick start commands
- Common tasks
- Command line reference
- addon.json templates
- Troubleshooting quick fixes

**Start here if:** You need a quick lookup or cheat sheet.

---

### �📘 [INSTALLATION.md](INSTALLATION.md)
Complete installation guide with step-by-step instructions.

**Contents:**
- System requirements
- Python installation
- Dependency setup
- First-run configuration
- Troubleshooting

**Start here if:** You're setting up for the first time.

---

### 📗 [USAGE.md](USAGE.md)
Comprehensive guide to using the application.

**Contents:**
- Creating new addons
- Publishing to Workshop
- Updating existing addons
- Managing addon.json
- Workshop images
- Command-line usage
- Best practices

**Start here if:** You want to learn how to use the application.

---

### 📙 [ADDON_JSON.md](ADDON_JSON.md)
Complete reference for addon.json configuration.

**Contents:**
- File structure
- Required fields
- Valid types and tags
- Ignore patterns
- Validation
- Examples
- Best practices

**Start here if:** You need to understand addon.json format.

---

### 📕 [API.md](API.md)
Developer documentation for using the core modules.

**Contents:**
- Module imports
- Class references
- Method signatures
- Code examples
- Best practices
- Error handling

**Start here if:** You're developing with the API or extending functionality.

---

### 🔧 [BATCH_FILES.md](BATCH_FILES.md)
Guide for Windows batch files (env.bat and run.bat).

**Contents:**
- env.bat usage
- run.bat usage
- Troubleshooting batch files
- Virtual environment explanation
- Advanced usage

**Start here if:** You're using Windows batch files for setup.

---

### 📊 [RESTRUCTURE.md](RESTRUCTURE.md)
Details about the project structure and organization.

**Contents:**
- Project structure overview
- Module organization
- File locations
- Architecture explanation

**Start here if:** You want to understand the project layout.

---

### 📋 [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
Complete summary of the restructuring and project overview.

**Contents:**
- What changed in restructuring
- Key improvements
- New features
- Complete file listing

**Start here if:** You want a comprehensive project overview.

---

### 📜 [GUI_LEGACY.md](GUI_LEGACY.md)
Legacy GUI documentation (historical reference).

**Contents:**
- Original GUI documentation
- Legacy information

**Start here if:** You need historical reference.

---

## Quick Links

### For Users
1. [Quick Start Guide](QUICKSTART.md)
2. [Install the application](INSTALLATION.md)
3. [Learn basic usage](USAGE.md#getting-started)
4. [Create your first addon](USAGE.md#creating-a-new-addon)
5. [Publish to Workshop](USAGE.md#publishing-to-workshop)
6. [Use batch files (Windows)](BATCH_FILES.md)

### For Developers
1. [API Overview](API.md#overview)
2. [Core Modules](API.md#core-modules)
3. [Code Examples](API.md#examples)
4. [Best Practices](API.md#best-practices)
5. [Project Structure](RESTRUCTURE.md)

### Reference
- [addon.json Fields](ADDON_JSON.md#required-fields)
- [Valid Addon Types](ADDON_JSON.md#type-string)
- [Common Tags](ADDON_JSON.md#tags-array)
- [Ignore Patterns](ADDON_JSON.md#ignore-array)

## Contributing to Documentation

### Adding Documentation

1. Create new `.md` file in `docs/`
2. Use clear headings and structure
3. Include code examples
4. Add to this README
5. Link from main README

### Markdown Guidelines

- Use `#` for main title
- Use `##` for sections
- Use `###` for subsections
- Include code blocks with language:
  ```python
  # Python code
  ```
- Use tables for comparisons
- Add navigation links at bottom

### Documentation Style

- **Be clear and concise**
- **Use examples** for complex concepts
- **Include screenshots** when helpful
- **Organize logically** from basic to advanced
- **Link related content**
- **Keep updated** with code changes

## Building Documentation Site

For a web version of docs (optional):

```bash
# Install mkdocs
pip install mkdocs mkdocs-material

# Serve locally
mkdocs serve

# Build static site
mkdocs build
```

## Documentation Structure

```
docs/
├── QUICKSTART.md          # Quick reference guide
├── INSTALLATION.md        # Setup guide
├── USAGE.md              # User guide
├── ADDON_JSON.md         # Config reference
├── API.md                # Developer reference
├── BATCH_FILES.md        # Batch files guide
├── RESTRUCTURE.md        # Project structure
├── PROJECT_SUMMARY.md    # Complete summary
├── GUI_LEGACY.md         # Legacy reference
└── README.md             # This file
```

## Formats

All documentation is in Markdown format for:
- Easy editing
- Version control friendly
- GitHub rendering
- Multiple output formats

## Translations

Currently available in:
- English

Contributions for translations welcome!

## Getting Help

If documentation is unclear or incomplete:

1. Check all related docs
2. Search GitHub issues
3. Create new issue with:
   - What you're trying to do
   - Which doc you're reading
   - What's confusing
   - Suggestions for improvement

## Offline Access

All documentation is available offline in this repository:

```bash
# Clone repository
git clone https://github.com/yourusername/Garrys-Mod-Addon-Uploader.git

# Read docs in your editor or browser
cd Garrys-Mod-Addon-Uploader/docs
```

---

[← Back to Main README](../README.md)
