"""
sensor.py file: Sensor class
"""

import revpimodio2
#import time
from multiprocessing import Pool

class Sensor(object):
    def __init__(self, sensor_name: str, pin: int):
        self.sensor_name = sensor_name                    
        self.state = False                          
        # RevPi module
        self.rpi = revpimodio2.RevPiModIO(autorefresh=True)
        # Value check before accepting the provided pin
        if not (isinstance(pin, int) and (pin >= 1) and (pin <= 9)):
            raise ValueError("Input pins go from 1 to 9, got {0}".format(pin))
        self.pin = self.rpi.io['I_' + str(pin)]
        
        # RevPi Settings
        # Set the exit signal (ctrl+C) and exit loop actions
        self.rpi.handlesignalend(self.exit_function)
        # Monitoring the selected input; subscribing a function when the input 
        # changes
        self.pin.reg_event(self.event_function)

    # Executed only if an input pin changes its value
    def event_function(self, ioname, iovalue) -> None:
        self.state = iovalue
        if __name__ == '__main__':
            print(ioname, iovalue)

    # Executed at the program end to clean up before the end of it
    def exit_function(self):
        self.rpi.core.A1 = revpimodio2.OFF

    # Here the program starts the endless loop
    def start(self):
        # Set LED A1 at Core to green
        self.rpi.core.A1 = 1
        # Go into the mainloop and wait for events
        print("Go in to the mainloop()")
        self.rpi.mainloop()


if __name__ == '__main__':
    # Some test code
    light_sensor = Sensor('my_light_sensor', 3)
    light_sensor.start()
    