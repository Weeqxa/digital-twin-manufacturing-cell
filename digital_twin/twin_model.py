
from digital_twin.physical_model import ManufacturingCell


class DigitalTwin:
    """Digital representation of the manufacturing cell."""

    def __init__(self, cell=None):
        self.cell = cell if cell is not None else ManufacturingCell()

        self.current_state = None
        self.history = []

    def update(self, sensor_data):
        """Update the digital twin using sensor measurements."""

        temperature = sensor_data["temperature"]
        vibration = sensor_data["vibration"]
        motor_speed = sensor_data["motor_speed"]
        power = sensor_data["power"]

        alerts = []

        # Check critical conditions
        if temperature >= self.cell.motor.temperature_limit:
            alerts.append("Critical motor temperature")

        if vibration >= self.cell.motor.vibration_limit:
            alerts.append("Critical motor vibration")

        if motor_speed < self.cell.motor.min_speed:
            alerts.append("Motor speed below minimum")

        if power > self.cell.motor.rated_power:
            alerts.append("Power consumption above rated power")

        # Check warning conditions
        if temperature >= 70 and temperature < self.cell.motor.temperature_limit:
            alerts.append("High motor temperature")

        if vibration >= 3.5 and vibration < self.cell.motor.vibration_limit:
            alerts.append("High motor vibration")

        if motor_speed < 1400 and motor_speed >= self.cell.motor.min_speed:
            alerts.append("Reduced motor speed")

        if power >= 2.4 and power <= self.cell.motor.rated_power:
            alerts.append("Increased power consumption")

        # Determine equipment status
        if any("Critical" in alert or "below minimum" in alert
               or "above rated" in alert for alert in alerts):
            status = "Fault"

        elif alerts:
            status = "Warning"

        else:
            status = "Normal"

        # Update digital representation
        self.current_state = {
            "timestamp": sensor_data["timestamp"],
            "temperature": temperature,
            "vibration": vibration,
            "motor_speed": motor_speed,
            "power": power,
            "status": status,
            "alerts": alerts
        }

        # Save measurement in history
        self.history.append(self.current_state.copy())

        return self.current_state

    def get_current_state(self):
        """Return the latest digital twin state."""

        return self.current_state

    def get_history(self):
        """Return measurement history."""

        return self.history
