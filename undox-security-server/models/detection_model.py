from ultralytics import YOLO
import cv2

class DetectionModel:
    def __init__(self, weights="yolov8n.pt"):
        self.model = YOLO(weights)

    def train(self, data, project, name, epochs=50, imgsz=640, batch=16, device="cpu", patience=20):
        results = self.model.train(data=data, project=project, name=name, epochs=epochs, imgsz=imgsz, batch=batch, device=device, patience=patience)
        return results

    def evaluate(self, data):
        metrics = self.model.val(data)
        return metrics

    def predict(self, source, project="./runs/predicts", save=True, save_txt=True, imgsz=640, conf=0.25):
        results = self.model.predict(source=source, project=project, save=save, save_txt=save_txt, imgsz=imgsz, conf=conf)
        return results


if (__name__ == "__main__"):
    data = "./datasets/all_sensitive_info/data.yaml"
    test_source = "./datasets/all_sensitive_info/test/images"
    project = "./runs/train"
    name = "finetuned"

    detect = DetectionModel(weights="./runs/train/finetuned/weights/best.pt")

    # detect.train(data=data, project=project, name=name)

    # detect.evaluate(data=data, project=project)

    project = "./runs/predicts"
    detect.predict(source=test_source, project=project)
