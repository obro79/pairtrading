from enum import Enum


class Actions(Enum):
    LONG_A_SHORT_B = 1
    LONG_B_SHORT_A = -1
    EXIT_POSITION = 2
    HOLD = 0
