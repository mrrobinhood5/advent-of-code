import re
from itertools import starmap
from operator import mul


def get_memory() -> str:
    with open('input.txt', 'r') as file:
        return file.read().strip()


def solution1(memory: str):
    return sum(
        starmap(
            mul, map(
                lambda nums: (int(nums[0]), int(nums[1])),
                re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",
                           memory))))


def solution2(memory: str):
    return solution1(
        re.sub(r"(?s)don't\(\).*?(?:do\(\)|$", "", memory))


def print_solutions():
    memory = get_memory()
    print(solution1(memory))
    print(solution2(memory))


if __name__ == "__main__":
    print_solutions()
