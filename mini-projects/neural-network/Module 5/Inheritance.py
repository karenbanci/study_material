class Vehicle:
    def __init__(self):
        self._headlight_status = False

    @property
    def headlight_status(self):
        return self._headlight_status

    @headlight_status.setter
    def headlight_status(self, state: bool):
        self._headlight_status = state


class GasVehicle(Vehicle):
    def __init__(self):
        self._tank_status = "Empty"
        super().__init__()

    def fuel_up(self):
        print("Going to the gas station")
        self._tank_status = "Full"


class Battery:
    def __init__(self):
        self._status = "Empty"

    def charge(self):
        self._status = "Full"

    def drain(self):
        self._status = "Empty"


class ElectricVehicle(Vehicle):
    def __init__(self):
        self._my_battery = Battery()
        super().__init__()

    def fuel_up(self):
        print("Charging now")
        self._my_battery.charge()

