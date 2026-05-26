# 👷‍♂️ PPE Kit Detection using YOLOv8 & YOLO11

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-v8%20%7C%20v11-FF2F2F?style=for-the-badge&logo=yolo&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Real-time Personal Protective Equipment (PPE) detection system utilizing state-of-the-art **YOLOv8** and **YOLO11** object detection models. This system automatically scans images, videos, or live camera feeds to detect compliance with safety gear requirements (Helmets, Vests, Boots) in industrial and construction environments.

---

## 📌 Project Overview

Ensuring worker safety on construction sites and industrial zones is paramount. This repository provides a clean, end-to-end pipeline to:
1. **Preprocess and Remap Labels**: Standardize annotations from custom public datasets into a consolidated, clean 6-class representation.
2. **Train YOLOv8/YOLO11**: Custom training configuration with high resolution and hyperparameter settings optimized for safety equipment features.
3. **Perform Real-Time Inference**: Run fast prediction scripts on validation sets, video clips, or real-time webcams.

---

## 📂 Repository Structure

The codebase is kept clean and minimalist, separating dynamic datasets and model weights (which are ignored in version control) from code logic:

```directory
YOLO-based-PPE-Kit-Detection/
├── .gitignore             # Filters out dataset files and binary weights
├── README.md              # Detailed project documentation
├── dataset.yaml           # YOLO configuration defining class indices and dataset splits
├── train.py               # Custom training script for training YOLO models
├── predict.py             # Inference script for real-time predictions and testing
└── remap_labels.py        # Utility script to clean up and remap raw annotations
```

*Note: The actual `Dataset/` directory and large model weights files (`*.pt`) are omitted from Git tracking to preserve repository efficiency. See **Dataset Setup** and **Weights** below for setup instructions.*

---

## 🏷️ Class Remapping Strategy

To match the target schema required for this project, the raw dataset annotations are processed using `remap_labels.py`. This script consolidates a large set of original class indices into **6 strict classes**:

| New Class ID | Class Name | Description | Original Dataset ID |
| :---: | :---: | :---: | :---: |
| `0` | **helmet** | Properly worn safety helmet | `0` |
| `1` | **vest** | Properly worn high-visibility vest | `2` |
| `2` | **boots** | Safety steel-toe boots | `3` |
| `3` | **no_helmet** | Violator without safety helmet | `7` |
| `4` | **no_vest** | Violator without high-visibility vest | *Placeholder* |
| `5` | **no_boots** | Violator without safety boots | `10` |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/dmist08/YOLO-based-PPE-Kit-Detection.git
cd YOLO-based-PPE-Kit-Detection
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then install the required packages:
```bash
pip install ultralytics opencv-python
```

### 3. Dataset Placement
Extract your dataset zip file (`Dataset.zip`) into the root directory. Ensure the structure conforms to the following:
```directory
Dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

---

## 🚀 Workflow Instructions

### Step 1: Preprocess Bounding Boxes
Run the remapping script to format the annotations to our custom 6-class schema:
```bash
python remap_labels.py
```

### Step 2: Train the YOLO Model
The custom training script `train.py` runs fine-tuning using pretrained `yolov8n.pt` base weights for 100 epochs:
```bash
python train.py
```
Training runs are saved to the `runs/train/ppe_yolov8n` directory.

### Step 3: Run Inference (Real-Time Detection)
Ensure you have the trained weights file placed at `runs/train/ppe_yolov8n/weights/best.pt`. Then, run the inference script to validate detections:
```bash
python predict.py
```
*Tip: To test on a real-time webcam feed, uncomment the webcam source line in `predict.py`.*

---

## ⚖️ License
This project is open-source and licensed under the [MIT License](LICENSE).
