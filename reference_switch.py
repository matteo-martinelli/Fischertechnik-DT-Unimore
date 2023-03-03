"""
reference_switch.py file: ReferenceSwitch class
"""

import sensor
import revpimodio2


class ReferenceSwitch(sensor.Sensor):
    def __init__(self, name: str, pin: int):
        super.__init__()
        self.name = name
        self.pin = pin
        self._rpi = revpimodio2.RevPiModIO(autorefresh=True)
        self.__rpi_pinout_list = [self._rpi.io.I_1, self._rpi.io.I_2, self._rpi.io.I_3, self._rpi.io.I_4,
                                  self._rpi.io.I_5, self._rpi.io.I_6, self._rpi.io.I_7, self._rpi.io.I_8,
                                  self._rpi.io.I_9]

    def read_state(self) -> bool:
        self.state = self.__rpi_pinout_list[self.pin - 1]
        return self.state


if __name__ == '__main__':
    # Some test code
    reference_switch = ReferenceSwitch('my_reference_switch', 1)
    print(reference_switch.read_state())
