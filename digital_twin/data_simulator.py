
import numpy as np
from datetime import datetime

from digital_twin.physical_model import ManufacturingCell


class DataSimulator:
    """Simulates sensor data for the manufacturing cell."""

    def __init__(self, cell=None):
        self.cell = cell if cell is not None else ManufacturingCell()

    def generate_data(self, mode="Normal"):
        """Generate simulated sensor measurements."""

        if mode == "Normal":
            temperature = np.random.uniform(45, 65)
            vibration = np.random.uniform(0.5, 2.5)
            motor_speed = np.random.uniform(1400, 1500)
            power = np.random.uniform(1.5, 2.4)

        elif mode == "Warning":
            temperature = np.random.uniform(70, 79)
            vibration = np.random.uniform(3.5, 4.4)
            motor_speed = np.random.uniform(1300, 1390)
            power = np.random.uniform(2.4, 2.9)

        elif mode == "Fault":
            temperature = np.random.uniform(85, 100)
            vibration = np.random.uniform(5.0, 7.0)
            motor_speed = np.random.uniform(1100, 1250)
            power = np.random.uniform(3.0, 3.5)

        else:
            raise ValueError(
                "Invalid mode. Choose Normal, Warning, or Fault."
            )

        return {
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "temperature": round(temperature, 2),
            "vibration": round(vibration, 2),
            "motor_speed": round(motor_speed, 2),
            "power": round(power, 2),
            "mode": mode
        }
