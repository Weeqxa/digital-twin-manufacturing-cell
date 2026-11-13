
import streamlit as st
import pandas as pd
import plotly.express as px
import ast
from pathlib import Path

from digital_twin.data_simulator import DataSimulator
from digital_twin.twin_model import DigitalTwin


# Path to historical data
DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "historical_data.csv"
)


def save_history(history):
    """Save measurement history to CSV."""

    df = pd.DataFrame(history)
    df.to_csv(DATA_FILE, index=False)



def load_history():
    """Load historical measurements from CSV."""

    if not DATA_FILE.exists():
        return []

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        return []

    records = df.to_dict(orient="records")

    for record in records:
        alerts = record.get("alerts", [])

        if isinstance(alerts, str):
            record["alerts"] = ast.literal_eval(alerts)

    return records




def render_dashboard():
    """Display the Digital Twin dashboard."""

    st.set_page_config(
        page_title="Digital Twin Dashboard",
        page_icon="🏭",
        layout="wide"
    )

    st.title("🏭 Manufacturing Cell - Digital Twin")
    st.caption(
        "Monitoring and simulation of an industrial conveyor "
        "and electric motor."
    )

    # Initialize simulator and digital twin
    if "simulator" not in st.session_state:
        st.session_state.simulator = DataSimulator()

    if "twin" not in st.session_state:
        st.session_state.twin = DigitalTwin()

        # Restore previous measurements
        history = load_history()

        st.session_state.twin.history = history

        if history:
            st.session_state.twin.current_state = history[-1]

    simulator = st.session_state.simulator
    twin = st.session_state.twin

    # Sidebar controls
    st.sidebar.header("Simulation Controls")

    mode = st.sidebar.selectbox(
        "Operating Mode",
        ["Normal", "Warning", "Fault"]
    )

    generate = st.sidebar.button(
        "Generate New Measurement",
        use_container_width=True
    )

    if generate or twin.get_current_state() is None:

        sensor_data = simulator.generate_data(mode)
        current_state = twin.update(sensor_data)

        save_history(twin.get_history())

    current_state = twin.get_current_state()

    # Equipment status
    st.subheader("Equipment Status")

    status = current_state["status"]

    if status == "Normal":
        st.success("Machine Status: NORMAL")

    elif status == "Warning":
        st.warning("Machine Status: WARNING")

    else:
        st.error("Machine Status: FAULT")

    st.caption(
        f"Last measurement: {current_state['timestamp']}"
    )

    # Sensor measurements
    st.subheader("Current Sensor Measurements")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{current_state['temperature']} °C"
    )

    col2.metric(
        "Vibration",
        f"{current_state['vibration']} mm/s"
    )

    col3.metric(
        "Motor Speed",
        f"{current_state['motor_speed']} RPM"
    )

    col4.metric(
        "Power Consumption",
        f"{current_state['power']} kW"
    )

    # Alerts
    st.subheader("System Alerts")

    alerts = current_state["alerts"]

    if alerts:
        for alert in alerts:
            st.warning(alert)
    else:
        st.info("No active alerts. Equipment is operating normally.")

    # Historical measurements
    st.divider()
    st.subheader("Historical Data")

    history = twin.get_history()

    if history:

        df = pd.DataFrame(history)

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        tab1, tab2, tab3 = st.tabs(
            ["Temperature", "Vibration", "Energy"]
        )

        with tab1:
            fig = px.line(
                df,
                x="timestamp",
                y="temperature",
                title="Motor Temperature (°C)",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            fig = px.line(
                df,
                x="timestamp",
                y="vibration",
                title="Motor Vibration (mm/s)",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            fig = px.line(
                df,
                x="timestamp",
                y="power",
                title="Energy Consumption (kW)",
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Measurement History")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total measurements: {len(df)}"
        )
