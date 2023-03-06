"""
test.py: RevPiModIOTest class
Class to test the subscription to event handling.
"""

import revpimodio2
import time

class RevPiModIOTest():
    """Small test class for the mainloop().
    When the instantiation of the class calls the start() function, we go into 
    the mainloop(). The program then waits for events.
    Ctrl + C will leave the mainloop() cleanly.
    """
    def __init__(self):
        """Invoked during instantiation."""
        # RevPiModIO instantiating and set the Module in the autorefresh, so
        # the process image is automatically synchronized.
        self.revpi = revpimodio2.RevPiModIO(autorefresh=True)

        # Handle exit signal (Ctrl+C / SIGTERM) and exit the Loop.
        # You can pass a function to cleanup your RevPi (switch LEDs
        # off - it is the last read / write on process image before exit.
        self.revpi.handlesignalend(self.exitfunction)
        
        # Register a function in event handling for Input, which is executed,
        # when the Input value changes.
        # I_9 oven light sensor pin
        self.revpi.io.I_3.reg_event(self.eventfunction)
        self.revpi.io['O_10'].value = True

    def eventfunction(self, ioname, iovalue):
        """Only executed if an input pin changes its value.
        @param ioname: Is passed automatically and contains the IO name
        @param iovlaue: Value the IO has at the time of triggering"""
        # Inputs are mirrored to outputs and a screen is Output.
        # Only if the event is triggered!
        print(time.time(), ioname, iovalue)
        if(iovalue == True):
            """
            self.revpi.io['O_13'].value = True  # Open the oven door
            time.sleep(1)                       # Wait for the process
            self.revpi.io['O_5'].value = False  # Move the carrier inside the oven
            time.sleep(5)                       # Wait for the process
            self.revpi.io['O_13'].value = False # Close the oven door
            #time.sleep(5)                       # Wait for the process
            self.revpi.io['O_9'].value = True   # Turn on the oven light
            time.sleep(5)                       # Wait for the process
            self.revpi.io['O_9'].value = False  # Turn off the oven light
            #time.sleep(5)                       # Wait for the process
            self.revpi.io['O_13'].value = True  # Open the oven door
            time.sleep(1)                       # Wait for the process
            self.revpi.io['O_6'].value = False  # Move the carrier outside the oven
            time.sleep(5)                       # Wait for the process
            self.revpi.io['O_13'].value = False # Close the oven door
            print('process ended')
            """
            self.revpi.io['O_13'].value = True  # Open the oven door
            time.sleep(2)
            self.revpi.io['O_5'].value = True  # Move the carrier inside the oven
            time.sleep(7)
            if(self.revpi.io['I_7'].value):
                self.revpi.io['O_5'].value = False  # Move the carrier inside the oven    
            self.revpi.io['O_13'].value = False # Close the oven door
            
            

    
    def exitfunction(self):
        """This function does cleanup work before the end of the program."""
        # Turn off LED A1 on the Core
        self.revpi.core.A1 = revpimodio2.OFF
        self.revpi.io["O_1"].value = False
        self.revpi.io["O_2"].value = False
        self.revpi.io["O_3"].value = False
        self.revpi.io["O_4"].value = False
        self.revpi.io["O_5"].value = False
        self.revpi.io["O_6"].value = False
        self.revpi.io["O_7"].value = False
        self.revpi.io["O_8"].value = False
        self.revpi.io["O_9"].value = False
        self.revpi.io["O_10"].value = False
        self.revpi.io["O_11"].value = False
        self.revpi.io["O_12"].value = False
        self.revpi.io["O_13"].value = False
        self.revpi.io["O_14"].value = False
        
    
    def start(self):
        """Here the actual program runs in the endless loop."""
        # Set LED A1 at Core to green
        self.revpi.core.A1 = 1
        # Go into the mainloop and wait for events
        print("Go in to the mainloop()")
        self.revpi.mainloop()

if __name__ == "__main__":
    root = RevPiModIOTest()
    root.start()