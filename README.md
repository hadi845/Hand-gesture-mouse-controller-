# 🖱️ Virtual Mouse using Hand Tracking

A Python project that lets you control your computer mouse using hand gestures through a webcam. It uses **MediaPipe** for real-time hand landmark detection, **OpenCV** for video capture and visualization, and **PyAutoGUI** to simulate mouse actions like movement and click.


## ✨ Features

- Control the mouse pointer using your **index finger**.
- Simulate mouse **click** by bringing your **thumb and index finger** close together.
- Real-time hand tracking with **low latency**.

## 🛠️ Technologies Used

- [MediaPipe](https://google.github.io/mediapipe/) – for hand landmark detection.
- [OpenCV](https://opencv.org/) – for camera input and image processing.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – for controlling mouse movements and clicks.

## 🧑‍💻 How It Works

- The webcam captures your hand.
- MediaPipe detects key hand landmarks.
- The index finger (landmark 8) is used to control the mouse cursor.
- When the distance between the thumb (landmark 4) and index finger becomes small, a mouse click is triggered.

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed. Then install the required libraries:

```bash
pip install opencv-python mediapipe pyautogui
