import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Precision Aquaculture Engine", layout="wide")

st.title("Serverless Precision Aquaculture Pipeline")
st.caption("Distributed Evolutionary Computation & Real-Time Marine Anomaly Detection")

st.sidebar.header("Marine Telemetry Configuration")
selected_farm = st.sidebar.selectbox("Target Offshore Farm", ["Marlborough Sounds Salmon Array", "Southland Mussel Hatchery", "Coromandel Coastal Facility"])
bio_shock = st.sidebar.slider("Simulate Biological Shock (Hypoxic Event/Bio-Fouling)", 1.0, 5.0, 3.5)
run_simulation = st.sidebar.button("Initialize Evolutionary AWS Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: Sensor Ingestion -> Parallel Feature Selection -> XGBoost Inference")

if run_simulation:
    st.subheader(f"Active Marine Intelligence Monitor: {selected_farm}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_velocity = col1.empty()
    metric_efficiency = col2.empty()
    metric_oxygen = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(2929)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    oxygen_levels = []
    feature_efficiency = []
    
    base_oxygen = 8.5 
    base_efficiency = 40.0
    
    for i in range(100):
        velocity = int(np.random.uniform(50000, 100000))
        
        if i < 30:
            current_oxygen = base_oxygen + np.random.uniform(-0.5, 0.5)
            current_eff = base_efficiency + np.random.uniform(-2.0, 2.0)
            status = "OPTIMAL MARINE CONDITIONS"
        elif i >= 30 and i < 65:
            current_oxygen = base_oxygen - (i - 30) * (0.15 * bio_shock) + np.random.uniform(-1.0, 1.0)
            current_eff = min(99.0, base_efficiency + (i - 30) * 1.5 + np.random.uniform(-5.0, 5.0))
            status = "HYPOXIC EVENT DETECTED"
        else:
            current_oxygen = current_oxygen + np.random.uniform(0.1, 0.8)
            current_eff = current_eff + np.random.uniform(-1.0, 1.0)
            status = "AUTONOMOUS AERATION ACTIVE"
            
        current_oxygen = max(1.0, current_oxygen)
        current_eff = min(99.9, current_eff)
            
        oxygen_levels.append(current_oxygen)
        feature_efficiency.append(current_eff)
        
        metric_velocity.metric("Raw Telemetry Ingestion", f"{velocity:,} Nodes/s", "High-Dimensional Noise")
        metric_efficiency.metric("Evolutionary Selection Efficiency", f"{current_eff:.1f}%", f"+{(current_eff - base_efficiency):.1f}% Dimensionality Reduction")
        metric_oxygen.metric("Dissolved Oxygen (mg/L)", f"{current_oxygen:.2f} mg/L", f"{(current_oxygen - base_oxygen):.2f} Variance")
        
        if status == "HYPOXIC EVENT DETECTED":
            metric_status.metric("Biological Health Status", status, "Critical Biomass Threat")
        elif status == "AUTONOMOUS AERATION ACTIVE":
            metric_status.metric("Biological Health Status", status, "Actuators Deployed")
        else:
            metric_status.metric("Biological Health Status", status, "Stable")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=oxygen_levels, mode='lines', name='Dissolved Oxygen (mg/L)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=feature_efficiency, mode='lines', name='Algorithmic Optimization (%)', yaxis='y2', line=dict(color='green', dash='dot')))
        
        fig.update_layout(
            title="Precision Aquaculture: Evolutionary Feature Selection vs Marine Hypoxia",
            xaxis=dict(title="High-Frequency Sensor Timeline"),
            yaxis=dict(title="Dissolved Oxygen (mg/L)", range=[0, 12]),
            yaxis2=dict(title="Optimization Efficiency (%)", overlaying='y', side='right', range=[0, 100]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "HYPOXIC EVENT DETECTED" and i == 30:
            log_placeholder.error(f"BIOLOGICAL ALERT: High-dimensional noise spike and oxygen degradation detected at {time_steps[i].strftime('%H:%M:%S')}. Spawning ephemeral AWS Lambda instances to execute parallel evolutionary feature selection. Noise isolated.")
        elif status == "AUTONOMOUS AERATION ACTIVE" and i == 65:
            log_placeholder.warning(f"CYBER-PHYSICAL INTERVENTION: XGBoost inference engine successfully mapped critical biological threat. Automated aeration protocols triggered in marine farm.")
        elif status == "OPTIMAL MARINE CONDITIONS" and i % 5 == 0:
            log_placeholder.success(f"Log: Massive telemetry burst {i} ingested via serverless API. Evolutionary computation operating efficiently in background.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cloud architecture successfully parallelized evolutionary computation, isolating the biological threat and preserving marine biomass.")
else:
    st.info("Click 'Initialize Evolutionary AWS Engine' in the sidebar to simulate high-frequency precision aquaculture data.")