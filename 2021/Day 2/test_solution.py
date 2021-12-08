from solution import *


def test_do_commands():
    data = [['forward', '5'], ['down', '5'], ['forward', '8'], ['up', '3'], ['down', '8'], ['forward', '2']]
    assert do_commands(data) == 150


def test_do_commands_part2():
    data = [['forward', '5'], ['down', '5'], ['forward', '8'], ['up', '3'], ['down', '8'], ['forward', '2']]
    assert do_commands_part2(data) == 900
