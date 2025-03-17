import os
import cv2
from moviepy.editor import VideoFileClip

def get_video_info(video_path):
    """Extract information from an MP4 video file"""
    if not os.path.exists(video_path):
        print(f"Error: File not found: {video_path}")
        return
    
    # Get file size
    file_size_bytes = os.path.getsize(video_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    
    # Use OpenCV to get basic properties
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video: {video_path}")
        return
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Get codec information
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
    
    # Calculate duration from OpenCV
    duration_seconds = frame_count / fps if fps > 0 else 0
    
    # Try to get more accurate duration with MoviePy
    try:
        clip = VideoFileClip(video_path)
        duration_seconds = clip.duration
        clip.close()
    except Exception as e:
        print(f"Note: Using OpenCV duration calculation due to MoviePy error: {e}")
    
    # Format duration as HH:MM:SS
    hours = int(duration_seconds // 3600)
    minutes = int((duration_seconds % 3600) // 60)
    seconds = int(duration_seconds % 60)
    duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    # Release OpenCV resources
    cap.release()
    
    # Print information
    print(f"\nVideo Information: {os.path.basename(video_path)}")
    print(f"Resolution: {width}x{height}")
    print(f"Frame Count: {frame_count}")
    print(f"FPS: {fps:.2f}")
    print(f"Duration: {duration_formatted} ({duration_seconds:.2f} seconds)")
    print(f"Codec: {codec}")
    print(f"File Size: {file_size_mb:.2f} MB")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract information from MP4 video files')
    parser.add_argument('video_paths', nargs='+', help='Path(s) to MP4 video file(s)')
    args = parser.parse_args()
    
    for video_path in args.video_paths:
        get_video_info(video_path)

if __name__ == "__main__":
    main()

# python mytools/video_info.py /mnt/nas/share2/home/cby/Light-A-Video/input_animatediff/car.mp4