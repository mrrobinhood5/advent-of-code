with open('./test_input.txt') as f:
    fish_tank = [int(x) for x in f.readline().split(',')]

def do_the_thing(days, fish_tank):
    while days:
        temp_tank = []
        for index, fish in enumerate(fish_tank):
            # do the checks
            if not fish: # all 0s go to 6s and adds a new 8
                fish_tank[index] = 6
                temp_tank.append(8)
            else:
                fish_tank[index] -= 1
        fish_tank += temp_tank
        days -= 1
    return len(fish_tank)

print(do_the_thing(256, fish_tank))