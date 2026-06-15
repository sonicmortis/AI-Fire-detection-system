import streamlit as st
import time
import pandas as pd
from PIL import Image
from utils.model_utils import load_model, detect_fire
from utils.history_utils import save_to_history

def show_prediction():
    st.markdown("""
        <div class="main-header">
            <h1>🎯 Fire Detection</h1>
            <p>Upload an image or use webcam to detect fire and smoke</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Inisialisasi session state untuk menyimpan hasil deteksi
    if 'detection_result' not in st.session_state:
        st.session_state.detection_result = None
        st.session_state.result_img = None
        st.session_state.detections = []
        st.session_state.inference_ms = 0
        st.session_state.current_image = None
    
    model = load_model()
    if model is None:
        return
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        input_method = st.radio("Select Input Method", ["📁 Upload Image", "📸 Webcam"], horizontal=True)
    
        image = None
        if input_method == "📁 Upload Image":
            uploaded = st.file_uploader("Choose image...", type=['jpg', 'jpeg', 'png'])
            if uploaded:
                image = Image.open(uploaded)
                st.image(image, caption="Original", use_container_width=True)
        else:
            camera = st.camera_input("Take a picture")
            if camera:
                image = Image.open(camera)
        
        st.subheader("⚙️ Settings")
        confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.25, 0.05)
        
        if image and st.button("🔍 Detect", type="primary", use_container_width=True):
            with st.spinner("Analyzing..."):
                start = time.time()
                result_img, detections, speed = detect_fire(image, model, confidence_threshold)
                inference_ms = (time.time() - start) * 1000
                
                # Simpan ke session state
                st.session_state.result_img = result_img
                st.session_state.detections = detections
                st.session_state.inference_ms = inference_ms
                st.session_state.current_image = image
                
                st.rerun()
    
    with col_right:
        if st.session_state.result_img is not None:
            st.subheader("🎯 Detection Result")
            st.image(st.session_state.result_img, use_container_width=True)
    
    # Notifikasi dan hasil deteksi (full width)
    if st.session_state.detections:
        detections = st.session_state.detections
        inference_ms = st.session_state.inference_ms
        
        fire = any('FIRE' in d['class'] for d in detections)
        if fire:
            st.error("🚨 ALERT: FIRE DETECTED! 🚨")
        else:
            st.success("✅ No fire detected, but smoke may be present.")
        
        df = pd.DataFrame(detections)[['class', 'confidence', 'timestamp']]
        df.columns = ['Class', 'Confidence', 'Time']
        st.dataframe(df, use_container_width=True)
        
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("⏱️ Inference", f"{inference_ms:.1f} ms")
        col_b.metric("🎯 Objects", len(detections))
        col_c.metric("🔥 Fire", "Yes" if fire else "No")
        
        save_to_history(st.session_state.result_img, detections, inference_ms)