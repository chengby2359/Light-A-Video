import cv2
import numpy as np

def create_video_from_image(image_path, output_video_path, resolution=(512, 512), frame_count=16, fps=8.00):
    duration = frame_count / fps

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, resolution)

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # Resize the image to the specified resolution
    image = cv2.resize(image, resolution)

    # Write the same image for the specified frame count
    for _ in range(frame_count):
        out.write(image)

    # Release the VideoWriter object
    out.release()
    print(f"Video created successfully: {output_video_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert an image into a video.')
    parser.add_argument('image_path', help='Path to the input image file')
    parser.add_argument('output_video_path', help='Path to save the output video file')
    parser.add_argument('--resolution', nargs=2, type=int, default=[512, 512], 
                        help='Video resolution as width height (default: 512 512)')
    parser.add_argument('--frame_count', type=int, default=16, 
                        help='Number of frames in the video (default: 16)')
    parser.add_argument('--fps', type=float, default=8.0, 
                        help='Frames per second (default: 8.0)')
    args = parser.parse_args()

    resolution = (args.resolution[0], args.resolution[1])
    create_video_from_image(args.image_path, args.output_video_path, 
                           resolution=resolution, frame_count=args.frame_count, fps=args.fps)

    # Example usage:
    # python i2v.py /mnt/nas/datasets_tmp/ffhq/images1024x1024/04000/04033.png /mnt/nas/share2/home/cby/Light-A-Video/input_wan/04033.mp4
    # python i2v.py /mnt/nas/datasets_tmp/ffhq/images1024x1024/04000/04033.png /mnt/nas/share2/home/cby/Light-A-Video/input_wan/04033.mp4 --resolution 1024 1024 --frame_count 24 --fps 12