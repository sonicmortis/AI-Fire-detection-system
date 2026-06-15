# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime
import hashlib

def save_to_history(result_image, detections, inference_time):
    """Save detection result to session state history"""
    # Pastikan detection_history sudah ada di session state
    if 'detection_history' not in st.session_state:
        st.session_state.detection_history = []
    
    history_id = hashlib.md5(f"{datetime.now()}{len(st.session_state.detection_history)}".encode()).hexdigest()[:8]
    
    entry = {
        'id': history_id,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'fire_detected': any('FIRE' in d['class'] for d in detections),
        'smoke_detected': any('SMOKE' in d['class'] for d in detections),
        'total_detections': len(detections),
        'inference_time': inference_time,
        'detections': detections
    }
    
    st.session_state.detection_history.insert(0, entry)
    # Keep only last 20
    st.session_state.detection_history = st.session_state.detection_history[:20]

def clear_history():
    """Clear all detection history"""
    if 'detection_history' in st.session_state:
        st.session_state.detection_history = []