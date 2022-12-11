from __future__ import annotations


with open('input.txt') as f:
    raw_data = [[[int(z) for z in y.split('-')] for y in x.rstrip().split(',')] for x in f.readlines()]


def check_if_subset(first_group, second_group) -> bool:
    make_set = lambda x: set(range(x[0], x[1]+1))
    if make_set(first_group) <= make_set(second_group) or make_set(second_group) <= make_set(first_group):
        return True
    else:
        return False


def check_if_any(first_group, second_group) -> bool:
    for each in range(first_group[0], first_group[1]+1):
        if each in range(second_group[0], second_group[1]+1):
            return True

    return False


def part_1(assignments: list[list[list[int]]]) -> int:
    x = []
    for group in assignments:
        x.append(check_if_subset(*group))
    return sum(x)


def part_2(assignments: list[list[list[int]]]):
    x = []
    for group in assignments:
        x.append(check_if_any(*group))
    return sum(x)


print(raw_data)
print(part_2(raw_data))