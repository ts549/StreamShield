import cv2
from models import DetectionModel
from pathlib import Path
class AIWorker:

    def __init__(self):
        self.detection_model = DetectionModel(Path(__file__).resolve().parent.parent / 'models/runs/train/finetuned/weights/best.pt')
        # self.ocr_model = OCRModel()

    def blur_frame(self, frame, width, height):
        resized_frame = cv2.resize(frame, (640, 640))

        # Run prediction
        results = self.detection_model.predict(
            source=resized_frame,
            save=False,
            save_txt=False,
            imgsz=640,
            conf=0.2,
        )

        h, w = resized_frame.shape[:2]
        pad = 0.15

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                bw, bh = x2 - x1, y2 - y1
                x1 = max(0, int(x1 - bw * pad))
                y1 = max(0, int(y1 - bh * pad))
                x2 = min(w, int(x2 + bw * pad))
                y2 = min(h, int(y2 + bh * pad))

                roi = resized_frame[y1:y2, x1:x2]
                blurred_roi = cv2.GaussianBlur(roi, (51, 51), 30)
                resized_frame[y1:y2, x1:x2] = blurred_roi

        blurred_frame = cv2.resize(resized_frame, (width, height))
        return blurred_frame

if (__name__ == "__main__"):
    ai_worker = AIWorker()
    frame = cv2.imread("./models/datasets/credit_card/test/images/a.jpg")
    blurred_frame = ai_worker.blur_frame(frame=frame, width=640, height=360)

    cv2.imshow("Blurred Detections", blurred_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
