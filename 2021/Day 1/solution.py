with open('input.txt') as f:
    raw_data = f.readlines()
    raw_data = [int(d.rstrip()) for d in raw_data]


def sonar_sweep(data, count=0):
    for i, d in enumerate(data):
        if i:
            count += 1 if d > data[i - 1] and i else 0
    return count


def sonar_sweep_window(data):
    sums = []
    for i, d in enumerate(data):
        if i == len(data) - 2:
            break
        else:
            sums.append(sum(data[:i+2]))
    return sums

print(sonar_sweep(raw_data))
print(sonar_sweep_window(raw_data))
