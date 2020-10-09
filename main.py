from player import Player
from itertools import cycle
from random import randint
from swing_result import SwingResult
from deadball_enums import SwingResultType
from tables import hit, crit_hit

print("OH! THAT'S A BASEBALL!!")
print()

away_team = [
    Player('Immanuel Kant', 'SS', 29, 'S', ['S+', 'D+']),
    Player('Friedrich Nietzsche', 'LF', 34, 'L', ['C+']),
    Player('Arthur Schopenhauer', '1B', 28, 'L', ['C-']),
    Player('Friedrich Schlegel', 'CF', 26, 'R', ['D+']),
    Player('Gottfried Leibniz', 'C', 23, 'R', ['S+']),
    Player('Georg Hegel', '2B', 24, 'R', []),
    Player('Karl Jaspers', '3B', 21, 'L', []),
    Player('Martin Heidegger', 'RF', 20, 'L', []),
    Player('Karl Marx', 'P', 7, 'R', [], 6)
]

home_team = [
    Player('Empedocles', 'LF', 25, 'S', ['S+']),
    Player('Plato', '1B', 32, 'L', []),
    Player('Epicurus', '3B', 28, 'R', []),
    Player('Aristotle', 'RF', 27, 'R', []),
    Player('Epictetus', 'C', 26, 'L', []),
    Player('Heraklitus', 'CF', 25, 'L', ['S+', 'D+']),
    Player('Democritus', '2B', 25, 'R', []),
    Player('Archimedes', 'SS', 22, 'R', []),
    Player('Sophocles', 'P', 8, 'L', [], 6)
]

is_away_team_batting = True
away_batters = cycle(away_team)
home_batters = cycle(home_team)
batters = away_batters
pitcher = home_team[-1]

thats_the_ballgame = False
inning = 1
score_away = [0, []]
score_home = [0, []]
scoreboard = [
    score_away,
    score_home
]
runs_this_half_inning = 0
outs = 0
bases = '000'
while not thats_the_ballgame:
    batter = next(batters)

    print(f'batter: {batter.name} bt: {batter.bt}')
    print(f'pitcher: {pitcher.name} pd: {pitcher.pd}')

    swing = randint(1, 100)
    pitch = randint(1, pitcher.pd)
    mss = swing + pitch
    print(f'swing: {swing} + pitch: {pitch} = mss: {mss}')

    if mss <= 5:
        swing_result = crit_hit()
    elif mss <= batter.bt:
        swing_result = hit()
    elif mss <= batter.bt + 5:
        swing_result = SwingResult(SwingResultType.WALK)
    else:
        swing_result = SwingResult(SwingResultType.OUT, 1)

    if swing_result.type is SwingResultType.OUT:
        outs += swing_result.value
        print('OUT!')
    elif swing_result.type is SwingResultType.WALK:
        bases = list(bases)
        for i, base in enumerate(reversed(bases)):
            if base != '1':
                bases[-i - 1] = '1'
                bases = "".join(bases)
                break
        else:
            runs_this_half_inning += 1
        print('Walk')
        print(f'Bases: {bases}')
    else:
        batter_moves, runners_move = swing_result.value
        if runners_move >= 3:
            runs_this_half_inning += bases.count('1')
            bases = '000'
        elif runners_move == 2:
            if bases[-3] == '1':
                runs_this_half_inning += 1
            if bases[-2] == '1':
                runs_this_half_inning += 1
            if bases[-1] == '1':
                bases = '100'
            else:
                bases = '000'
        else:
            if bases[-3] == '1':
                runs_this_half_inning += 1
                bases = '0' + bases[-2:]
            if bases[-2] == '1':
                bases = '10' + bases[-1]
            if bases[-1] == '1':
                bases = bases[-3] + '10'

        if batter_moves < 4:
            bases = list(bases)
            bases[-batter_moves] = '1'
            bases = "".join(bases)
        else:
            runs_this_half_inning += 1

        print(f'Hit! Runners take {runners_move} base(s), batter takes {batter_moves} base(s)')
        print(bases)

    print()

    if outs >= 3:
        outs = 0
        bases = '000'

        if is_away_team_batting:
            is_away_team_batting = False
            batters = home_batters
            pitcher = away_team[-1]
        else:
            thats_the_ballgame = True
