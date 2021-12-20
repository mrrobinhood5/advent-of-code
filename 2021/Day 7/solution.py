with open('input.txt') as f:
    crabs = [int(x) for x in f.readline().split(',')]

def find_min_steps(crabs):
    counts = []
    for i in range(min(crabs), max(crabs)):
        counts.append(sum([abs(x-i) for x in crabs]))
    return min(counts)

def find_min_steps_exp(crabs):
    counts = []
    for i in range(min(crabs), max(crabs)):
        # thank goodness for the Gauss Summation
        counts.append(sum([int(abs(x-i)*(abs(x-i)+1)/2) for x in crabs]))
    return min(counts)

print(find_min_steps(crabs))
print(find_min_steps_exp(crabs))
