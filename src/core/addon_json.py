"""
addon.json Manager for GMOD addons
Handles reading, writing, and validating addon.json files
"""
import json
import os


class AddonJSON:
    """Manages addon.json files for GMOD addons"""
    
    VALID_TYPES = [
        "gamemode", "map", "weapon", "vehicle", "npc", 
        "tool", "effects", "model", "entity", "other"
    ]
    
    DEFAULT_IGNORE = [
        ".git/*",
        ".gitignore",
        ".gitattributes",
        "*.md",
        "*.bat",
        "*.zip",
        "*.gma",
        "*.psd",
        "*.bz2"
    ]
    
    def __init__(self, addon_folder=None):
        self.addon_folder = addon_folder
        self.data = self._get_default()
    
    def _get_default(self):
        """Get default addon.json structure"""
        return {
            "title": "My GMOD Addon",
            "type": "gamemode",
            "tags": ["fun"],
            "ignore": self.DEFAULT_IGNORE.copy()
        }
    
    def load(self, addon_folder=None):
        """
        Load addon.json from folder
        
        Args:
            addon_folder: Path to addon folder (optional if set in __init__)
            
        Returns:
            bool: True if loaded successfully
        """
        if addon_folder:
            self.addon_folder = addon_folder
        
        if not self.addon_folder:
            return False
        
        json_path = os.path.join(self.addon_folder, "addon.json")
        
        if not os.path.exists(json_path):
            return False
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except Exception as e:
            print(f"Failed to load addon.json: {e}")
            return False
    
    def save(self, addon_folder=None):
        """
        Save addon.json to folder
        
        Args:
            addon_folder: Path to addon folder (optional if set in __init__)
            
        Returns:
            bool: True if saved successfully
        """
        if addon_folder:
            self.addon_folder = addon_folder
        
        if not self.addon_folder:
            return False
        
        json_path = os.path.join(self.addon_folder, "addon.json")
        
        try:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Failed to save addon.json: {e}")
            return False
    
    def validate(self):
        """
        Validate addon.json data
        
        Returns:
            tuple: (valid: bool, errors: list)
        """
        errors = []
        
        # Check required fields
        if not self.data.get('title'):
            errors.append("Title is required")
        
        if not self.data.get('type'):
            errors.append("Type is required")
        elif self.data['type'] not in self.VALID_TYPES:
            errors.append(f"Invalid type. Must be one of: {', '.join(self.VALID_TYPES)}")
        
        if 'tags' not in self.data:
            errors.append("Tags array is required")
        elif not isinstance(self.data['tags'], list):
            errors.append("Tags must be an array")
        
        if 'ignore' not in self.data:
            errors.append("Ignore array is required")
        elif not isinstance(self.data['ignore'], list):
            errors.append("Ignore must be an array")
        
        return len(errors) == 0, errors
    
    def set_title(self, title):
        """Set addon title"""
        self.data['title'] = title
    
    def set_type(self, addon_type):
        """Set addon type"""
        if addon_type in self.VALID_TYPES:
            self.data['type'] = addon_type
            return True
        return False
    
    def set_tags(self, tags):
        """Set tags (accepts list or comma-separated string)"""
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',') if tag.strip()]
        self.data['tags'] = tags
    
    def set_ignore(self, ignore_patterns):
        """Set ignore patterns (accepts list or newline-separated string)"""
        if isinstance(ignore_patterns, str):
            ignore_patterns = [line.strip() for line in ignore_patterns.split('\n') if line.strip()]
        self.data['ignore'] = ignore_patterns
    
    def get_title(self):
        """Get addon title"""
        return self.data.get('title', '')
    
    def get_type(self):
        """Get addon type"""
        return self.data.get('type', 'gamemode')
    
    def get_tags(self):
        """Get tags as list"""
        return self.data.get('tags', [])
    
    def get_tags_string(self):
        """Get tags as comma-separated string"""
        return ', '.join(self.get_tags())
    
    def get_ignore(self):
        """Get ignore patterns as list"""
        return self.data.get('ignore', [])
    
    def get_ignore_string(self):
        """Get ignore patterns as newline-separated string"""
        return '\n'.join(self.get_ignore())
