class Player:
    def __init__(self, name, position, bt, hand, traits, pd=-20, age=24, hot_cold=None, injury=None):
        self.name = name
        self.position = position
        self.bt = bt
        self.traits = traits
        self.hand = hand
        self.age = age
        self.hot_cold = hot_cold
        self.pd = pd
        self.injury = injury

    def __repr__(self):
        return '<' \
               f'Player name:{self.name} ' \
               f'position:{self.position} ' \
               f'bt:{self.bt} ' \
               f'traits:{self.traits} ' \
               f'hand:{self.hand} ' \
               f'age:{self.age} ' \
               f'pd:{self.pd} ' \
               f'Hot/Cold?:{self.hot_cold} ' \
               f'injury:{self.injury}' \
               '>'

    def __str__(self):
        return '<' \
               f'Player name:{self.name} ' \
               f'position:{self.position} ' \
               f'bt:{self.bt} ' \
               f'traits:{self.traits} ' \
               f'hand:{self.hand} ' \
               f'age:{self.age} ' \
               f'pd:{self.pd} ' \
               f'Hot/Cold?:{self.hot_cold} ' \
               f'injury:{self.injury}' \
               '>'
