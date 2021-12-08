with open('input.txt') as f:
    raw_data = [d.rstrip().split(' ') for d in f.readlines()]


def do_commands(data):
    m = {}
    for command in data:
        m[command[0]] = m.get(command[0], 0) + int(command[1])
    return m['forward'] * (m['down'] - m['up'])


def do_commands_part2(data):
    m = {}
    for d in data:
        c, i = d[0], int(d[1])
        if c == 'down':
            m['aim'] = m.get("aim", 0) + i
        elif c == 'up':
            m['aim'] = m.get("aim", 0) - i
        else:
            m['forward'] = m.get('forward', 0) + i
            m['depth'] = m.get('depth', 0) + (m.get('aim', 0) * i)
    return m['forward'] * m['depth']


print(f'Day 2, Part 1: {do_commands(raw_data)}')
print(f'Day 2, Part 2: {do_commands_part2(raw_data)}')
