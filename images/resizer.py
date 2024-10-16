from PIL import Image

def compress_and_resize_image(input_path, output_path, quality=20, new_width=None, new_height=None):
    # Open an image file
    with Image.open(input_path) as img:
        # Convert the image to RGB if it's in a different mode
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize the image if new dimensions are provided
        if new_width and new_height:
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
        
        # Compress the image by adjusting the quality
        img.save(output_path, "JPEG", quality=quality)

# Usage example
compress_and_resize_image('images\profile.png', 'images\photo.jpg', quality=20, new_width=380, new_height=380)
