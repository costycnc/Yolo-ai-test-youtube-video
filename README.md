# Yolo ai test youtube video

Developed by: **costycnc**

A lightweight Python project to download YouTube videos or Shorts at an optimized resolution (720p) without requiring FFmpeg, and perform real-time object detection using **YOLOv8**. 

The system extracts bounding box coordinates and logs the detected objects live into both the OpenCV video window and the DOS terminal (command prompt) frame by frame.

## 🚀 Project Structure

The project is split into two independent scripts to optimize performance and prevent repeated downloads:
1. `scarica_video.py`: Handles downloading only the video track from YouTube in HD (720p).
2. `analisi_yolo.py`: Runs the YOLOv8 model on the local video file, showing bounding boxes and live terminal logs.

## 📦 Requirements & Installation

Make sure you have Python installed on your PC. Open your DOS terminal and install the required libraries using the following command:

```bash
pip install opencv-python ultralytics yt-dlp
```

## 🛠️ How to Use

1. Run the download script first to save the video to your hard drive:
   ```bash
   python scarica_video.py
   ```
2. Once the download is complete, start the visual analysis script:
   ```bash
   python analisi_yolo.py
   ```
3. Press the **'q'** key on the video window to close the application at any time.

## ⚙️ Path Configuration

Ensure that the absolute paths inside the scripts correctly point to your local directories:
* YOLO Model: `c:\test\robot_project\yolov8n.pt`
* Video Destination: `c:\test\youtube\video_target.mp4`

