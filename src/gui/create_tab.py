"""
Create & Publish Tab for GUI
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os


class CreatePublishTab:
    """Tab for creating and publishing new addons"""
    
    def __init__(self, parent, workshop_manager, config):
        self.parent = parent
        self.workshop_manager = workshop_manager
        self.config = config
        
        self.create_folder_var = tk.StringVar()
        self.create_image_var = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI components"""
        frame = ttk.LabelFrame(self.parent, text="Create and Publish New Addon", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Addon folder path
        ttk.Label(frame, text="Addon Folder:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.create_folder_var, width=50).grid(row=0, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_folder).grid(row=0, column=2, pady=5)
        
        # Image file path
        ttk.Label(frame, text="Image (pic.jpg):").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(frame, textvariable=self.create_image_var, width=50).grid(row=1, column=1, pady=5, padx=5)
        ttk.Button(frame, text="Browse", command=self.browse_image).grid(row=1, column=2, pady=5)
        
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
        ttk.Button(button_frame, text="Create GMA Only", command=self.create_gma, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Create & Publish", command=self.create_and_publish, width=20).pack(side=tk.LEFT, padx=5)
        
        # Output console
        ttk.Label(frame, text="Output:").grid(row=4, column=0, sticky=tk.NW, pady=5)
        self.output = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.output.grid(row=5, column=0, columnspan=3, pady=5, padx=5, sticky=tk.NSEW)
        
        frame.grid_rowconfigure(5, weight=1)
        frame.grid_columnconfigure(1, weight=1)
    
    def browse_folder(self):
        """Browse for addon folder"""
        folder = filedialog.askdirectory(title="Select Addon Folder")
        if folder:
            self.create_folder_var.set(folder)
            # Auto-find pic.jpg
            pic_path = os.path.join(folder, "pic.jpg")
            if os.path.exists(pic_path):
                self.create_image_var.set(pic_path)
    
    def browse_image(self):
        """Browse for image file"""
        file = filedialog.askopenfilename(
            title="Select Image", 
            filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file:
            self.create_image_var.set(file)
    
    def log(self, message):
        """Add message to output console"""
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)
    
    def clear_output(self):
        """Clear output console"""
        self.output.delete(1.0, tk.END)
    
    def create_gma(self):
        """Create GMA file only"""
        folder = self.create_folder_var.get()
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
    
    def create_and_publish(self):
        """Create GMA and publish to Workshop"""
        folder = self.create_folder_var.get()
        image = self.create_image_var.get()
        
        if not folder or not os.path.exists(folder):
            messagebox.showerror("Error", "Please select a valid addon folder!")
            return
        
        if not image or not os.path.exists(image):
            messagebox.showerror("Error", "Please select a valid image file!")
            return
        
        self.clear_output()
        self.log(f"Creating and publishing addon: {os.path.basename(folder)}")
        self.log(f"Image: {image}\n")
        
        def run():
            success, messages = self.workshop_manager.create_and_publish(folder, image)
            
            for msg in messages:
                self.log(msg)
            
            if success:
                messagebox.showinfo("Success", "Addon published to Workshop successfully!")
            else:
                messagebox.showerror("Error", "Failed to publish addon!")
        
        threading.Thread(target=run, daemon=True).start()
