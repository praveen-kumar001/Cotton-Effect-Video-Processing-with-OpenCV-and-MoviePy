import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def apply_cotton_effect(frame):
    # Convert the frame to a softer, pastel-like image
    # Step 1: Apply bilateral filter for edge-preserving smoothing
    smooth = cv2.bilateralFilter(frame, 9, 75, 75)

    # Step 2: Convert to grayscale and blur for a cartoonish look
    gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)

    # Step 3: Create an edge mask using adaptive threshold
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)

    # Step 4: Convert back to color and merge with the smoothed image
    color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cotton_effect = cv2.bitwise_and(smooth, color)

    return cotton_effect

def process_video(input_path, output_path):
    # Load the video using moviepy
    clip = VideoFileClip(input_path)

    def apply_effect_to_frame(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert MoviePy frame (RGB) to OpenCV (BGR)
        cotton_frame = apply_cotton_effect(frame)
        return cv2.cvtColor(cotton_frame, cv2.COLOR_BGR2RGB)  # Convert back to RGB for MoviePy

    # Apply the effect to each frame and write out the video
    processed_clip = clip.fl_image(apply_effect_to_frame)  # Apply the effect directly to the frame
    processed_clip.write_videofile(output_path, audio=False)

if __name__ == "__main__":
    input_video = "/home/praveenkumar/Videos/Autonomous Campus Shuttle _ NMICPS TiHAN Foundation - IIT Hyderabad.mp4"   # Path to your input video
    output_video = "/home/praveenkumar/Videos/_cotton_video.mp4"  # Path to save the processed video
    process_video(input_video, output_video)
