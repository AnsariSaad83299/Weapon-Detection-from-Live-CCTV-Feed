import cv2
from ultralytics import YOLO
import os

def get_results(model, frame):

    results = model(frame, show= True, conf= 0.5)
    return results

def extract_frames(video_path, frame_rate=1, display_duration=1000):
    video_capture = cv2.VideoCapture(video_path)
    model = YOLO('roboflow-v8.pt')
    
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return
    
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    frame_interval = fps // frame_rate
    
    frame_count = 0
    
    while True:
        ret, frame = video_capture.read()
        
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            
            results = model(frame, conf= 0.5)
            for r in results:
                bboxes = r.boxes.xywh
    
            if len(bboxes) != 0:
                for box in bboxes:
                    x, y, w, h = box
                    x= int(x.item()) -10
                    y= int(y.item()) -5
                    w= int(w.item())
                    h= int(h.item())
    
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)   
                save_path = os.path.join("temp", f"frame_{frame_count}.jpg")
                cv2.imwrite(save_path, frame)


            cv2.imshow("Frame with Bounding Boxes", frame)
            key = cv2.waitKey(display_duration)

            if key & 0xFF == ord('q'):
                break
        
        frame_count += 1
    
    video_capture.release()
    
    cv2.destroyAllWindows()


video_path = "Gun-Movies/1-short.mp4"
extract_frames(video_path, frame_rate=1, display_duration=1000)  # Display each frame for 1000 milliseconds (1 second)


