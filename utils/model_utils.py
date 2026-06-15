import streamlit as st
import cv2
import numpy as np
import time
import os  
from ultralytics import YOLO
from PIL import Image
from datetime import datetime
from .config import CLASS_NAMES, CLASS_COLORS

@st.cache_resource
def load_model():
    """Load YOLO model with caching"""
    model_path = "best.pt"
    if not os.path.exists(model_path):
        st.error(f"❌ Model file '{model_path}' not found!")
        return None
    try:
        return YOLO(model_path)
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

def detect_fire(image, model, confidence_threshold=0.25):
    """Run fire detection on image"""
    img = np.array(image.copy())
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) if len(img.shape) == 3 else img
    
    # Run inference
    results = model(img_bgr, conf=confidence_threshold)
    
    detections = []
    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                if cls == 2:
                    continue
                
                color = CLASS_COLORS.get(cls, (255, 255, 255))
                label = CLASS_NAMES.get(cls, f"Class {cls}")
                label_text = f"{label} ({conf:.2f})"
                
                # Draw bounding box
                cv2.rectangle(img_bgr, (x1, y1), (x2, y2), color, 3)
                
                # Draw label background
                (label_w, label_h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(img_bgr, (x1, y1 - label_h - 5), (x1 + label_w, y1), color, -1)
                cv2.putText(img_bgr, label_text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
                detections.append({
                    'class': label,
                    'confidence': conf,
                    'bbox': [x1, y1, x2, y2],
                    'timestamp': datetime.now().strftime("%H:%M:%S")
                })
    
    result_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return result_img, detections, results[0].speed