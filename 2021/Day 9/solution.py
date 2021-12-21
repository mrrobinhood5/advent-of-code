with open('test_input.txt') as f:
    height_map = [[int(y) for y in x.rstrip()] for x in f.readlines()]


def find_hotspots(height_map):
    low_spots = []
    low_spots_coords = []
    for row_num, row in enumerate(height_map):
        for col_num, each in enumerate(row):
            # define whats the left, right, up and down. If its on an edge, it counts as being smaller
            left = each+1 if not col_num else row[col_num-1]
            right = each+1 if col_num == len(row)-1 else row[col_num+1]
            up = height_map[row_num-1][col_num] if row_num else each+1
            down = height_map[row_num+1][col_num] if row_num != len(height_map)-1 else each+1
            #compare it to all 4 coords
            if left > each < right:
                if up > each < down:
                    low_spots.append(each)
                    low_spots_coords.append((row_num, col_num))
    # to get the risk level, its sum of the numbers plus the amount of numbers
    return sum(low_spots) + len(low_spots)

def find_basins(height_map):
    basins = []
    # iterate over all the cells
    for row_num, row in enumerate(height_map):
        for col_num, each in enumerate(row):
            # define whats the left, right, up and down. If its on an edge, it counts as being smaller
            left = each+1 if not col_num else row[col_num-1]
            right = each+1 if col_num == len(row)-1 else row[col_num+1]
            up = height_map[row_num-1][col_num] if row_num else each+1
            down = height_map[row_num+1][col_num] if row_num != len(height_map)-1 else each+1
            #compare it to all 4 coords
            if left > each < right:
                if up > each < down:
                    this_basin = [(row_num, col_num)]
                    # this is where a low point is. now we gotta 
                    

    return



print(f'Day 9, Part 1: {find_hotspots(height_map)}')
print(f'Day 9, Part 2: {find_basins(height_map)}')