class SwingResult:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return '<' \
               f'{self.__class__.__name__} Type:{self.result} ' \
               f'Value:{self.value} ' \
               '>'

    def __str__(self):
        return '<' \
               f'{self.__class__.__name__} Type:{self.result} ' \
               f'Value:{self.value} ' \
               '>'
