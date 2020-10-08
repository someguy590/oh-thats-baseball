from random import randint


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


def hit():
    n = randint(1, 20)


def crit_hit():
    n = randint(1, 20)
