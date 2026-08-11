import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="VexarDrive Fleet Analytics", page_icon="🚗", layout="wide")

st.title("VexarDrive Fleet Analytics")
st.caption("Driver Safety & Vehicle Health Dashboard")

@st.cache_data
def load_data():
    driver = pd.read_csv("outputs/driver_ranking.csv")
    vehicle = pd.read_csv("outputs/vehicle_health_ranking.csv")
    return driver, vehicle

driver, vehicle = load_data()

tab1, tab2 = st.tabs(["Driver Safety & Risk", "Vehicle Health"])

with tab1:
    st.header("Driver Safety & Risk")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Drivers", len(driver))
    c2.metric("Higher Risk", int((driver["risk_category"] == "Higher Risk").sum()))
    c3.metric("Moderate Risk", int((driver["risk_category"] == "Moderate Risk").sum()))
    c4.metric("Lower Risk", int((driver["risk_category"] == "Lower Risk").sum()))

    st.subheader("Top 10 Risky Drivers")
    top = driver.sort_values("risk_score", ascending=False).head(10).sort_values("risk_score")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(top["Driver_ID"].astype(str), top["risk_score"])
    ax.set_xlabel("Risk Score")
    ax.set_xlim(0, 100)
    st.pyplot(fig, clear_figure=True)

    st.subheader("Risk Distribution")
    counts = driver["risk_category"].value_counts().reindex(
        ["Higher Risk", "Moderate Risk", "Lower Risk"], fill_value=0
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(counts.index, counts.values)
    ax.set_ylabel("Drivers")
    st.pyplot(fig, clear_figure=True)

    st.subheader("Driver Ranking")
    st.dataframe(
        driver[["risk_rank", "Driver_ID", "risk_score", "risk_category",
                 "overspeed_rate", "harsh_braking_rate",
                 "harsh_acceleration_rate", "aggressive_lateral_rate"]],
        use_container_width=True, hide_index=True
    )

with tab2:
    st.header("Vehicle Health & Maintenance")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Vehicles", len(vehicle))
    c2.metric("Higher Attention", int((vehicle["maintenance_category"] == "Higher Attention").sum()))
    c3.metric("Monitor", int((vehicle["maintenance_category"] == "Monitor").sum()))
    c4.metric("Lower Attention", int((vehicle["maintenance_category"] == "Lower Attention").sum()))

    st.subheader("Top 10 Vehicles by Maintenance Attention")
    top = vehicle.sort_values("maintenance_attention_score", ascending=False).head(10).sort_values("maintenance_attention_score")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(top["Vehicle_ID"].astype(str), top["maintenance_attention_score"])
    ax.set_xlabel("Maintenance Attention Score")
    ax.set_xlim(0, 100)
    st.pyplot(fig, clear_figure=True)

    st.subheader("Maintenance Status Distribution")
    counts = vehicle["maintenance_category"].value_counts().reindex(
        ["Higher Attention", "Monitor", "Lower Attention"], fill_value=0
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(counts.index, counts.values)
    ax.set_ylabel("Vehicles")
    st.pyplot(fig, clear_figure=True)

    st.subheader("Vehicle Ranking")
    st.dataframe(
        vehicle[["maintenance_rank", "Vehicle_ID", "Make", "Model",
                 "maintenance_attention_score", "maintenance_category",
                 "sensor_anomaly_rate", "Odometer_KM_Start_of_Week",
                 "days_since_service", "vehicle_age_years"]],
        use_container_width=True, hide_index=True
    )

st.divider()
st.caption("Scores are relative fleet-prioritization indicators, not calibrated accident probabilities or confirmed mechanical diagnoses.")
