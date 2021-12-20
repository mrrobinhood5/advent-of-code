with open('input.txt') as f:
    raw_data = [[y.split(" ") for y in x.rstrip().split(" | ")] for x in f.readlines()]

def do_some_counts(raw_data):
    lengths = [2, 3, 4, 7]
    count = 0
    for _, y in raw_data:
        count += len([e for e in y if len(e) in lengths])
    return count

def decode(raw_data):
    solutions = []
    for digits, problem in raw_data:
        l = [len(x) for x in digits]
        fives, sixes = [x for x in digits if len(x) == 5], [x for x in digits if len(x) == 6]
        
        # get the 1, 4, 7 and 8
        decoded_map = {
            1: digits[l.index(2)],
            4: digits[l.index(4)],
            7: digits[l.index(3)],
            8: digits[l.index(7)]}
        
        # get the 0, 6, 9
        for six in sixes:
            if not all(item in [c for c in six] for item in decoded_map[1]):
                decoded_map.update({6: six})
            elif all(item in [c for c in six] for item in decoded_map[4]):
                decoded_map.update({9: six})
            else:
                decoded_map.update({0: six})

        # get the 2, 3, 5,
        for five in fives:
            if all(item in [c for c in five] for item in decoded_map[1]):
                decoded_map.update({3: five})
            elif all(item in decoded_map[9] for item in [c for c in five]):
                decoded_map.update({5:five})
            else:
                decoded_map.update({2: five})
        
        # solve all the problems
        decoded_map = {"".join(sorted(y)):x for x,y in decoded_map.items()}
        solutions.append(int("".join([str(decoded_map["".join(sorted(x))]) for x in problem])))
    
    return sum(solutions)
        
print(f'Day 8, Part 1: {do_some_counts(raw_data)}')
print(f'Day 8, Part 2: {decode(raw_data)}')