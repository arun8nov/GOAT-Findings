# 🐐 GOAT-FINDINGS: Smart Animal Intrusion Detection System

## 🌾 Real World Problem
I live in a village, and at the back of my house, I cultivate vegetables for my home use.  
However, goats and sheep often enter my field from the nearby road and spoil the crops.  
This frequent issue leads to frustration and crop damage.

---

## 💡 How a Data Scientist from a Village Solved It
Using **data science and computer vision**, I developed a **Goat & Sheep Detection System** that automatically tracks animals entering the field through a **CCTV camera feed** and sends a notification to the user.

---

## 🔍 Project Overview

### 1. Data Collection
- Gathered real-world videos of goats and sheep from **YouTube** and personal recordings.  
- Extracted frames and uploaded them to **Roboflow** for annotation.

### 2. Annotation & Dataset Preparation
- Used **Segmentation task** in Roboflow.  
- Annotated two classes:  
  - 🐐 **Goat** — 885 images  
  - 🐏 **Sheep** — 2649 images  
- Total Images: 779  
- Dataset Size: **~76.9 MB**  
- Exported dataset in **YOLO format**.

### 3. Model Training
- Trained a **YOLOv11n segmentation model** using **Google Colab**.  
- Dataset imported from **Roboflow** workspace.  
- Achieved accurate segmentation between goats and sheep.  
- The final trained model is saved as **`best.pt`**.

### 4. Real-Time Tracking & Notification
- Implemented real-time animal tracking using **Ultralytics YOLO**.  
- Used the **track.py** script to detect and follow goats/sheep in a video or live CCTV stream.  
- Future version will include **audio alert** (cracker sound) through a connected speaker when intrusion is detected.

---

## 🧠 Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python |
| **Framework** | Ultralytics YOLOv11 |
| **Annotation Tool** | Roboflow |
| **IDE** | VS Code / Google Colab |
| **Libraries Used** | ultralytics, opencv-python, numpy |
| **Hardware** | CCTV Camera / Local Video Feed |

---

## 📂 Project Structure
```
GOAT-FINDINGS/
│
├── samples/                   # Test videos
│   ├── Goat.mp4
│   ├── goat1.mp4
│   ├── goat2.mp4
│   ├── goat3.mp4
│   ├── goat4.mp4
│   └── goat5.mp4
│
├── best.pt                    # Trained YOLOv11n model
├── track.py                   # Tracking and detection script
├── downlode.ipynb             # Data download/processing notebook
├── requirements.txt           # Required dependencies
├── README.md                  # Project documentation
└── .gitignore
```
Git_Link : https://github.com/arun8nov/GOAT-Findings
---

## ⚙️ track.py Example
```python
import ultralytics
from ultralytics import YOLO

# Load trained YOLOv11n model
model = YOLO("best.pt")

# Track animals from a video source
model.track(source="D:\GIT\GOAT-Findings\samples\Goat.mp4", show=True)
```

---

## 🚀 Future Enhancements
- 🔊 Add speaker-based alert system  on detection.  
- 📱 Send intrusion notifications to mobile devices.  
- 🤖 Integrate IoT for automatic electric fencing control.  
- 💻 Deploy on low-power devices like Raspberry Pi for real-time edge processing.

---

## 🌱 Impact
This project demonstrates how **Data Science and AI** can be applied to **real-world rural problems**.  
By automating the detection of goats and sheep entering the cultivation area, it reduces manual monitoring and helps protect crops effectively.

---

## 👨‍💻 Author
**Arunprakash B**  
📧 *arunbabubprakash@gmail.com*  
🔗 Project Type: Personal | Applied AI in Agriculture  

---

⭐ *“Empowering rural life with AI — one problem at a time.”*
