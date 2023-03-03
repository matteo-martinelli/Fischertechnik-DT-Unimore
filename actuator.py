"""
actuator.py file: Actuator class
"""


class Actuator(object):
    def __init__(self, name: str):
        self.name = name
        self.state = None
        self.state = self.get_state()   # For state initialising

    def get_state(self) -> bool:
        pass

    def set_state(self) -> None:
        pass
