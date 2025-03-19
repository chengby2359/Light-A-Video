import os
from PIL import Image

def resize_image(input_path, output_path, size=(800, 600)):
    """
    Resize an image to the specified size and save it
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the resized image
        size (tuple): Width and height to resize to, default (800, 600)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save the resized image
            resized_img.save(output_path)
            print(f"Image resized to {size} and saved to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Resize an image to a fixed size")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the resized image")
    parser.add_argument("--width", type=int, default=512, help="Width of the resized image")
    parser.add_argument("--height", type=int, default=768, help="Height of the resized image")
    
    args = parser.parse_args()
    # import pdb;pdb.set_trace()
    resize_image(args.input, args.output, (args.width, args.height))