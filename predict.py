from ultralytics import YOLO
import cv2

# Load trained model (best weights)
model = YOLO("runs/train/ppe_yolov8n/weights/best.pt")

# For validation images
results = model.predict(source="Dataset/images/val", conf=0.25, show=True, device=0)

# OR for webcam
# results = model.predict(source=0, conf=0.25, show=True, device=0)


# Optional: save predictions
results[0].save(filename="output.jpg")
