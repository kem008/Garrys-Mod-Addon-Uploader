"""
Settings Tab for GUI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class SettingsTab:
    """Tab for application settings"""
    
    def __init__(self, parent, config):
        self.parent = parent
        self.config = config
        
        self.gmad_var = tk.StringVar(value=config.get('gmad_path'))
        self.gmpublish_var = tk.StringVar(value=config.get('gmpublish_path'))
        self.base_path_var = tk.StringVar(value=config.get('base_path'))
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI components"""
        frame = ttk.LabelFrame(self.parent, text="Application Settings", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # GMAD path
        ttk.Label(frame, text="GMAD.exe Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.gmad_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_gmad).grid(row=0, column=2, pady=5)
        
        # GMPUBLISH path
        ttk.Label(frame, text="GMPUBLISH.exe Path:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.gmpublish_var, width=50).grid(row=1, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_gmpublish).grid(row=1, column=2, pady=5)
        
        # Base path
        ttk.Label(frame, text="Base Addons Path:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.base_path_var, width=50).grid(row=2, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_base_path).grid(row=2, column=2, pady=5)
        
        # Save button
        ttk.Button(frame, text="Save Settings", command=self.save_settings, width=20).grid(row=3, column=1, pady=20)
        
        # Info
        info_text = """
Settings are saved in config.json in the same directory as this application.

Default Steam GMOD location:
C:\\Program Files (x86)\\Steam\\steamapps\\common\\GarrysMod\\bin\\

If you installed Steam in a different location, browse to find:
- gmad.exe (for creating GMA files)
- gmpublish.exe (for publishing to Workshop)
        """
        ttk.Label(frame, text=info_text, justify=tk.LEFT, foreground="blue").grid(
            row=4, column=0, columnspan=3, pady=10, sticky=tk.W
        )
    
    def browse_gmad(self):
        """Browse for gmad.exe"""
        file = filedialog.askopenfilename(
            title="Select GMAD.exe", 
            filetypes=[("Executable", "*.exe"), ("All files", "*.*")]
        )
        if file:
            self.gmad_var.set(file)
    
    def browse_gmpublish(self):
        """Browse for gmpublish.exe"""
        file = filedialog.askopenfilename(
            title="Select GMPUBLISH.exe", 
            filetypes=[("Executable", "*.exe"), ("All files", "*.*")]
        )
        if file:
            self.gmpublish_var.set(file)
    
    def browse_base_path(self):
        """Browse for base addons path"""
        folder = filedialog.askdirectory(title="Select Base Addons Path")
        if folder:
            self.base_path_var.set(folder)
    
    def save_settings(self):
        """Save settings to config file"""
        self.config.update(
            gmad_path=self.gmad_var.get(),
            gmpublish_path=self.gmpublish_var.get(),
            base_path=self.base_path_var.get()
        )
        
        if self.config.save():
            messagebox.showinfo("Success", "Settings saved successfully!")
        else:
            messagebox.showerror("Error", "Failed to save settings!")
