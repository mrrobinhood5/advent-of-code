with open('./input.txt') as f:
    raw_data = [d.rstrip() for d in f.readlines()]

n = raw_data.pop(0).split(',')
c, t = [], []

for row in raw_data:
    if row:
        t.append(row.split())
    if len(t) == 5:
        c.append(t)
        t = []


def play_bingo(cards, numbers):
    for number in numbers:
        for card in cards:
            for row in card:
                if number in row:
                    card[card.index(row)][row.index(number)] = 'x'
                if ['x'] * 5 in card:
                    return card, int(number)


def find_totals(card, number):
    total = 0
    for row in card:
        total += sum([int(x) for x in row if x != 'x'])
    return total * number

# print(play_bingo(c, n))
# print(find_totals(*play_bingo(c, n)))