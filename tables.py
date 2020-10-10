from random import randint
from deadball_enums import SwingResultType, DefenseResult
from swing_result import SwingResult


def out():
    n = randint(0, 9)
    if n <= 2:
        return 'K'
    elif n == 3:
        return 'G-3'
    elif n == 4:
        return '4-3'
    elif n == 5:
        return '5-3'
    elif n == 6:
        return '6-3'
    elif n == 7:
        return 'F-7'
    elif n == 8:
        return 'F-8'
    else:
        return 'F-9'


def defense():
    n = randint(1, 12)
    if n <= 2:
        return DefenseResult.ERROR
    if n <= 9:
        return DefenseResult.NOTHING
    elif n <= 11:
        return DefenseResult.REDUCE_HIT
    else:
        return DefenseResult.OUT


def hit():
    n = randint(1, 20)
    if n <= 2:
        return SwingResult(SwingResultType.HIT, (1, 1))
    elif n <= 7:
        defense_result = defense()
        if defense_result is DefenseResult.NOTHING or defense_result is DefenseResult.REDUCE_HIT:
            return SwingResult(SwingResultType.HIT, (1, 1))
        elif defense_result is DefenseResult.ERROR:
            return SwingResult(SwingResultType.HIT, (2, 2))
        else:
            return SwingResult(SwingResultType.OUT, 1)
    elif n <= 12:
        return SwingResult(SwingResultType.HIT, (1, 2))
    elif n <= 15:
        defense_result = defense()
        if defense_result is DefenseResult.NOTHING:
            return SwingResult(SwingResultType.HIT, (2, 2))
        elif defense_result is DefenseResult.ERROR:
            return SwingResult(SwingResultType.HIT, (3, 3))
        elif defense_result is DefenseResult.REDUCE_HIT:
            return SwingResult(SwingResultType.HIT, (1, 2))
        else:
            return SwingResult(SwingResultType.OUT, 1)
    elif n <= 17:
        return SwingResult(SwingResultType.HIT, (2, 3))
    elif n == 18:
        defense_result = defense()
        if defense_result is DefenseResult.NOTHING:
            return SwingResult(SwingResultType.HIT, (3, 3))
        elif defense_result is DefenseResult.ERROR:
            return SwingResult(SwingResultType.HIT, (4, 4))
        elif defense_result is DefenseResult.REDUCE_HIT:
            return SwingResult(SwingResultType.HIT, (2, 3))
        else:
            return SwingResult(SwingResultType.OUT, 1)
    else:
        return SwingResult(SwingResultType.HIT, (4, 4))


def crit_hit():
    n = randint(1, 20)
    if n <= 12:
        return SwingResult(SwingResultType.HIT, (2, 3))
    elif n <= 17:
        return SwingResult(SwingResultType.HIT, (3, 4))
    else:
        return SwingResult(SwingResultType.HIT, (4, 4))