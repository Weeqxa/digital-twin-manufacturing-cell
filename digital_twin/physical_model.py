
from dataclasses import dataclass


@dataclass
class Motor:
    """Physical model of the electric motor."""

    name: str = "Electric Motor M-01"

    nominal_speed: float = 1450.0  # RPM
    rated_power: float = 3.0       # kW

    temperature_limit: float = 80.0  # °C
    vibration_limit: float = 4.5     # mm/s

    min_speed: float = 1300.0  # RPM
    max_speed: float = 1500.0  # RPM


@dataclass
class Conveyor:
    """Physical model of the conveyor belt."""

    name: str = "Conveyor Belt C-01"

    length: float = 5.0       # meters
    nominal_speed: float = 1.2  # m/s


class ManufacturingCell:
    """Description of the manufacturing cell."""

    def __init__(self):
        self.name = "Manufacturing Cell MC-01"

        # Physical components
        self.motor = Motor()
        self.conveyor = Conveyor()

        # Available sensors
        self.sensors = [
            "Temperature Sensor",
            "Vibration Sensor",
            "Speed Sensor",
            "Energy Meter"
        ]

    def get_description(self):
        """Return information about the manufacturing cell."""

        return {
            "cell_name": self.name,
            "motor": self.motor.name,
            "conveyor": self.conveyor.name,
            "sensors": self.sensors
        }
