from collections import Counter

with open('./input.txt') as f:
    raw_data = [d.rstrip() for d in f.readlines()]
initial_data = [[[int(i) for i in y.split(',')] for y in x.split(' -> ')] for x in raw_data]


def find_hot_spots(data, straights = True):
    my_count = Counter()
    for coords in data:
        temp = []
        ((x1, y1),(x2, y2)) = sorted(coords)

        if (x1 == x2 or y1 == y2):
            for t in range(x1, x2+1):
                temp.append((t, y1))
                temp.append((t, y2))
            for t in range(y1, y2+1):
                temp.append((x1, t))
                temp.append((x2, t))   
                 
        if not straights:
            if (x1 != x2 and y1 != y2):
                slope = (y2-y1)/(x2-x1)
                for t in range(x1, x2+1):
                    temp.append((t, int(y1)))
                    y1 += slope
        my_count.update(Counter(set(temp)))
    return len([v for v in my_count.values() if v > 1])

print(f'Day 5, Part 1: {find_hot_spots(initial_data)} ')
print(f'Day 5, Part 2: {find_hot_spots(initial_data, straights=False)} ')
