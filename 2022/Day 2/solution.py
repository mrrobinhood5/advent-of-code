from __future__ import annotations


# open the input
with open('input.txt') as f:
    raw_data = [[y for y in x.rstrip().split()] for x in f.readlines()]

# the point system
points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
# outcomes = {
#     'T': [['A','X'], ['B','Y'], ['C','Z']],
#     'L': [['A','Z'], ['B','X'], ['C','Y']],
#     'W': [['A','Y'], ['B','Z'], ['C','X']]
# }

outcomes = {
    # X = LOSE, Y = DRAW, Z = WIN
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
}
# scoring = {
#     'T': 3,
#     'W': 6,
#     'L': 0
# }

scoring = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def match(moves: list[list[str]]) -> int:
    outcome = []
    tally = []
    # iterate all outcomes
    for move in moves:
        tally.append(points[move[1]])
        for result, possibilities in outcomes.items():
            if move in possibilities:
                outcome.append(result)

    # score the outcomes
    total_score = sum([scoring[x] for x in outcome]) + sum(tally)
    return total_score


def match2(moves: list[list[str]]) -> int:
    outcome = []
    tally = []
    # iterate all outcomes
    for move in moves:
        # add points for wins/losses
        tally.append(scoring[move[1]])
        #
        outcome.append(points[outcomes[move[1]][move[0]]])

    # score the outcomes
    total_score = sum(outcome) + sum(tally)
    return total_score


print(match2(raw_data))
