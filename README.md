# 🖱️ Virtual Mouse using OpenCV and MediaPipe

Control your computer's mouse using hand gestures captured through your webcam. This project uses **OpenCV**, **MediaPipe**, and **AutoPy** to perform real-time cursor movement, clicking, and dragging without a physical mouse.

---

## ✨ Features

- 👆 Move the mouse cursor using your index finger.
- 👌 Left click using the index and middle fingers.
- 🤏 Drag and drop using a thumb-index pinch gesture.
- 🎯 Cursor smoothing for stable movement.
- 📺 Displays real-time FPS.
- 🖥️ Active movement region for improved cursor control.

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- AutoPy

---

## 📂 Folder Structure

```
Virtual-Mouse/
│── HandTrackingModule.py
│── VirtualMouse.py
│── requirements.txt
└── README.md
```

---

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Virtual-Mouse.git
cd Virtual-Mouse
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python VirtualMouse.py
```

---

## 🎮 Gestures

| Gesture | Action |
|---------|--------|
| ☝️ Index Finger Up | Move Cursor |
| ☝️ + ✌️ Index & Middle Finger Close | Left Click |
| 🤏 Thumb & Index Finger Pinch | Drag and Drop |

---

## ⚙️ How It Works

1. Captures live video using OpenCV.
2. Detects hand landmarks using MediaPipe.
3. Maps finger coordinates to the screen resolution.
4. Smooths cursor movement using interpolation.
5. Performs mouse actions using AutoPy.

---

## 📋 Requirements

- Python 3.10 or above
- Webcam

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

```text
opencv-python
mediapipe
numpy
autopy
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## ⭐ If you found this project useful, consider giving it a star!
