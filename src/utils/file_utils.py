"""
Utility functions for GMOD Workshop Manager
"""
import os


def validate_file_exists(filepath):
    """Check if a file exists"""
    return os.path.exists(filepath) and os.path.isfile(filepath)


def validate_folder_exists(folderpath):
    """Check if a folder exists"""
    return os.path.exists(folderpath) and os.path.isdir(folderpath)


def get_addon_name(addon_folder):
    """Get addon name from folder path"""
    return os.path.basename(addon_folder)


def get_gma_output_path(addon_folder):
    """Generate output path for GMA file"""
    folder_name = get_addon_name(addon_folder)
    parent_dir = os.path.dirname(addon_folder)
    return os.path.join(parent_dir, f"{folder_name}.gma")


def find_pic_jpg(addon_folder):
    """Find pic.jpg in addon folder"""
    pic_path = os.path.join(addon_folder, "pic.jpg")
    if validate_file_exists(pic_path):
        return pic_path
    return None


def find_addon_json(addon_folder):
    """Find addon.json in addon folder"""
    json_path = os.path.join(addon_folder, "addon.json")
    if validate_file_exists(json_path):
        return json_path
    return None


def validate_workshop_id(workshop_id):
    """Validate Workshop ID format"""
    if not workshop_id:
        return False
    
    # Remove whitespace
    workshop_id = str(workshop_id).strip()
    
    # Should be numeric
    return workshop_id.isdigit() and len(workshop_id) > 0


def format_file_size(size_bytes):
    """Format file size in human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def get_file_size(filepath):
    """Get file size in bytes"""
    try:
        return os.path.getsize(filepath)
    except:
        return 0
