from PIL import Image, ImageDraw, ImageFont
import os

# Create a 512x512 image for Steam Workshop
width, height = 512, 512
image = Image.new('RGB', (width, height), color='#1b2838')  # Steam dark blue

# Draw
draw = ImageDraw.Draw(image)

# Add gradient effect
for i in range(height):
    shade = int(27 + (i / height) * 30)
    draw.line([(0, i), (width, i)], fill=(shade, shade + 11, shade + 29))

# Add text
try:
    # Try to use a larger font
    font_large = ImageFont.truetype("arial.ttf", 60)
    font_small = ImageFont.truetype("arial.ttf", 30)
except:
    # Fallback to default font
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Title text
title = "GMOD Addon"
subtitle = "Workshop Item"

# Get text bounding boxes
title_bbox = draw.textbbox((0, 0), title, font=font_large)
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)

title_width = title_bbox[2] - title_bbox[0]
title_height = title_bbox[3] - title_bbox[1]
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]

# Center text
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

# Save the image
image.save('pic.jpg', 'JPEG', quality=95)
print("✓ pic.jpg created successfully! (512x512)")
print("This is a placeholder image. Replace it with your actual addon artwork.")
