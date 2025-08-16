**>>>Project Overview**
This project is a deep learning-based system designed to detect obstacles on railway tracks using a YOLOv8 object detection model.It provides real-time alerts through sound and popup messages when an obstacle is detected, helping to enhance railway safety.

The detection system works both with:
-Live webcam feed (real-time detection)
-Static images (image-based detection)

**>>>Dataset**
-Source: Roboflow
-Type: Pre-annotated dataset for railway track obstacles
-Annotation format: YOLO format
-Classes: Objects/obstacles on railway tracks

**🛠 Features**

1. **YOLOv8 Object Detection**  
   - Utilized the latest YOLOv8 model from Ultralytics for fast and precise detection.  
   - Capable of identifying multiple types of obstacles on railway tracks.

2. **Training on Google Colab**  
   - Leveraged **Google Colab** with GPU acceleration for training.  
   - Experimented with multiple hyperparameters, selecting the best-performing weights for deployment.

3. **Live Cam Detection**  
   -system can process live camera input to detect obstacles on railway tracks. For simplicity, the current implementation uses full-frame detection without restricting to a region of interest.

4. **Alert System Integration**  
   - On detecting an obstacle with high confidence, the system:  
     - Captures the detection frame.  
     - Displays a popup notification (**Obstacle detected!**).

5. **Sound Alert Mechanism**  
   - Triggered a **beep sound** using the `winsound` module whenever an obstacle is detected.


**>>>Technologies & Libraries Used**
-Ultralytics YOLOv8 → Model training & inference
-OpenCV → Image capture, display, and preprocessing
-Winsound → Play alert sound (Windows only)
-PyMsgBox → Show popup alert when an obstacle is detected
-Time → Manage alert cooldowns to prevent spamming
