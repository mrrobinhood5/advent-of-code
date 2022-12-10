import string


# bring in the input
with open('input.txt') as f:
    raw_data = [x.rstrip() for x in f.readlines()]


def split_rucksack(ruck:str) -> tuple:
    midpoint = int(len(ruck)/2)
    compartments = (ruck[:midpoint], ruck[midpoint:])
    return compartments


def find_item(compartments: tuple[str, str]) -> str:
    # split into sets for each
    x = []
    for letter in compartments[0]:
        if letter in compartments[1]:
            return letter
    raise TypeError


def find_score(letter: str) -> int:
    all_letters = string.ascii_lowercase + string.ascii_uppercase
    return all_letters.index(letter)+1


def break_into_groups(all_rucks: list[str]) -> list[list[str]]:
    grouped_rucks = []
    for index in range(0, len(all_rucks), 3):
        grouped_rucks.append(all_rucks[index:index+3])
    return grouped_rucks


def find_badge(group: list[str]) -> str:
    sorted_rucks = [sorted(set(ruck)) for ruck in group]
    for item in sorted_rucks[0]:
        if item in sorted_rucks[1] and item in sorted_rucks[2]:
            return item
    raise TypeError


def part_1() -> int:
    return sum([find_score(find_item(split_rucksack(ruck))) for ruck in raw_data])


def part_2() -> int:
    x = []
    for group in break_into_groups(raw_data):
        x.append(find_badge(group))
    return sum([find_score(y) for y in x])


print(part_2())
