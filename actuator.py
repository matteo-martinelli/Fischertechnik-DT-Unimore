"""
actuator.py file: Actuator class
"""


class Actuator(object):
    def __init__(self):
        self.state = False
        self.read_state()   # For state initialising

    def read_state(self) -> bool:
        pass

    def write_state(self) -> bool:
        pass
