from enum import Enum


class Play(Enum):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    TRIPLE = 'Triple'


class SwingResultType(Enum):
    HIT = 'Hit'
    WALK = 'Walk'
    OUT = 'Out'


class DefenseResult(Enum):
    ERROR = 'Error'
    NOTHING = 'Nothing'
    REDUCE_HIT = 'Reduce hit'
    OUT = 'Out'
