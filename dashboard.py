# -*- coding: utf-8 -*-
"""
Dashboard Page
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.config import TRAINING_STATS, TRAINING_PROGRESS

def show_dashboard():
    st.markdown("""
        <div class="main-header">
            <h1>📊 Analytics Dashboard</h1>
            <p>Model performance statistics and detection analytics</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Model metrics
    st.subheader("🎯 Model Performance")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("mAP50", f"{TRAINING_STATS['mAP50']*100:.1f}%")
    c2.metric("mAP50-95", f"{TRAINING_STATS['mAP50_95']*100:.1f}%")
    c3.metric("Precision", f"{TRAINING_STATS['Precision']*100:.1f}%")
    c4.metric("Recall", f"{TRAINING_STATS['Recall']*100:.1f}%")
    
    # Per-class performance
    class_df = pd.DataFrame({
        'Class': ['Fire 🔥', 'Smoke 💨'],
        'mAP50': [TRAINING_STATS['Fire_mAP50']*100, TRAINING_STATS['Smoke_mAP50']*100],
        'Instances': [TRAINING_STATS['Fire_Instances'], TRAINING_STATS['Smoke_Instances']]
    })
    fig = px.bar(class_df, x='Class', y='mAP50', text='mAP50', color='Class',
                 color_discrete_sequence=['#ff4444', '#ffaa44'], title='mAP50 by Class')
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(yaxis_range=[0, 100], showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Dataset distribution
    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.pie(values=[TRAINING_STATS['Fire_Instances'], TRAINING_STATS['Smoke_Instances']],
                      names=['Fire', 'Smoke'], title='Dataset Distribution',
                      color_discrete_sequence=['#ff4444', '#ffaa44'])
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <h4>📊 Dataset Stats</h4>
                <p>Validation Images: {TRAINING_STATS['Total_Images']}</p>
                <p>Total Boxes: {TRAINING_STATS['Total_Instances']}</p>
                <p>Fire: {TRAINING_STATS['Fire_Instances']} ({TRAINING_STATS['Fire_Instances']/TRAINING_STATS['Total_Instances']*100:.1f}%)</p>
                <p>Smoke: {TRAINING_STATS['Smoke_Instances']} ({TRAINING_STATS['Smoke_Instances']/TRAINING_STATS['Total_Instances']*100:.1f}%)</p>
                <hr><p>Epochs: 50 | Size: 512px | Batch: 48</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Training progress chart
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=TRAINING_PROGRESS['epochs'], y=[v*100 for v in TRAINING_PROGRESS['mAP50']],
                              mode='lines+markers', name='mAP50', line=dict(color='#e94560', width=2)))
    fig3.update_layout(title='Training Progress (50 Epochs)', xaxis_title='Epoch', yaxis_title='mAP50 (%)', height=400)
    st.plotly_chart(fig3, use_container_width=True)
    
    # Live history stats - PERBAIKAN DI SINI
    st.subheader("📈 Live Detection Stats")
    
    # Cek apakah detection_history ada dan tidak kosong
    if 'detection_history' in st.session_state and st.session_state.detection_history:
        df_hist = pd.DataFrame(st.session_state.detection_history)
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Scans", len(df_hist))
        c2.metric("Fire Detected", df_hist['fire_detected'].sum())
        c3.metric("Smoke Detected", df_hist['smoke_detected'].sum())
    else:
        st.info("ℹ️ No detection history yet. Try the Prediction page!")