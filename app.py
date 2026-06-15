import streamlit as st
from utils.config import init_session_state, apply_css

# Page config harus di awal
st.set_page_config(
    page_title="AI Fire Detection System",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Init session state HARUS sebelum import halaman
init_session_state()

# Init session state (set dark_mode = True langsung)
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True

# Import halaman (setelah set_page_config)
import home
import prediction
import dashboard
import history
import about

# Apply CSS (dark mode langsung)
apply_css()

# Sidebar navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/fire-alarm.png", width=80)
    st.markdown("# 🔥 AI Fire Detection")
    st.markdown("---")
    
    st.markdown("### 📱 Navigation")
    
    page = st.radio(
        "",
        ["Home", "Prediction", "Dashboard", "History", "ℹAbout"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("© 2025/2026 - Image Processing Final Project")

# Page routing
if page == "Home":
    home.show_home()
elif page == "Prediction":
    prediction.show_prediction()
elif page == "Dashboard":
    dashboard.show_dashboard()
elif page == "History":
    history.show_history()
elif page == "ℹAbout":
    about.show_about()