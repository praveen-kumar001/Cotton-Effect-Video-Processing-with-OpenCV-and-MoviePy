# Cotton Effect Video Processing

This Python project applies a cotton-like effect to each frame of a video using `OpenCV` for image processing and `MoviePy` for handling video files. The cotton effect softens the image, giving it a pastel or cartoon-like appearance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

To run this project, ensure you have Python 3.6+ installed. You will also need to install the following libraries:

1. OpenCV (cv2)
2. NumPy
3. MoviePy

You can install them using `pip`:

```bash
pip install opencv-python numpy moviepy

if __name__ == "__main__":
    input_video = "/path/to/your/input_video.mp4"   # Path to your input video
    output_video = "/path/to/your/output_video.mp4"  # Path to save the processed video
    process_video(input_video, output_video)

python add.py

.
├── add.py                 # Main script applying the cotton effect
├── README.md              # Documentation (this file)
└── requirements.txt       # Optional: List of required Python libraries

This `README.md` gives an overview of the project, explains how to install and use the program, and describes its functionality.

