from enum import Enum, auto

class State(Enum):
    INIT = auto()
    INTRO = auto()
    EXPERIENCE = auto()
    END = auto()

class Event(Enum):
    START = auto()
    ANSWER = auto()
    TIMEOUT = auto()

    