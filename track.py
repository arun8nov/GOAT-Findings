import ultralytics
from ultralytics import YOLO
model =YOLO("best.pt")
model.track(source="D:\GIT\GOAT-Findings\samples\Goat.mp4",show=True)