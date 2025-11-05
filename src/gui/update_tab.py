"""
Update Tab for GUI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os


class UpdateTab:
    """Tab for updating existing Workshop addons"""
    
    def __init__(self, parent, workshop_manager, config):
        self.parent = parent
        self.workshop_manager = workshop_manager
        self.config = config
        
        self.update_folder_var = tk.StringVar()
        self.workshop_id_var = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI components"""
        frame = ttk.LabelFrame(self.parent, text="Update Existing Workshop Addon", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder path
        ttk.Label(frame, text="Addon Folder:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.update_folder_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_folder).grid(row=0, column=2, pady=5)
        
        # Workshop ID
        ttk.Label(frame, text="Workshop ID:").grid(row=1, column=0, sticky=tk.W, pady=5)
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
        ttk.Button(button_frame, text="Create GMA Only", command=self.create_gma, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Update Workshop", command=self.update_workshop, width=20).pack(side=tk.LEFT, padx=5)
        
        # Output console
        ttk.Label(frame, text="Output:").grid(row=5, column=0, sticky=tk.NW, pady=5)
        self.output = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.output.grid(row=6, column=0, columnspan=3, pady=5, padx=5, sticky=tk.NSEW)
        
        frame.grid_rowconfigure(6, weight=1)
        frame.grid_columnconfigure(1, weight=1)
    
    def browse_folder(self):
        """Browse for addon folder"""
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.update_folder_var.set(folder)
    
    def log(self, message):
        """Add message to output console"""
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)
    
    def clear_output(self):
        """Clear output console"""
        self.output.delete(1.0, tk.END)
    
    def create_gma(self):
        """Create GMA file only"""
        folder = self.update_folder_var.get()
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
        
        self.clear_output()
        folder_name = os.path.basename(folder)
        output_gma = os.path.join(os.path.dirname(folder), f"{folder_name}.gma")
        
        self.log(f"Creating GMA file for: {folder_name}")
        self.log(f"Output: {output_gma}\n")
        
        def run():
            success, stdout, stderr = self.workshop_manager.create_gma(folder, output_gma)
            self.log(stdout)
            if stderr:
                self.log(stderr)
            
            if success:
                self.log("\n✓ GMA created successfully!")
                messagebox.showinfo("Success", "GMA file created successfully!")
            else:
                self.log("\n✗ Failed to create GMA!")
                messagebox.showerror("Error", "Failed to create GMA file!")
        
        threading.Thread(target=run, daemon=True).start()
    
    def update_workshop(self):
        """Update Workshop addon"""
        folder = self.update_folder_var.get()
        workshop_id = self.workshop_id_var.get()
        
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
        
        if not workshop_id:
            messagebox.showerror("Error", "Please enter a Workshop ID!")
            return
        
        self.clear_output()
        self.log(f"Updating workshop addon: {workshop_id}\n")
        
        def run():
            success, messages = self.workshop_manager.create_and_update(folder, workshop_id)
            
            for msg in messages:
                self.log(msg)
            
            if success:
                messagebox.showinfo("Success", "Workshop addon updated successfully!")
            else:
                messagebox.showerror("Error", "Failed to update Workshop addon!")
        
        threading.Thread(target=run, daemon=True).start()
