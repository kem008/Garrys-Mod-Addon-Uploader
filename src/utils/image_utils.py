"""
Image utilities for workshop thumbnails
"""
from PIL import Image, ImageDraw, ImageFont
import os


def create_placeholder_image(output_path, title="GMOD Addon", subtitle="Workshop Item"):
    """
    Create a placeholder workshop image
    
    Args:
        output_path: Path to save the image
        title: Main title text
        subtitle: Subtitle text
        
    Returns:
        bool: True if successful
    """
    try:
        # Create a 512x512 image for Steam Workshop
        width, height = 512, 512
        image = Image.new('RGB', (width, height), color='#1b2838')
        
        draw = ImageDraw.Draw(image)
        
        # Add gradient effect
        for i in range(height):
            shade = int(27 + (i / height) * 30)
            draw.line([(0, i), (width, i)], fill=(shade, shade + 11, shade + 29))
        
        # Load fonts
        try:
            font_large = ImageFont.truetype("arial.ttf", 60)
            font_small = ImageFont.truetype("arial.ttf", 30)
        except:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Calculate text positions
        title_bbox = draw.textbbox((0, 0), title, font=font_large)
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        
        title_x = (width - title_width) // 2
        title_y = (height - title_height) // 2 - 40
        
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = title_y + title_height + 20
        
        # Draw text with shadow
        shadow_offset = 3
        draw.text((title_x + shadow_offset, title_y + shadow_offset), title, fill='#000000', font=font_large)
        draw.text((title_x, title_y), title, fill='#66c0f4', font=font_large)
        
        draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, fill='#000000', font=font_small)
        draw.text((subtitle_x, subtitle_y), subtitle, fill='#c7d5e0', font=font_small)
        
        # Add border
        border_width = 2
        draw.rectangle([(border_width, border_width), (width - border_width, height - border_width)], 
                      outline='#66c0f4', width=border_width)
        
        # Save
        image.save(output_path, 'JPEG', quality=95)
        return True
    except Exception as e:
        print(f"Failed to create image: {e}")
        return False


def validate_workshop_image(image_path):
    """
    Validate if image meets Workshop requirements
    
    Args:
        image_path: Path to image file
        
    Returns:
        tuple: (valid: bool, errors: list)
    """
    errors = []
    
    if not os.path.exists(image_path):
        errors.append("Image file does not exist")
        return False, errors
    
    try:
        img = Image.open(image_path)
        
        # Check format
        if img.format not in ['JPEG', 'JPG']:
            errors.append("Image must be JPEG format")
        
        # Check size (recommended 512x512, but allow variations)
        width, height = img.size
        if width < 256 or height < 256:
            errors.append("Image is too small (minimum 256x256 recommended)")
        
        if width > 1024 or height > 1024:
            errors.append("Image is too large (maximum 1024x1024 recommended)")
        
        # Check file size
        file_size = os.path.getsize(image_path)
        if file_size > 1024 * 1024:  # 1MB
            errors.append("Image file size exceeds 1MB")
        
        img.close()
        
    except Exception as e:
        errors.append(f"Failed to validate image: {str(e)}")
    
    return len(errors) == 0, errors


def resize_image(input_path, output_path, size=(512, 512)):
    """
    Resize image to specified dimensions
    
    Args:
        input_path: Input image path
        output_path: Output image path
        size: Target size tuple (width, height)
        
    Returns:
        bool: True if successful
    """
    try:
        img = Image.open(input_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path, 'JPEG', quality=95)
        img.close()
        return True
    except Exception as e:
        print(f"Failed to resize image: {e}")
        return False
