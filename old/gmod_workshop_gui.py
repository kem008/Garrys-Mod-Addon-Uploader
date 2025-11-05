import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import os
import json
import threading


class GMODWorkshopGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GMOD Workshop Manager")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Default paths
        self.gmad_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe"
        self.gmpublish_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe"
        self.base_path = r"D:\Steam\GarrysMod\Garrys-Mod-Addon-Uploader"
        
        self.setup_ui()
        self.load_config()
        
    def setup_ui(self):
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)
        self.addon_json_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.create_tab, text="Create & Publish")
        self.notebook.add(self.update_tab, text="Update Addon")
        self.notebook.add(self.addon_json_tab, text="addon.json Editor")
        self.notebook.add(self.settings_tab, text="Settings")
        
        # Setup each tab
        self.setup_create_tab()
        self.setup_update_tab()
        self.setup_addon_json_tab()
        self.setup_settings_tab()
        
    def setup_create_tab(self):
        frame = ttk.LabelFrame(self.create_tab, text="Create and Publish New Addon", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder path
        ttk.Label(frame, text="Addon Folder:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.create_folder_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.create_folder_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_create_folder).grid(row=0, column=2, pady=5)
        
        # Image file path
        ttk.Label(frame, text="Image (pic.jpg):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.create_image_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.create_image_var, width=50).grid(row=1, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_create_image).grid(row=1, column=2, pady=5)
        
        # Info labels
        info_frame = ttk.Frame(frame)
        info_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky=tk.W)
        ttk.Label(info_frame, text="Note: Image should be JPG format (512x512 recommended)", 
                 foreground="blue").pack(anchor=tk.W)
        ttk.Label(info_frame, text="Ensure addon.json exists in your addon folder!", 
                 foreground="red").pack(anchor=tk.W)
        
        # Action buttons
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)
        ttk.Button(button_frame, text="Create GMA", command=self.create_gma, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Create & Publish", command=self.create_and_publish, width=20).pack(side=tk.LEFT, padx=5)
        
        # Output console
        ttk.Label(frame, text="Output:").grid(row=4, column=0, sticky=tk.NW, pady=5)
        self.create_output = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.create_output.grid(row=5, column=0, columnspan=3, pady=5, padx=5, sticky=tk.NSEW)
        
        frame.grid_rowconfigure(5, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
    def setup_update_tab(self):
        frame = ttk.LabelFrame(self.update_tab, text="Update Existing Workshop Addon", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder path
        ttk.Label(frame, text="Addon Folder:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.update_folder_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.update_folder_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_update_folder).grid(row=0, column=2, pady=5)
        
        # Workshop ID
        ttk.Label(frame, text="Workshop ID:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.workshop_id_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.workshop_id_var, width=50).grid(row=1, column=1, pady=5, padx=5)
        
        # Changelog (optional)
        ttk.Label(frame, text="Changelog:").grid(row=2, column=0, sticky=tk.NW, pady=5)
        self.changelog_text = scrolledtext.ScrolledText(frame, height=5, width=50)
        self.changelog_text.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky=tk.EW)
        
        # Info label
        ttk.Label(frame, text="Note: Find Workshop ID in the addon's Steam Workshop URL", 
                 foreground="blue").grid(row=3, column=0, columnspan=3, pady=5, sticky=tk.W)
        
        # Action buttons
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=10)
        ttk.Button(button_frame, text="Create GMA", command=self.update_create_gma, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Update Workshop", command=self.update_workshop, width=20).pack(side=tk.LEFT, padx=5)
        
        # Output console
        ttk.Label(frame, text="Output:").grid(row=5, column=0, sticky=tk.NW, pady=5)
        self.update_output = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.update_output.grid(row=6, column=0, columnspan=3, pady=5, padx=5, sticky=tk.NSEW)
        
        frame.grid_rowconfigure(6, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
    def setup_addon_json_tab(self):
        frame = ttk.LabelFrame(self.addon_json_tab, text="addon.json Editor", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder
        folder_frame = ttk.Frame(frame)
        folder_frame.pack(fill=tk.X, pady=5)
        ttk.Label(folder_frame, text="Addon Folder:").pack(side=tk.LEFT, padx=5)
        self.json_folder_var = tk.StringVar()
        ttk.Entry(folder_frame, textvariable=self.json_folder_var, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="Browse", command=self.browse_json_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="Load", command=self.load_addon_json).pack(side=tk.LEFT, padx=5)
        
        # Title
        ttk.Label(frame, text="Title:").pack(anchor=tk.W, pady=(10, 0))
        self.json_title_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.json_title_var, width=70).pack(fill=tk.X, pady=5)
        
        # Type
        type_frame = ttk.Frame(frame)
        type_frame.pack(fill=tk.X, pady=5)
        ttk.Label(type_frame, text="Type:").pack(side=tk.LEFT, padx=5)
        self.json_type_var = tk.StringVar(value="gamemode")
        types = ["gamemode", "map", "weapon", "vehicle", "npc", "tool", "effects", "model", "entity", "other"]
        ttk.Combobox(type_frame, textvariable=self.json_type_var, values=types, width=20, state="readonly").pack(side=tk.LEFT, padx=5)
        
        # Tags
        ttk.Label(frame, text="Tags (comma-separated):").pack(anchor=tk.W, pady=(10, 0))
        self.json_tags_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.json_tags_var, width=70).pack(fill=tk.X, pady=5)
        ttk.Label(frame, text="Example: fun, roleplay, realism", foreground="gray").pack(anchor=tk.W)
        
        # Ignore patterns
        ttk.Label(frame, text="Ignore Patterns (one per line):").pack(anchor=tk.W, pady=(10, 0))
        self.json_ignore_text = scrolledtext.ScrolledText(frame, height=10, width=70)
        self.json_ignore_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Default ignore patterns
        default_ignore = ".git/*\n.gitignore\n.gitattributes\n*.md\n*.bat\n*.zip\n*.gma\n*.psd\n*.bz2"
        self.json_ignore_text.insert(1.0, default_ignore)
        
        # Save button
        ttk.Button(frame, text="Save addon.json", command=self.save_addon_json, width=20).pack(pady=10)
        
    def setup_settings_tab(self):
        frame = ttk.LabelFrame(self.settings_tab, text="Application Settings", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # GMAD path
        ttk.Label(frame, text="GMAD.exe Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.gmad_var = tk.StringVar(value=self.gmad_path)
        ttk.Entry(frame, textvariable=self.gmad_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_gmad).grid(row=0, column=2, pady=5)
        
        # GMPUBLISH path
        ttk.Label(frame, text="GMPUBLISH.exe Path:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.gmpublish_var = tk.StringVar(value=self.gmpublish_path)
        ttk.Entry(frame, textvariable=self.gmpublish_var, width=50).grid(row=1, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_gmpublish).grid(row=1, column=2, pady=5)
        
        # Base path
        ttk.Label(frame, text="Base Addons Path:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.base_path_var = tk.StringVar(value=self.base_path)
        ttk.Entry(frame, textvariable=self.base_path_var, width=50).grid(row=2, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_base_path).grid(row=2, column=2, pady=5)
        
        # Save button
        ttk.Button(frame, text="Save Settings", command=self.save_config, width=20).grid(row=3, column=1, pady=20)
        
        # Info
        info_text = """
Settings are saved in config.json in the same directory as this application.

Default Steam GMOD location:
C:\\Program Files (x86)\\Steam\\steamapps\\common\\GarrysMod\\bin\\

If you installed Steam in a different location, browse to find:
- gmad.exe (for creating GMA files)
- gmpublish.exe (for publishing to Workshop)
        """
        ttk.Label(frame, text=info_text, justify=tk.LEFT, foreground="blue").grid(row=4, column=0, columnspan=3, pady=10, sticky=tk.W)
        
    # Browse methods
    def browse_create_folder(self):
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.create_folder_var.set(folder)
            # Auto-find pic.jpg
            pic_path = os.path.join(folder, "pic.jpg")
            if os.path.exists(pic_path):
                self.create_image_var.set(pic_path)
                
    def browse_create_image(self):
        file = filedialog.askopenfilename(title="Select Image", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file:
            self.create_image_var.set(file)
            
    def browse_update_folder(self):
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.update_folder_var.set(folder)
            
    def browse_json_folder(self):
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.json_folder_var.set(folder)
            
    def browse_gmad(self):
        file = filedialog.askopenfilename(title="Select GMAD.exe", filetypes=[("Executable", "*.exe"), ("All files", "*.*")])
        if file:
            self.gmad_var.set(file)
            
    def browse_gmpublish(self):
        file = filedialog.askopenfilename(title="Select GMPUBLISH.exe", filetypes=[("Executable", "*.exe"), ("All files", "*.*")])
        if file:
            self.gmpublish_var.set(file)
            
    def browse_base_path(self):
        folder = filedialog.askdirectory(title="Select Base Addons Path")
        if folder:
            self.base_path_var.set(folder)
    
    # Create & Publish methods
    def create_gma(self):
        folder = self.create_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        folder_name = os.path.basename(folder)
        output_gma = os.path.join(os.path.dirname(folder), f"{folder_name}.gma")
        
        self.create_output.delete(1.0, tk.END)
        self.create_output.insert(tk.END, f"Creating GMA file for: {folder_name}\n")
        self.create_output.insert(tk.END, f"Output: {output_gma}\n\n")
        
        def run():
            try:
                result = subprocess.run(
                    [self.gmad_var.get(), "create", "-folder", folder, "-out", output_gma],
                    capture_output=True, text=True
                )
                self.create_output.insert(tk.END, result.stdout)
                self.create_output.insert(tk.END, result.stderr)
                if result.returncode == 0:
                    self.create_output.insert(tk.END, "\n✓ GMA created successfully!\n")
                    messagebox.showinfo("Success", "GMA file created successfully!")
                else:
                    self.create_output.insert(tk.END, "\n✗ Failed to create GMA!\n")
                    messagebox.showerror("Error", "Failed to create GMA file!")
            except Exception as e:
                self.create_output.insert(tk.END, f"\nError: {str(e)}\n")
                messagebox.showerror("Error", str(e))
                
        threading.Thread(target=run, daemon=True).start()
        
    def create_and_publish(self):
        folder = self.create_folder_var.get()
        image = self.create_image_var.get()
        
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        if not image or not os.path.exists(image):
            messagebox.showerror("Error", "Please select a valid image file!")
            return
            
        folder_name = os.path.basename(folder)
        output_gma = os.path.join(os.path.dirname(folder), f"{folder_name}.gma")
        
        self.create_output.delete(1.0, tk.END)
        self.create_output.insert(tk.END, f"Creating and publishing addon: {folder_name}\n")
        self.create_output.insert(tk.END, f"GMA output: {output_gma}\n")
        self.create_output.insert(tk.END, f"Image: {image}\n\n")
        
        def run():
            try:
                # Create GMA
                self.create_output.insert(tk.END, "Step 1: Creating GMA...\n")
                result1 = subprocess.run(
                    [self.gmad_var.get(), "create", "-folder", folder, "-out", output_gma],
                    capture_output=True, text=True
                )
                self.create_output.insert(tk.END, result1.stdout)
                self.create_output.insert(tk.END, result1.stderr)
                
                if result1.returncode != 0:
                    self.create_output.insert(tk.END, "\n✗ Failed to create GMA!\n")
                    messagebox.showerror("Error", "Failed to create GMA file!")
                    return
                    
                self.create_output.insert(tk.END, "\n✓ GMA created successfully!\n\n")
                
                # Publish to Workshop
                self.create_output.insert(tk.END, "Step 2: Publishing to Workshop...\n")
                result2 = subprocess.run(
                    [self.gmpublish_var.get(), "create", "-addon", output_gma, "-icon", image],
                    capture_output=True, text=True
                )
                self.create_output.insert(tk.END, result2.stdout)
                self.create_output.insert(tk.END, result2.stderr)
                
                if result2.returncode == 0:
                    self.create_output.insert(tk.END, "\n✓ Successfully published to Workshop!\n")
                    messagebox.showinfo("Success", "Addon published to Workshop successfully!")
                else:
                    self.create_output.insert(tk.END, "\n✗ Failed to publish to Workshop!\n")
                    messagebox.showerror("Error", "Failed to publish to Workshop!")
            except Exception as e:
                self.create_output.insert(tk.END, f"\nError: {str(e)}\n")
                messagebox.showerror("Error", str(e))
                
        threading.Thread(target=run, daemon=True).start()
        
    # Update methods
    def update_create_gma(self):
        folder = self.update_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        folder_name = os.path.basename(folder)
        output_gma = os.path.join(os.path.dirname(folder), f"{folder_name}.gma")
        
        self.update_output.delete(1.0, tk.END)
        self.update_output.insert(tk.END, f"Creating GMA file for: {folder_name}\n")
        self.update_output.insert(tk.END, f"Output: {output_gma}\n\n")
        
        def run():
            try:
                result = subprocess.run(
                    [self.gmad_var.get(), "create", "-folder", folder, "-out", output_gma],
                    capture_output=True, text=True
                )
                self.update_output.insert(tk.END, result.stdout)
                self.update_output.insert(tk.END, result.stderr)
                if result.returncode == 0:
                    self.update_output.insert(tk.END, "\n✓ GMA created successfully!\n")
                    messagebox.showinfo("Success", "GMA file created successfully!")
                else:
                    self.update_output.insert(tk.END, "\n✗ Failed to create GMA!\n")
                    messagebox.showerror("Error", "Failed to create GMA file!")
            except Exception as e:
                self.update_output.insert(tk.END, f"\nError: {str(e)}\n")
                messagebox.showerror("Error", str(e))
                
        threading.Thread(target=run, daemon=True).start()
        
    def update_workshop(self):
        folder = self.update_folder_var.get()
        workshop_id = self.workshop_id_var.get()
        
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        if not workshop_id:
            messagebox.showerror("Error", "Please enter a Workshop ID!")
            return
            
        folder_name = os.path.basename(folder)
        output_gma = os.path.join(os.path.dirname(folder), f"{folder_name}.gma")
        
        self.update_output.delete(1.0, tk.END)
        self.update_output.insert(tk.END, f"Updating workshop addon: {workshop_id}\n")
        self.update_output.insert(tk.END, f"GMA output: {output_gma}\n\n")
        
        def run():
            try:
                # Create GMA
                self.update_output.insert(tk.END, "Step 1: Creating GMA...\n")
                result1 = subprocess.run(
                    [self.gmad_var.get(), "create", "-folder", folder, "-out", output_gma],
                    capture_output=True, text=True
                )
                self.update_output.insert(tk.END, result1.stdout)
                self.update_output.insert(tk.END, result1.stderr)
                
                if result1.returncode != 0:
                    self.update_output.insert(tk.END, "\n✗ Failed to create GMA!\n")
                    messagebox.showerror("Error", "Failed to create GMA file!")
                    return
                    
                self.update_output.insert(tk.END, "\n✓ GMA created successfully!\n\n")
                
                # Update Workshop
                self.update_output.insert(tk.END, "Step 2: Updating Workshop addon...\n")
                result2 = subprocess.run(
                    [self.gmpublish_var.get(), "update", "-addon", output_gma, "-id", workshop_id],
                    capture_output=True, text=True
                )
                self.update_output.insert(tk.END, result2.stdout)
                self.update_output.insert(tk.END, result2.stderr)
                
                if result2.returncode == 0:
                    self.update_output.insert(tk.END, "\n✓ Workshop addon updated successfully!\n")
                    messagebox.showinfo("Success", "Workshop addon updated successfully!")
                else:
                    self.update_output.insert(tk.END, "\n✗ Failed to update Workshop addon!\n")
                    messagebox.showerror("Error", "Failed to update Workshop addon!")
            except Exception as e:
                self.update_output.insert(tk.END, f"\nError: {str(e)}\n")
                messagebox.showerror("Error", str(e))
                
        threading.Thread(target=run, daemon=True).start()
        
    # addon.json methods
    def load_addon_json(self):
        folder = self.json_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        json_path = os.path.join(folder, "addon.json")
        if not os.path.exists(json_path):
            messagebox.showwarning("Warning", "addon.json not found. Creating new one.")
            return
            
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            self.json_title_var.set(data.get('title', ''))
            self.json_type_var.set(data.get('type', 'gamemode'))
            
            tags = data.get('tags', [])
            self.json_tags_var.set(', '.join(tags))
            
            ignore = data.get('ignore', [])
            self.json_ignore_text.delete(1.0, tk.END)
            self.json_ignore_text.insert(1.0, '\n'.join(ignore))
            
            messagebox.showinfo("Success", "addon.json loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load addon.json: {str(e)}")
            
    def save_addon_json(self):
        folder = self.json_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
            
        title = self.json_title_var.get()
        if not title:
            messagebox.showerror("Error", "Please enter a title!")
            return
            
        addon_type = self.json_type_var.get()
        tags_str = self.json_tags_var.get()
        tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
        
        ignore_str = self.json_ignore_text.get(1.0, tk.END)
        ignore = [line.strip() for line in ignore_str.split('\n') if line.strip()]
        
        data = {
            "title": title,
            "type": addon_type,
            "tags": tags,
            "ignore": ignore
        }
        
        json_path = os.path.join(folder, "addon.json")
        
        try:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo("Success", f"addon.json saved to:\n{json_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save addon.json: {str(e)}")
            
    # Config methods
    def load_config(self):
        config_path = "config.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    self.gmad_path = config.get('gmad_path', self.gmad_path)
                    self.gmpublish_path = config.get('gmpublish_path', self.gmpublish_path)
                    self.base_path = config.get('base_path', self.base_path)
                    
                    self.gmad_var.set(self.gmad_path)
                    self.gmpublish_var.set(self.gmpublish_path)
                    self.base_path_var.set(self.base_path)
            except:
                pass
                
    def save_config(self):
        config = {
            'gmad_path': self.gmad_var.get(),
            'gmpublish_path': self.gmpublish_var.get(),
            'base_path': self.base_path_var.get()
        }
        
        try:
            with open("config.json", 'w') as f:
                json.dump(config, f, indent=4)
            messagebox.showinfo("Success", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GMODWorkshopGUI(root)
    root.mainloop()
