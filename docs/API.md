# API Documentation

Developer reference for using GMOD Workshop Manager modules programmatically.

## Overview

This document describes the API for the core modules that can be used to integrate Workshop functionality into your own applications or scripts.

## Table of Contents

1. [Installation](#installation)
2. [Core Modules](#core-modules)
3. [Configuration](#configuration)
4. [Workshop Operations](#workshop-operations)
5. [addon.json Management](#addonjson-management)
6. [Utilities](#utilities)
7. [Examples](#examples)

## Installation

```bash
pip install -r requirements.txt
```

Import modules in your Python code:

```python
from src.core import Config, WorkshopManager, AddonJSON
from src.utils import *
```

## Core Modules

### Config

Manages application configuration settings.

#### Class: `Config`

```python
from src.core import Config

config = Config(config_file="config.json")
```

**Constructor Parameters:**
- `config_file` (str, optional): Path to config file. Default: "config.json"

**Methods:**

##### `load()`

Load configuration from file.

```python
settings = config.load()
# Returns: dict with settings
```

##### `save(settings=None)`

Save configuration to file.

```python
success = config.save()
# Returns: bool (True if successful)
```

##### `get(key, default=None)`

Get a configuration value.

```python
gmad_path = config.get('gmad_path')
# Returns: value or default if not found
```

##### `set(key, value)`

Set a configuration value.

```python
config.set('gmad_path', 'C:\\path\\to\\gmad.exe')
```

##### `update(**kwargs)`

Update multiple configuration values.

```python
config.update(
    gmad_path='C:\\path\\to\\gmad.exe',
    gmpublish_path='C:\\path\\to\\gmpublish.exe'
)
```

**Example:**

```python
from src.core import Config

# Load config
config = Config()

# Get value
gmad_path = config.get('gmad_path')

# Set values
config.set('base_path', 'D:\\Addons')

# Save
config.save()
```

### WorkshopManager

Handles Workshop operations (create GMA, publish, update).

#### Class: `WorkshopManager`

```python
from src.core import WorkshopManager

manager = WorkshopManager(
    gmad_path='C:\\...\\gmad.exe',
    gmpublish_path='C:\\...\\gmpublish.exe'
)
```

**Constructor Parameters:**
- `gmad_path` (str): Path to gmad.exe
- `gmpublish_path` (str): Path to gmpublish.exe

**Methods:**

##### `create_gma(addon_folder, output_path)`

Create a GMA file from addon folder.

```python
success, stdout, stderr = manager.create_gma(
    addon_folder='D:\\Addons\\MyAddon',
    output_path='D:\\Addons\\MyAddon.gma'
)
```

**Parameters:**
- `addon_folder` (str): Path to addon source folder
- `output_path` (str): Path for output GMA file

**Returns:**
- `tuple`: (success: bool, stdout: str, stderr: str)

##### `publish_addon(gma_path, image_path)`

Publish a new addon to Steam Workshop.

```python
success, stdout, stderr = manager.publish_addon(
    gma_path='D:\\Addons\\MyAddon.gma',
    image_path='D:\\Addons\\MyAddon\\pic.jpg'
)
```

**Parameters:**
- `gma_path` (str): Path to GMA file
- `image_path` (str): Path to workshop thumbnail

**Returns:**
- `tuple`: (success: bool, stdout: str, stderr: str)

##### `update_addon(gma_path, workshop_id)`

Update an existing Workshop addon.

```python
success, stdout, stderr = manager.update_addon(
    gma_path='D:\\Addons\\MyAddon.gma',
    workshop_id='1234567890'
)
```

**Parameters:**
- `gma_path` (str): Path to GMA file
- `workshop_id` (str): Steam Workshop ID

**Returns:**
- `tuple`: (success: bool, stdout: str, stderr: str)

##### `create_and_publish(addon_folder, image_path)`

Create GMA and publish in one operation.

```python
success, messages = manager.create_and_publish(
    addon_folder='D:\\Addons\\MyAddon',
    image_path='D:\\Addons\\MyAddon\\pic.jpg'
)
```

**Parameters:**
- `addon_folder` (str): Path to addon source folder
- `image_path` (str): Path to workshop thumbnail

**Returns:**
- `tuple`: (success: bool, messages: list of str)

##### `create_and_update(addon_folder, workshop_id)`

Create GMA and update existing Workshop item.

```python
success, messages = manager.create_and_update(
    addon_folder='D:\\Addons\\MyAddon',
    workshop_id='1234567890'
)
```

**Parameters:**
- `addon_folder` (str): Path to addon source folder
- `workshop_id` (str): Steam Workshop ID

**Returns:**
- `tuple`: (success: bool, messages: list of str)

**Complete Example:**

```python
from src.core import WorkshopManager

# Initialize
manager = WorkshopManager(
    gmad_path='C:\\Program Files (x86)\\Steam\\steamapps\\common\\GarrysMod\\bin\\gmad.exe',
    gmpublish_path='C:\\Program Files (x86)\\Steam\\steamapps\\common\\GarrysMod\\bin\\gmpublish.exe'
)

# Create and publish
success, messages = manager.create_and_publish(
    addon_folder='D:\\Addons\\MyAddon',
    image_path='D:\\Addons\\MyAddon\\pic.jpg'
)

for msg in messages:
    print(msg)

if success:
    print("Published successfully!")
else:
    print("Failed to publish")
```

### AddonJSON

Manages addon.json files.

#### Class: `AddonJSON`

```python
from src.core import AddonJSON

addon = AddonJSON(addon_folder='D:\\Addons\\MyAddon')
```

**Constructor Parameters:**
- `addon_folder` (str, optional): Path to addon folder

**Class Attributes:**

```python
AddonJSON.VALID_TYPES  # List of valid addon types
AddonJSON.DEFAULT_IGNORE  # Default ignore patterns
```

**Methods:**

##### `load(addon_folder=None)`

Load addon.json from folder.

```python
success = addon.load('D:\\Addons\\MyAddon')
# Returns: bool (True if loaded)
```

##### `save(addon_folder=None)`

Save addon.json to folder.

```python
success = addon.save('D:\\Addons\\MyAddon')
# Returns: bool (True if saved)
```

##### `validate()`

Validate addon.json data.

```python
valid, errors = addon.validate()
# Returns: tuple (valid: bool, errors: list of str)
```

##### `set_title(title)`

Set addon title.

```python
addon.set_title("My Awesome Addon")
```

##### `set_type(addon_type)`

Set addon type.

```python
success = addon.set_type("gamemode")
# Returns: bool (True if type is valid)
```

##### `set_tags(tags)`

Set tags (accepts list or comma-separated string).

```python
addon.set_tags(["fun", "roleplay"])
# or
addon.set_tags("fun, roleplay")
```

##### `set_ignore(ignore_patterns)`

Set ignore patterns (accepts list or newline-separated string).

```python
addon.set_ignore(["*.md", "*.psd"])
# or
addon.set_ignore("*.md\n*.psd")
```

##### Getter Methods

```python
title = addon.get_title()  # Returns: str
addon_type = addon.get_type()  # Returns: str
tags = addon.get_tags()  # Returns: list
tags_str = addon.get_tags_string()  # Returns: str (comma-separated)
ignore = addon.get_ignore()  # Returns: list
ignore_str = addon.get_ignore_string()  # Returns: str (newline-separated)
```

**Complete Example:**

```python
from src.core import AddonJSON

# Create new addon.json
addon = AddonJSON()

# Set values
addon.set_title("My Gamemode")
addon.set_type("gamemode")
addon.set_tags(["roleplay", "fun"])
addon.set_ignore(["*.md", "*.psd", ".git/*"])

# Validate
valid, errors = addon.validate()
if valid:
    # Save
    addon.save('D:\\Addons\\MyGamemode')
    print("Saved!")
else:
    print("Errors:", errors)

# Load existing
addon2 = AddonJSON()
if addon2.load('D:\\Addons\\MyGamemode'):
    print(f"Title: {addon2.get_title()}")
    print(f"Type: {addon2.get_type()}")
    print(f"Tags: {addon2.get_tags_string()}")
```

## Utilities

### File Utilities

```python
from src.utils import file_utils
```

#### Functions

##### `validate_file_exists(filepath)`

```python
exists = file_utils.validate_file_exists('D:\\file.txt')
# Returns: bool
```

##### `validate_folder_exists(folderpath)`

```python
exists = file_utils.validate_folder_exists('D:\\folder')
# Returns: bool
```

##### `get_addon_name(addon_folder)`

```python
name = file_utils.get_addon_name('D:\\Addons\\MyAddon')
# Returns: str ('MyAddon')
```

##### `get_gma_output_path(addon_folder)`

```python
gma_path = file_utils.get_gma_output_path('D:\\Addons\\MyAddon')
# Returns: str ('D:\\Addons\\MyAddon.gma')
```

##### `find_pic_jpg(addon_folder)`

```python
pic_path = file_utils.find_pic_jpg('D:\\Addons\\MyAddon')
# Returns: str or None
```

##### `find_addon_json(addon_folder)`

```python
json_path = file_utils.find_addon_json('D:\\Addons\\MyAddon')
# Returns: str or None
```

##### `validate_workshop_id(workshop_id)`

```python
valid = file_utils.validate_workshop_id('1234567890')
# Returns: bool
```

##### `format_file_size(size_bytes)`

```python
size_str = file_utils.format_file_size(1048576)
# Returns: str ('1.00 MB')
```

##### `get_file_size(filepath)`

```python
size = file_utils.get_file_size('D:\\file.txt')
# Returns: int (bytes)
```

### Image Utilities

```python
from src.utils import image_utils
```

#### Functions

##### `create_placeholder_image(output_path, title, subtitle)`

```python
success = image_utils.create_placeholder_image(
    output_path='pic.jpg',
    title='GMOD Addon',
    subtitle='Workshop Item'
)
# Returns: bool
```

##### `validate_workshop_image(image_path)`

```python
valid, errors = image_utils.validate_workshop_image('pic.jpg')
# Returns: tuple (valid: bool, errors: list of str)
```

##### `resize_image(input_path, output_path, size)`

```python
success = image_utils.resize_image(
    input_path='original.jpg',
    output_path='pic.jpg',
    size=(512, 512)
)
# Returns: bool
```

## Examples

### Example 1: Simple Publish Script

```python
from src.core import Config, WorkshopManager

# Load config
config = Config()

# Create manager
manager = WorkshopManager(
    config.get('gmad_path'),
    config.get('gmpublish_path')
)

# Publish addon
success, messages = manager.create_and_publish(
    addon_folder='D:\\Addons\\MyAddon',
    image_path='D:\\Addons\\MyAddon\\pic.jpg'
)

for msg in messages:
    print(msg)
```

### Example 2: Batch Update Multiple Addons

```python
from src.core import WorkshopManager

manager = WorkshopManager(gmad_path, gmpublish_path)

addons = [
    {'folder': 'D:\\Addons\\Addon1', 'id': '1111111111'},
    {'folder': 'D:\\Addons\\Addon2', 'id': '2222222222'},
    {'folder': 'D:\\Addons\\Addon3', 'id': '3333333333'},
]

for addon in addons:
    print(f"Updating {addon['folder']}...")
    success, messages = manager.create_and_update(
        addon['folder'],
        addon['id']
    )
    
    if success:
        print(f"✓ {addon['folder']} updated")
    else:
        print(f"✗ {addon['folder']} failed")
```

### Example 3: Create addon.json Programmatically

```python
from src.core import AddonJSON

# Define addons
addons_data = [
    {
        'folder': 'D:\\Addons\\Gamemode1',
        'title': 'My Roleplay Gamemode',
        'type': 'gamemode',
        'tags': ['roleplay', 'fun']
    },
    {
        'folder': 'D:\\Addons\\Weapon1',
        'title': 'Custom Weapon Pack',
        'type': 'weapon',
        'tags': ['combat', 'fun']
    }
]

# Create addon.json for each
for data in addons_data:
    addon = AddonJSON()
    addon.set_title(data['title'])
    addon.set_type(data['type'])
    addon.set_tags(data['tags'])
    
    if addon.save(data['folder']):
        print(f"✓ Created addon.json for {data['title']}")
    else:
        print(f"✗ Failed for {data['title']}")
```

### Example 4: Validate All Addons

```python
import os
from src.core import AddonJSON

addon_folders = ['D:\\Addons\\Addon1', 'D:\\Addons\\Addon2']

for folder in addon_folders:
    addon = AddonJSON()
    
    if addon.load(folder):
        valid, errors = addon.validate()
        
        if valid:
            print(f"✓ {os.path.basename(folder)} is valid")
        else:
            print(f"✗ {os.path.basename(folder)} has errors:")
            for error in errors:
                print(f"  - {error}")
    else:
        print(f"✗ {os.path.basename(folder)}: addon.json not found")
```

### Example 5: Custom Build Pipeline

```python
from src.core import WorkshopManager, AddonJSON
from src.utils import find_pic_jpg, validate_workshop_image

def build_and_publish(addon_folder):
    """Complete build and publish pipeline"""
    
    # Validate addon.json
    addon = AddonJSON()
    if not addon.load(addon_folder):
        print("Error: addon.json not found")
        return False
    
    valid, errors = addon.validate()
    if not valid:
        print("Error: Invalid addon.json")
        for error in errors:
            print(f"  - {error}")
        return False
    
    # Validate image
    pic_path = find_pic_jpg(addon_folder)
    if not pic_path:
        print("Error: pic.jpg not found")
        return False
    
    valid, errors = validate_workshop_image(pic_path)
    if not valid:
        print("Warning: Image issues:")
        for error in errors:
            print(f"  - {error}")
    
    # Publish
    manager = WorkshopManager(gmad_path, gmpublish_path)
    success, messages = manager.create_and_publish(addon_folder, pic_path)
    
    for msg in messages:
        print(msg)
    
    return success

# Use it
build_and_publish('D:\\Addons\\MyAddon')
```

## Error Handling

All methods return success indicators. Always check return values:

```python
# Check boolean returns
success = addon.save()
if not success:
    print("Save failed")

# Check tuple returns
valid, errors = addon.validate()
if not valid:
    for error in errors:
        print(f"Error: {error}")

# Check with subprocess results
success, stdout, stderr = manager.create_gma(folder, output)
if not success:
    print(f"Error: {stderr}")
```

## Thread Safety

The core modules are not thread-safe. If using in a multi-threaded environment:

```python
import threading

lock = threading.Lock()

def safe_operation():
    with lock:
        # Perform operations
        config.save()
```

## Best Practices

1. **Always validate** before saving
2. **Check return values** for all operations
3. **Use absolute paths** for all file operations
4. **Handle exceptions** with try-except blocks
5. **Close resources** properly
6. **Load config once** at startup
7. **Reuse managers** instead of recreating

## Related Documentation

- [Usage Guide](USAGE.md) - GUI usage
- [addon.json Reference](ADDON_JSON.md) - Configuration format
- [Installation Guide](INSTALLATION.md) - Setup instructions

---

[← Back to addon.json Reference](ADDON_JSON.md) | [Back to README](../README.md)
