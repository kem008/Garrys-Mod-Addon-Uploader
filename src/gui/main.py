"""
Main GUI Application for GMOD Workshop Manager
"""
import tkinter as tk
from tkinter import ttk
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core import Config, WorkshopManager
from gui.create_tab import CreatePublishTab
from gui.update_tab import UpdateTab
from gui.addon_json_tab import AddonJSONTab
from gui.settings_tab import SettingsTab


class GMODWorkshopGUI:
    """Main GUI Application"""
    
    # GMOD Color Scheme
    GMOD_BLUE = "#1E88E5"
    GMOD_DARK_BLUE = "#1565C0"
    GMOD_LIGHT_BLUE = "#42A5F5"
    GMOD_WHITE = "#FFFFFF"
    GMOD_LIGHT_GRAY = "#F5F5F5"
    GMOD_TEXT = "#212121"
    
    def __init__(self, root):
        self.root = root
        self.root.title("GMOD Workshop Manager")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Apply GMOD color scheme
        self.apply_gmod_style()
        
        # Load configuration
        self.config = Config()
        
        # Initialize workshop manager
        self.workshop_manager = WorkshopManager(
            self.config.get('gmad_path'),
            self.config.get('gmpublish_path')
        )
        
        self.setup_ui()
    
    def apply_gmod_style(self):
        """Apply GMOD-style colors to the application"""
        style = ttk.Style()
        style.theme_use('clam')  # Use clam theme for better customization
        
        # Configure main background
        self.root.configure(bg=self.GMOD_LIGHT_GRAY)
        
        # Configure notebook (tabs)
        style.configure('TNotebook', background=self.GMOD_LIGHT_GRAY, borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background=self.GMOD_WHITE,
                       foreground=self.GMOD_TEXT,
                       padding=[20, 10],
                       font=('Segoe UI', 10, 'bold'))
        style.map('TNotebook.Tab',
                 background=[('selected', self.GMOD_BLUE)],
                 foreground=[('selected', self.GMOD_WHITE)])
        
        # Configure frames
        style.configure('TFrame', background=self.GMOD_WHITE)
        style.configure('TLabelframe', background=self.GMOD_WHITE, 
                       foreground=self.GMOD_DARK_BLUE,
                       borderwidth=2,
                       relief='solid')
        style.configure('TLabelframe.Label', 
                       background=self.GMOD_WHITE,
                       foreground=self.GMOD_DARK_BLUE,
                       font=('Segoe UI', 10, 'bold'))
        
        # Configure buttons
        style.configure('TButton',
                       background=self.GMOD_BLUE,
                       foreground=self.GMOD_WHITE,
                       borderwidth=0,
                       focuscolor='none',
                       font=('Segoe UI', 9, 'bold'),
                       padding=[10, 5])
        style.map('TButton',
                 background=[('active', self.GMOD_LIGHT_BLUE), ('pressed', self.GMOD_DARK_BLUE)])
        
        # Configure labels
        style.configure('TLabel', 
                       background=self.GMOD_WHITE,
                       foreground=self.GMOD_TEXT,
                       font=('Segoe UI', 9))
        
        # Configure entry fields
        style.configure('TEntry',
                       fieldbackground=self.GMOD_WHITE,
                       foreground=self.GMOD_TEXT,
                       borderwidth=2)
        
        # Configure checkbuttons
        style.configure('TCheckbutton',
                       background=self.GMOD_WHITE,
                       foreground=self.GMOD_TEXT,
                       font=('Segoe UI', 9))
        style.map('TCheckbutton',
                 background=[('active', self.GMOD_WHITE)])
        
        # Configure combobox (dropdown)
        style.configure('TCombobox',
                       fieldbackground=self.GMOD_WHITE,
                       background=self.GMOD_BLUE,
                       foreground=self.GMOD_TEXT,
                       borderwidth=2)
    
    def setup_ui(self):
        """Setup the main UI"""
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tab frames
        create_frame = ttk.Frame(self.notebook)
        update_frame = ttk.Frame(self.notebook)
        addon_json_frame = ttk.Frame(self.notebook)
        settings_frame = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(create_frame, text="Create & Publish")
        self.notebook.add(update_frame, text="Update Addon")
        self.notebook.add(addon_json_frame, text="addon.json Editor")
        self.notebook.add(settings_frame, text="Settings")
        
        # Initialize tab controllers
        self.create_tab = CreatePublishTab(create_frame, self.workshop_manager, self.config)
        self.update_tab = UpdateTab(update_frame, self.workshop_manager, self.config)
        self.addon_json_tab = AddonJSONTab(addon_json_frame, self.config)
        self.settings_tab = SettingsTab(settings_frame, self.config)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = GMODWorkshopGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
