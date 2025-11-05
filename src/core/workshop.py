"""
Workshop Operations for GMOD addons
Handles GMA creation, publishing, and updating
"""
import subprocess
import os


class WorkshopManager:
    """Manages Workshop operations for GMOD addons"""
    
    def __init__(self, gmad_path, gmpublish_path):
        self.gmad_path = gmad_path
        self.gmpublish_path = gmpublish_path
    
    def create_gma(self, addon_folder, output_path):
        """
        Create a GMA file from addon folder
        
        Args:
            addon_folder: Path to addon source folder
            output_path: Path for output GMA file
            
        Returns:
            tuple: (success: bool, output: str, error: str)
        """
        try:
            result = subprocess.run(
                [self.gmad_path, "create", "-folder", addon_folder, "-out", output_path],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            success = result.returncode == 0
            return success, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Operation timed out"
        except Exception as e:
            return False, "", str(e)
    
    def publish_addon(self, gma_path, image_path):
        """
        Publish a new addon to Steam Workshop
        
        Args:
            gma_path: Path to GMA file
            image_path: Path to workshop thumbnail image
            
        Returns:
            tuple: (success: bool, output: str, error: str)
        """
        try:
            result = subprocess.run(
                [self.gmpublish_path, "create", "-addon", gma_path, "-icon", image_path],
                capture_output=True,
                text=True,
                timeout=300  # Publishing can take longer
            )
            
            success = result.returncode == 0
            return success, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Publishing timed out"
        except Exception as e:
            return False, "", str(e)
    
    def update_addon(self, gma_path, workshop_id):
        """
        Update an existing Workshop addon
        
        Args:
            gma_path: Path to GMA file
            workshop_id: Steam Workshop ID of the addon
            
        Returns:
            tuple: (success: bool, output: str, error: str)
        """
        try:
            result = subprocess.run(
                [self.gmpublish_path, "update", "-addon", gma_path, "-id", str(workshop_id)],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            success = result.returncode == 0
            return success, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Update timed out"
        except Exception as e:
            return False, "", str(e)
    
    def create_and_publish(self, addon_folder, image_path):
        """
        Create GMA and publish in one operation
        
        Args:
            addon_folder: Path to addon source folder
            image_path: Path to workshop thumbnail image
            
        Returns:
            tuple: (success: bool, messages: list)
        """
        messages = []
        folder_name = os.path.basename(addon_folder)
        output_gma = os.path.join(os.path.dirname(addon_folder), f"{folder_name}.gma")
        
        # Step 1: Create GMA
        messages.append("Creating GMA file...")
        success, stdout, stderr = self.create_gma(addon_folder, output_gma)
        messages.append(stdout)
        if stderr:
            messages.append(stderr)
        
        if not success:
            messages.append("✗ Failed to create GMA")
            return False, messages
        
        messages.append("✓ GMA created successfully")
        
        # Step 2: Publish
        messages.append("\nPublishing to Workshop...")
        success, stdout, stderr = self.publish_addon(output_gma, image_path)
        messages.append(stdout)
        if stderr:
            messages.append(stderr)
        
        if not success:
            messages.append("✗ Failed to publish to Workshop")
            return False, messages
        
        messages.append("✓ Successfully published to Workshop!")
        return True, messages
    
    def create_and_update(self, addon_folder, workshop_id):
        """
        Create GMA and update existing Workshop item
        
        Args:
            addon_folder: Path to addon source folder
            workshop_id: Steam Workshop ID
            
        Returns:
            tuple: (success: bool, messages: list)
        """
        messages = []
        folder_name = os.path.basename(addon_folder)
        output_gma = os.path.join(os.path.dirname(addon_folder), f"{folder_name}.gma")
        
        # Step 1: Create GMA
        messages.append("Creating GMA file...")
        success, stdout, stderr = self.create_gma(addon_folder, output_gma)
        messages.append(stdout)
        if stderr:
            messages.append(stderr)
        
        if not success:
            messages.append("✗ Failed to create GMA")
            return False, messages
        
        messages.append("✓ GMA created successfully")
        
        # Step 2: Update
        messages.append("\nUpdating Workshop addon...")
        success, stdout, stderr = self.update_addon(output_gma, workshop_id)
        messages.append(stdout)
        if stderr:
            messages.append(stderr)
        
        if not success:
            messages.append("✗ Failed to update Workshop addon")
            return False, messages
        
        messages.append("✓ Workshop addon updated successfully!")
        return True, messages
