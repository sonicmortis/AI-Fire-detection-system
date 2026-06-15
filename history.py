import streamlit as st
import pandas as pd
from utils.history_utils import clear_history

def show_history():
    st.markdown("""
        <div class="main-header">
            <h1>📜 Detection History</h1>
            <p>Your recent fire detection results</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🗑️ Clear History", use_container_width=True):
            clear_history()
            st.rerun()
    
    # PERBAIKAN DI SINI - cek apakah detection_history ada
    if 'detection_history' in st.session_state and st.session_state.detection_history:
        for i, entry in enumerate(st.session_state.detection_history):
            with st.expander(f"📸 Detection {i+1} - {entry['timestamp']}", expanded=(i==0)):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Fire:** {'Yes' if entry['fire_detected'] else 'No'}")
                    st.write(f"**Smoke:** {'Yes' if entry['smoke_detected'] else 'No'}")
                    st.write(f"**Objects:** {entry['total_detections']}")
                    st.write(f"**Inference:** {entry['inference_time']:.1f} ms")
                with col2:
                    if entry['detections']:
                        df = pd.DataFrame(entry['detections'])[['class', 'confidence']]
                        st.dataframe(df, hide_index=True, use_container_width=True)
    else:
        st.info("📭 No detection history yet. Go to Prediction page!")