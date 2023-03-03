# -*- coding: utf-8 -*-
import revpimodio2
import actuator
import time


class Test(actuator.Actuator):
    def __init__(self, name: str, pin: int):
        super().__init__(name)

        self.rpi = revpimodio2.RevPiModIO(autorefresh=True)
        self.rpi.handlesignalend(self.rpi_cleanup)
        
        self.pin = pin
        #self.state = self.get_state()

        print("Go into cycleloop")
        self.rpi.cycleloop(self.cycleprogram, blocking=False)
    
    def set_state(self, value: bool):
        self.rpi.io['O_' + str(self.pin)].value = value
        print('State set to: ' + str(value))
    
    def get_state(self) -> bool:
        print('The state is ' + str(self.state))
        return self.state
    
    def cycleprogram(self, cycletools):
        """This function is automatically executed every IO cycle."""
        pin_state = self.get_state()
        
        if (pin_state != self.state):
            self.set_state(self.state)
            #self.rpi.io['O_' + str(self.pin)].value = self.state
        
    def rpi_cleanup(self):
        """This function does cleanup work before the end of the program."""
        self.rpi.core.a1green.value = False
        self.rpi.io['O_' + str(self.pin)].value = False

if __name__ == '__main__':
    motor_saw = Test('my_saw', 3)
    motor_saw.set_state(True)
    time.sleep(2) 
    motor_saw.set_state(False)
    