from ultralytics import YOLO

# Load the pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="dataset.yaml",   # path to dataset config
    epochs=100,           # total epochs
    imgsz=640,             # image size
    batch=16,              # adjust if you get GPU OOM
    device=0,              # 0 means first GPU
    workers=4,             # number of CPU workers for dataloading
    project="runs/train",  # output directory
    name="ppe_yolov8n",    # run name
)
