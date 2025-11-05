"""
Configuration Manager for GMOD Workshop Manager
Handles loading and saving application settings
"""
import json
import os


class Config:
    """Manages application configuration settings"""
    
    DEFAULT_CONFIG = {
        'gmad_path': r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe",
        'gmpublish_path': r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe",
        'base_path': r"D:\Steam\GarrysMod\Garrys-Mod-Addon-Uploader"
    }
    
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.settings = self.load()
    
    def load(self):
        """Load configuration from file or return defaults"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Failed to load config: {e}")
                return self.DEFAULT_CONFIG.copy()
        return self.DEFAULT_CONFIG.copy()
    
    def save(self, settings=None):
        """Save configuration to file"""
        if settings:
            self.settings = settings
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key, default=None):
        """Get a configuration value"""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Set a configuration value"""
        self.settings[key] = value
    
    def update(self, **kwargs):
        """Update multiple configuration values"""
        self.settings.update(kwargs)
