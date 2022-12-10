from __future__ import annotations


# just change this from test_input to input
with open('input.txt') as f:
    raw_data = [x.rstrip() for x in f.readlines()]
    data, y = [], []
    for x in range(len(raw_data)):

        if raw_data[x] != '':
            y.append(int(raw_data[x]))
        else:
            data.append(y)
            y = []


def day_1(calorie_data: list[list[int]]) -> int:
    # This just calculates which is the top group sum
    calories = [sum(x) for x in calorie_data]
    return max(calories)


def day_1_p2(calorie_data: list[list[int]]) -> int:
    # This should get the top 3 and then add those
    calories = [sum(x) for x in calorie_data]
    return sum(list(sorted(calories, reverse=True))[:3])


print(day_1_p2(data))
