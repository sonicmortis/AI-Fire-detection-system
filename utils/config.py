# -*- coding: utf-8 -*-

import streamlit as st

TRAINING_STATS = {
    'mAP50': 0.427,
    'mAP50_95': 0.200,
    'Precision': 0.497,
    'Recall': 0.421,
    'Fire_mAP50': 0.610,
    'Smoke_mAP50': 0.244,
    'Total_Images': 1431,
    'Total_Instances': 2975,
    'Fire_Instances': 2121,
    'Smoke_Instances': 854
}

TRAINING_PROGRESS = {
    'epochs': list(range(1, 51)),
    'mAP50': [0.172, 0.0688, 0.217, 0.184, 0.228, 0.278, 0.239, 0.275, 0.287, 0.22,
              0.289, 0.304, 0.298, 0.319, 0.306, 0.316, 0.33, 0.347, 0.343, 0.342,
              0.346, 0.335, 0.36, 0.368, 0.373, 0.378, 0.373, 0.387, 0.38, 0.377,
              0.396, 0.394, 0.409, 0.399, 0.407, 0.403, 0.411, 0.412, 0.412, 0.415,
              0.41, 0.418, 0.418, 0.421, 0.424, 0.422, 0.423, 0.423, 0.423, 0.427]
}

CLASS_NAMES = {
    0: "🔥 FIRE",
    1: "💨 SMOKE"
}

CLASS_COLORS = {
    0: (255, 0, 0),
    1: (0, 255, 255)
}

def init_session_state():
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True
    if 'detection_history' not in st.session_state:
        st.session_state.detection_history = []

def apply_css():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        }
        .main-header {
            background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .main-header h1 {
            color: white;
            font-size: 2.5rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .main-header p {
            color: white;
            margin-top: 10px;
            opacity: 0.9;
        }
        
        [data-testid="stMetricValue"] {
            text-align: center !important;
            font-weight: 700 !important;
        }
        [data-testid="stMetricLabel"] {
            text-align: center !important;
            display: block !important;
            width: 100% !important;
        }
        [data-testid="stMetricDelta"] {
            text-align: center !important;
        }
        [data-testid="stMetric"] {
            text-align: center !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
        }
        
        .metric-card {
            background: rgba(30, 30, 50, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 1rem;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(233, 69, 96, 0.3);
            border: 1px solid rgba(233, 69, 96, 0.5);
            background: rgba(40, 40, 65, 0.9);
        }
        .metric-card h2, .metric-card h3, .metric-card h4, .metric-card p {
            text-align: center !important;
            margin-left: auto !important;
            margin-right: auto !important;
            width: 100% !important;
        }
        .metric-card h2 {
            color: #ff6b6b;
            font-weight: bold;
        }
        [data-testid="stSidebar"] {
            background: rgba(20, 20, 40, 0.95);
            border-right: 1px solid rgba(255,255,255,0.1);
        }
        .stButton > button {
            background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
        }
        .stButton > button:hover {
            opacity: 0.9;
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(233, 69, 96, 0.4);
            cursor: pointer;
        }
        .stRadio > div {
            gap: 1rem;
        }
        .stDataFrame {
            background: rgba(30, 30, 50, 0.5);
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)