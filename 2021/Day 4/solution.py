with open('./input.txt') as f:
    raw_data = [d.rstrip() for d in f.readlines()]

n = raw_data.pop(0).split(',')

def format_raw(raw_data):
    d, t = [], []
    for row in raw_data:
        if row:
            t.append(row.split())
        if len(t) == 5:
            d.append(t)
            t = []
    return d


def play_bingo(cards, numbers, flag=0):
    ci, ni = 0, 0
    if not flag:
        c,_, n,_ = checkrows(cards, numbers)
        return c, int(n)
    else:
        while cards:
            c, ci, n, ni = checkrows(cards, numbers[ni:])
            cards.pop(ci)
            if not cards:
                return c, int(n)


def checkrows(cards, numbers):
    ccard = []
    for number in numbers:
        for card in cards:
            for row in card:
                if number in row:
                    card[card.index(row)][row.index(number)] = 'x'
                    ccard = [[card[j][i] for j in range(len(card))] for i in range(len(card[0]))]
                if ['x']*5 in card or ['x']*5 in ccard:
                    return card, cards.index(card), number, numbers.index(number)
            
def find_totals(card, number):
    total = 0
    for row in card:    
        total += sum([int(x) for x in row if x != 'x'])
    return total * number

print(f'Day 4, Part1: {find_totals(*play_bingo(format_raw(raw_data), n))}')
print(f'Day 4, Part2: {find_totals(*play_bingo(format_raw(raw_data), n, flag = 1))}')
