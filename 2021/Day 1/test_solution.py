from solution import *


def test_sonar_sweep1():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep(data) == 7


def test_sonar_sweep2():
    data = list(reversed([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    assert sonar_sweep(data) == 2


def test_sonar_sweep_window():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar_sweep_window(data) == 5
