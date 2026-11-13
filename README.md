
# Digital Twin – Manufacturing Cell

## Project Description

This project implements a simple Digital Twin of an industrial manufacturing cell consisting of a conveyor belt and an electric motor.

The system simulates sensor measurements, updates a digital representation of the equipment, detects abnormal operating conditions and visualizes the results using an interactive dashboard.

## Technologies

- Python 3
- Streamlit
- NumPy
- Pandas
- Plotly

## System Features

- Physical model of a manufacturing cell
- Simulated sensor data
- Digital Twin model
- Equipment condition monitoring
- Anomaly detection using threshold-based rules
- Interactive monitoring dashboard
- Historical measurement storage in CSV

## Monitored Parameters

| Parameter | Unit |
|---|---|
| Temperature | °C |
| Vibration | mm/s |
| Motor Speed | RPM |
| Power Consumption | kW |

## Simulation Modes

- Normal – normal equipment operation
- Warning – abnormal operating conditions
- Fault – simulated critical equipment conditions

## Project Structure

```text
Digital_Twin/
├── dashboard/
├── data/
├── digital_twin/
├── screenshots/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Weeqxa/digital-twin-manufacturing-cell.git
cd digital-twin-manufacturing-cell
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run main.py
```

Open the application in your browser:

http://localhost:8501

## Important Note

This project uses simulated sensor data.
It is an educational Digital Twin prototype and
is not connected to real industrial equipment.

## Author

Volodymyr Ihnatov

## Course

Architektúry informačných systémov a prediktívna údržba
