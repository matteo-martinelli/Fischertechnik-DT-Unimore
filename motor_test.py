# -*- coding: utf-8 -*-
import revpimodio2
import time


class Test(object):
    def __init__(self):
        self.rpi = revpimodio2.RevPiModIO(autorefresh=True)
        self.rpi.handlesignalend(self.rpi_cleanup)
        
        self.pin = 3
        self.state = self.rpi.io['O_' + str(self.pin)].value

        print("Go into cycleloop")
        self.rpi.cycleloop(self.cycleprogram, blocking=False)
        print("Left the cycleloop")
    
    def set_state(self, value: bool):
        self.state = value
    
    def get_state(self) -> bool:
        return self.state
        
    def cycleprogram(self, cycletools):
        """This function is automatically executed every IO cycle."""
        pin_state = self.rpi.io['O_' + str(self.pin)].value
        
        if (pin_state != self.state):
            self.rpi.io['O_' + str(self.pin)].value = self.state
        
    def rpi_cleanup(self):
        """This function does cleanup work before the end of the program."""
        self.rpi.core.a1green.value = False
        self.rpi.io['O_' + str(self.pin)].value = False

if __name__ == '__main__':
    motor_saw = Test()
    print('Setting the state to True')
    motor_saw.set_state(True)
    time.sleep(5)
    print('Setting the state to False')
    motor_saw.set_state(False)
    