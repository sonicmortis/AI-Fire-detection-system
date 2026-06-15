import streamlit as st
from utils.config import apply_css

def show_about():
    apply_css()
    
    st.markdown("""
        <div class="main-header">
            <h1>ℹ️ About This Project</h1>
            <p>AI Fire Detection System - Image Processing Final Project</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Project Overview")
        st.write("""
            Final assignment for **DIF60202 – Image Processing** at **Informatika**.
            Uses YOLOv8 for fire and smoke detection.
        """)
        
        st.subheader("🛠️ Technologies")
        st.markdown("""
        | Technology | Purpose |
        |-----------|---------|
        | YOLOv8 | Object Detection |
        | Streamlit | Web Framework |
        | OpenCV | Image Processing |
        | Plotly | Visualizations |
        """)
        
        st.subheader("📚 References")
        st.markdown("- Ultralytics YOLOv8\n- Roboflow\n- Streamlit Docs")
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <h4 style="text-align: center;">🎓 Course Info</h4>
                <hr>
                <p><strong>Code:</strong> DIF60202</p>
                <p><strong>Name:</strong> Image Processing</p>
                <p><strong>Semester:</strong> Genap 2025/2026</p>
                <hr>
                <h4 style="text-align: center;">👨‍💻 Developer</h4>
                <p style="text-align: center;">
                    <strong>M. Luthfi Kautsar Rizata</strong><br>
                    NIM: 2311532020
                </p>
                <hr>
                <p><strong>Deadline:</strong> 16 Juni 2026</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    for col, icon, text in [(col1, "🔥", "Fire Detection"), (col2, "💨", "Smoke Detection"), (col3, "📊", "Analytics")]:
        with col:
            st.markdown(f"""
                <div class="metric-card" style="text-align: center;">
                    <h2>{icon}</h2>
                    <h4>{text}</h4>
                </div>
            """, unsafe_allow_html=True)