with open('input.txt') as f:
    raw_data = [int(d.rstrip()) for d in f.readlines()]


def sonar_sweep(data, count=0):
    for i, d in enumerate(data):
        if i:
            count += 1 if d > data[i - 1] and i else 0
    return count


def sonar_sweep_window(data, sums=[]):
    for i, d in enumerate(data):
        if i == len(data) - 2:
            break
        else:
            sums.append(sum(data[i:i+3]))
    return sonar_sweep(sums)


print(f'Part 1: {sonar_sweep(raw_data)}')
print(f'Part 2: {sonar_sweep_window(raw_data)}')
