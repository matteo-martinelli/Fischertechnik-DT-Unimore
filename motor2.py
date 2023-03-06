"""
motor.py file: Motor class
"""

import actuator
import revpimodio2
import time


class Motor(actuator.Actuator):
    def __init__(self, name: str, pin: int):
        self.name = name
        self.pin = pin
        # RevPi module
        self.rpi = revpimodio2.RevPiModIO(autorefresh=True, debug=True)
        # Value check before accepting the provided pin
        if not (isinstance(pin, int) and (pin >= 1) and (pin <= 14)):
            raise ValueError("Output pins go from 1 to 14, got {0}".format(pin))
        #self.pin = self.rpi.io['O_' + str(pin)]
        self.pin = self.rpi.io.O_4
        for i in range(len(self.rpi.io)):
            print(self.rpi.io[i])

    def read_state(self) -> bool:
        self.state = self.pin.value
        return self.state

    def activate_motor(self) -> None:
        self.pin.value = True
        self.state = True
        print("Motor activate at pin " + str(self.pin.name))

        
    def deactivate_motor(self) -> None:
        #self.rpi.cleanup()
        self.pin.value = False
        self.state = False
        print("Motor deactivate at pin " + str(self.pin.name))
    
    def activation_test(self) -> None:
        self.activate_motor()
        time.sleep(5)
        self.deactivate_motor()

    def print_io_errors(self):
        print(self.rpi.maxioerrors)

    def module_cleanup(self):
        self.rpi.cleanup()


if __name__ == '__main__':
    # Some test code
    motor = Motor('my_motor', 4)
    #motor.activate_motor()
    #time.sleep(5)
    #motor.deactivate_motor()
    motor.activation_test()
