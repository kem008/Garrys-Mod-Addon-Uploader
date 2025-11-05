"""
addon.json Editor Tab for GUI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.addon_json import AddonJSON


class AddonJSONTab:
    """Tab for editing addon.json files"""
    
    # Common GMOD Workshop Tags
    COMMON_TAGS = [
        "fun", "roleplay", "scenic", "movie", "realism", "cartoon",
        "water", "comic", "build", "comic", "toy"
    ]
    
    def __init__(self, parent, config):
        self.parent = parent
        self.config = config
        self.addon_json = AddonJSON()
        
        self.json_folder_var = tk.StringVar()
        self.json_title_var = tk.StringVar()
        self.json_type_var = tk.StringVar(value="gamemode")
        
        # Tag checkboxes variables
        self.tag_vars = {}
        for tag in self.COMMON_TAGS:
            self.tag_vars[tag] = tk.BooleanVar(value=False)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI components"""
        frame = ttk.LabelFrame(self.parent, text="addon.json Editor", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder
        folder_frame = ttk.Frame(frame)
        folder_frame.pack(fill=tk.X, pady=5)
        ttk.Label(folder_frame, text="Addon Folder:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(folder_frame, textvariable=self.json_folder_var, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="Load", command=self.load_json).pack(side=tk.LEFT, padx=5)
        
        # Title
        ttk.Label(frame, text="Title:").pack(anchor=tk.W, pady=(10, 0))
        ttk.Entry(frame, textvariable=self.json_title_var, width=70).pack(fill=tk.X, pady=5)
        
        # Type
        type_frame = ttk.Frame(frame)
        type_frame.pack(fill=tk.X, pady=5)
        ttk.Label(type_frame, text="Type:").pack(side=tk.LEFT, padx=5)
        type_combo = ttk.Combobox(
            type_frame, 
            textvariable=self.json_type_var, 
            values=AddonJSON.VALID_TYPES, 
            width=20, 
            state="readonly"
        )
        type_combo.pack(side=tk.LEFT, padx=5)
        
        # Tags with checkboxes
        tags_label_frame = ttk.LabelFrame(frame, text="Workshop Tags", padding=10)
        tags_label_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(tags_label_frame, 
                 text="Select tags for your addon (select up to 2):", 
                 foreground="gray").pack(anchor=tk.W, pady=(0, 5))
        
        # Create grid of checkboxes for tags
        tags_grid = ttk.Frame(tags_label_frame)
        tags_grid.pack(fill=tk.X)
        
        row = 0
        col = 0
        for tag in self.COMMON_TAGS:
            cb = ttk.Checkbutton(
                tags_grid, 
                text=tag.capitalize(), 
                variable=self.tag_vars[tag],
                command=self.on_tag_change
            )
            cb.grid(row=row, column=col, sticky=tk.W, padx=10, pady=2)
            col += 1
            if col > 4:  # 5 columns
                col = 0
                row += 1
        
        # Ignore patterns
        ttk.Label(frame, text="Ignore Patterns (one per line):").pack(anchor=tk.W, pady=(10, 0))
        self.json_ignore_text = scrolledtext.ScrolledText(frame, height=10, width=70)
        self.json_ignore_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Default ignore patterns
        self.json_ignore_text.insert(1.0, '\n'.join(AddonJSON.DEFAULT_IGNORE))
        
        # Buttons
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Save addon.json", command=self.save_json, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Validate", command=self.validate_json, width=20).pack(side=tk.LEFT, padx=5)
    
    def browse_folder(self):
        """Browse for addon folder"""
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.json_folder_var.set(folder)
    
    def on_tag_change(self):
        """Handle tag checkbox changes - limit to 2 tags"""
        selected = sum(1 for var in self.tag_vars.values() if var.get())
        if selected > 2:
            messagebox.showwarning("Tag Limit", "You can only select up to 2 tags!")
    
    def get_selected_tags(self):
        """Get list of selected tags"""
        return [tag for tag, var in self.tag_vars.items() if var.get()]
    
    def set_selected_tags(self, tags_string):
        """Set checkboxes based on comma-separated tags string"""
        # First uncheck all
        for var in self.tag_vars.values():
            var.set(False)
        
        # Then check the ones in the string
        if tags_string:
            tags = [tag.strip().lower() for tag in tags_string.split(',')]
            for tag in tags:
                if tag in self.tag_vars:
                    self.tag_vars[tag].set(True)
    
    def load_json(self):
        """Load addon.json from folder"""
        folder = self.json_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
        
        self.addon_json = AddonJSON(folder)
        if self.addon_json.load():
            self.json_title_var.set(self.addon_json.get_title())
            self.json_type_var.set(self.addon_json.get_type())
            
            # Set tag checkboxes based on loaded tags
            self.set_selected_tags(self.addon_json.get_tags_string())
            
            self.json_ignore_text.delete(1.0, tk.END)
            self.json_ignore_text.insert(1.0, self.addon_json.get_ignore_string())
            
            messagebox.showinfo("Success", "addon.json loaded successfully!")
        else:
            messagebox.showwarning("Warning", "addon.json not found. You can create a new one.")
    
    def save_json(self):
        """Save addon.json to folder"""
        folder = self.json_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
        
        title = self.json_title_var.get()
        if not title:
            messagebox.showerror("Error", "Please enter a title!")
            return
        
        # Update addon_json object
        self.addon_json.set_title(title)
        self.addon_json.set_type(self.json_type_var.get())
        
        # Get selected tags and convert to comma-separated string
        selected_tags = self.get_selected_tags()
        self.addon_json.set_tags(', '.join(selected_tags))
        
        self.addon_json.set_ignore(self.json_ignore_text.get(1.0, tk.END))
        
        # Validate
        valid, errors = self.addon_json.validate()
        if not valid:
            messagebox.showerror("Validation Error", "\n".join(errors))
            return
        
        # Save
        if self.addon_json.save(folder):
            messagebox.showinfo("Success", f"addon.json saved to:\n{os.path.join(folder, 'addon.json')}")
        else:
            messagebox.showerror("Error", "Failed to save addon.json!")
    
    def validate_json(self):
        """Validate current addon.json data"""
        # Update addon_json object with current values
        self.addon_json.set_title(self.json_title_var.get())
        self.addon_json.set_type(self.json_type_var.get())
        
        # Get selected tags and convert to comma-separated string
        selected_tags = self.get_selected_tags()
        self.addon_json.set_tags(', '.join(selected_tags))
        
        self.addon_json.set_ignore(self.json_ignore_text.get(1.0, tk.END))
        
        valid, errors = self.addon_json.validate()
        
        if valid:
            messagebox.showinfo("Validation", "✓ addon.json is valid!")
        else:
            messagebox.showerror("Validation Errors", "\n".join(errors))
