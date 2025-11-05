import subprocess
import os


# Paths
gmad_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe"
gmpublish_path = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmpublish.exe"


# Get the folder name from user input
folder_name = input("Enter the name of your addon folder: ")
workshop_id = input("Enter the id of your workshop addon: ")

addon_path = os.path.join(r"D:\Steam\GarrysMod\Garrys-Mod-Addon-Uploader", folder_name)  # Adjust the base path as needed
output_gma_path = os.path.join(r"D:\Steam\GarrysMod\Garrys-Mod-Addon-Uploader", f"{folder_name}.gma")  # Output GMA file path
pic_path = os.path.join(addon_path, "pic.jpg")  # pic.jpg file path

# Create GMA file
subprocess.run([gmad_path, "create", "-folder", addon_path, "-out", output_gma_path])


# Upload to Workshop with thumbnail
subprocess.run([gmpublish_path, "update", "-addon", output_gma_path, "-id", workshop_id])

input("")