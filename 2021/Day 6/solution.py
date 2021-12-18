from collections import deque

with open('input.txt') as f:
    fish_tank = [int(x) for x in f.readline().split(',')]

def do_the_thing_efficiently(days, fish_tank):
    # build the deque
    d = deque([fish_tank.count(i) for i in range(0,9)])
    
    # play musical chairs
    for i in range(0, days):
        d[7] += d[0] if d[0] else 0
        d.rotate(-1)
    return(sum(d))

# print(do_the_thing(256, fish_tank))
print(do_the_thing_efficiently(256, fish_tank))