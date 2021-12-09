with open('input.txt') as f:
    raw_data = [d.rstrip() for d in f.readlines()]


def get_life_support(data):
    bit_length = len(data[0])
    max_data, min_data = data, data

    # do the max bits first
    for l in range(bit_length):
        max_bits = [d[l] for d in max_data]
        mx = get_maxes(max_bits)
        max_data = [x for x in max_data if x[l] == mx]
        if len(max_data) == 1:
            break

    # do the min bits
    for l in range(bit_length):
        min_bits = [d[l] for d in min_data]
        mn = get_maxes(min_bits, mx=False)
        min_data = [x for x in min_data if x[l] == mn]
        if len(min_data) == 1:
            break
    print(min_data)
    ogr, csr = f'0b{max_data[0]}', f'0b{min_data[0]}'
    print(ogr, csr)
    return int(ogr, base=2) * int(csr, base=2)


def get_maxes(data, mx=True):
    if mx:
        return "1" if data.count("1") >= data.count("0") else "0"
    else:
        return "0" if data.count("0") <= data.count("1") else "1"


def get_power_consumption(data):
    bit_length, gamma, epsilon = len(data[0]), '0b', '0b'

    for l in range(bit_length):
        temp_bits = [int(d[l]) for d in data]
        gamma += get_bits(temp_bits)
        epsilon += get_bits(temp_bits, False)

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    return gamma * epsilon


def get_bits(l, m=True):
    if m:
        return str(max(l, key=l.count))
    else:
        return str(min(l, key=l.count))


print(f'Day 3, Part 1: {get_power_consumption(raw_data)}')
print(f'Day 3, Part 2: {get_life_support(raw_data)}')
