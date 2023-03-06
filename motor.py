# -*- coding: utf-8 -*-
import revpimodio2
import actuator
import time


class Motor(actuator.Actuator):
    def __init__(self, name: str, pin: int):
        super().__init__(name)

        self.rpi = revpimodio2.RevPiModIO(autorefresh=True)
        self.rpi.handlesignalend(self.rpi_cleanup)
        
        # Add here the pin number control; if the number is not in the range, 
        # an errore should be raised.
        self.pin = pin
        self.state = self.get_state()

        print("Go into cycleloop")
        self.rpi.cycleloop(self.cycleprogram, blocking=False)
    
    def set_state(self, value: bool) -> None:
        self.rpi.io['O_' + str(self.pin)].value = value
        self.state = value
        print('State set to: ' + str(value))
    
    def get_state(self) -> bool:
        return self.state
    
    def cycleprogram(self, cycletools):
        """This function is automatically executed every IO cycle."""
        pin_state = self.get_state()
        
        if (pin_state != self.state):
            print('here')
            self.set_state(self.state)
        
    def rpi_cleanup(self):
        """This function does cleanup work before the end of the program."""
        self.rpi.core.a1green.value = False
        self.rpi.io['O_' + str(self.pin)].value = False

if __name__ == '__main__':
    conveyor_belt = Motor('conveyor belt', 3)
    conveyor_belt.set_state(True)
    time.sleep(2) 
    conveyor_belt.set_state(False)
    del(conveyor_belt)

    time.sleep(0.5)

    motor_saw = Motor('motor saw', 4)
    motor_saw.set_state(True)
    time.sleep(2) 
    motor_saw.set_state(False)
    del(motor_saw)