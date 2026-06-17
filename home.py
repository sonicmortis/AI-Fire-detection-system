import streamlit as st
from utils.config import TRAINING_STATS

def show_home():
    st.markdown("""
        <div class="main-header">
            <h1>🔥 AI Fire Detection System</h1>
            <p>Real-time Fire & Smoke Detection using YOLOv8 Deep Learning</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="small")
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <span style="color: #6c5ce7; font-size: 1.17em; font-weight: bold; display: block; margin: 0 0 0.5rem 0;">Fire Detection</span>
                <h2 style="color: white; font-size: 2rem; font-weight: bold; display: block; margin: 0 0 0.5rem 0">{TRAINING_STATS['Fire_mAP50']*100:.1f}%</h2>
                <p style="color: #aaa; margin: 0;">mAP50 Score</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <span style="color: #ffaa44; font-size: 1.17em; font-weight: bold; display: block; margin: 0 0 0.5rem 0;">Smoke Detection</span>
                <h2 style="color: white; font-size: 2rem; font-weight: bold; display: block; margin: 0 0 0.5rem 0">{TRAINING_STATS['Smoke_mAP50']*100:.1f}%</h2>
                <p style="color: #aaa; margin: 0;">mAP50 Score</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <span style="color: #6c5ce7; font-size: 1.17em; font-weight: bold; display: block; margin: 0 0 0.5rem 0;">Overall mAP50</span>
                <h2 style="color: white; font-size: 2rem; font-weight: bold; display: block; margin: 0 0 0.5rem 0;">{TRAINING_STATS['mAP50']*100:.1f}%</h2>
                <p style="color: #aaa; margin: 0;">Mean Average Precision</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <span style="color: #00cec9; font-size: 1.17em; font-weight: bold; display: block; margin: 0 0 0.5rem 0;">Model Speed</span>
                <h2 style="color: white; font-size: 2rem; margin: 0.5rem 0;">~1.6ms</h2>
                <p style="color: #aaa; margin: 0;">Inference per image</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1_bot, col2_bot = st.columns(2)
    
    with col1_bot:
        st.subheader("🎯 About This System")
        st.write("""
            Uses **YOLOv8** deep learning model to detect fire and smoke in real-time.
            
            **Features:**
            - 🔥 Fire (Blue bounding box)
            - 💨 Smoke (Yellow bounding box)
            - 📊 Performance analytics
            - 🎥 Webcam & image upload
        """)
    
    with col2_bot:
        st.subheader("📋 Course Info")
        st.markdown("""
            **Course:** Image Processing  
            **Semester:** Genap 2025/2026  
            **Model:** YOLOv8n (50 epochs)  
        """)
    
    st.markdown("---")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
            <div class="metric-card">
                <h2>📸</h2>
                <h4>1. Input</h4>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
            <div class="metric-card">
                <h2>🧠</h2>
                <h4>2. Process</h4>
            </div>
        """, unsafe_allow_html=True)
    with col_c:
        st.markdown("""
            <div class="metric-card">
                <h2>⚠️</h2>
                <h4>3. Alert</h4>
            </div>
        """, unsafe_allow_html=True)
