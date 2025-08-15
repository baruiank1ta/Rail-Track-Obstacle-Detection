from ultralytics import YOLO
import cv2
import winsound
import pymsgbox
import time
import os

MODEL_PATH = "best.pt"         # Your trained model file
ALERT_SOUND_FILE = "alert.wav" # Your alert sound file
CONF_THRESHOLD = 0.4           # Detection confidence threshold
ALERT_COOLDOWN = 3             # Cooldown time between alerts (seconds)

# Load YOLO model
model = YOLO(MODEL_PATH)

# Function to play alert sound
def alert_sound():
    if os.path.exists(ALERT_SOUND_FILE):
        winsound.PlaySound(ALERT_SOUND_FILE, winsound.SND_FILENAME)
    else:
        print("Alert sound file not found.")

# Function to show popup alert
def popup_alert():
    pymsgbox.alert('Obstacle detected!', 'ALERT')

# Function to process detections
def process_detections(results):
    detected = False
    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            if conf > CONF_THRESHOLD:
                detected = True
    return detected

# Function to run detection on an image
def detect_on_image(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Error: Could not read image {image_path}")
        return

    results = model(frame)
    if process_detections(results):
        print("Object Detected!")
        alert_sound()
        popup_alert()
    else:
        print("No object detected above threshold.")

    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Detection - Image", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to run detection on webcam (live)
def detect_on_webcam():
    cap = cv2.VideoCapture(0)
    last_alert_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        if process_detections(results):
            current_time = time.time()
            if current_time - last_alert_time > ALERT_COOLDOWN:
                print("Object Detected!")
                alert_sound()
                popup_alert()
                last_alert_time = current_time

        annotated_frame = results[0].plot()
        cv2.imshow("YOLO Detection - Live", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


print("Choose Mode:")
print("1. Static Image Detection")
print("2. Live Webcam Detection")
choice = input("Enter 1 or 2: ")

if choice == "1":
    image_path = input("Enter image file path: ")
    detect_on_image(image_path)
elif choice == "2":
    detect_on_webcam()
else:
    print("Invalid choice.")

