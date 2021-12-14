file = open('./Day 9/input.txt', 'r')
input = [line.strip() for line in file]

heightmap = [[int(number) for number in row] for row in input]

# Add to new list padded with 9s

height = len(heightmap)
width = len(heightmap[0])


padded = [[9] * (width + 2) for _ in range(height + 2)]

for row in range(height):
    padded[row + 1][1:width + 1] = heightmap[row]

low_point_values = []
low_points = []
for row in range(1, height + 1):
    for column in range(1, width + 1):
        val = padded[row][column]
        up = padded[row - 1][column]
        down = padded[row + 1][column]
        left = padded[row][column - 1]
        right = padded[row][column + 1]
        if val < up and val < down and val < left and val < right:
            low_point_values.append(val)
            low_points.append((row, column))
print(
    f'The sum of risk levels is {sum(low_point_values) + len(low_point_values)}!')

basin_sizes = []


def checkAdjacent(row: int, column: int, last_value: int, visited) -> None:
    if ((row, column) in visited):
        return
    val = padded[row][column]
    if val <= last_value or val == 9:
        return
    visited.append((row, column))
    checkAdjacent(row+1, column, val, visited)
    checkAdjacent(row-1, column, val, visited)
    checkAdjacent(row, column+1, val, visited)
    checkAdjacent(row, column-1, val, visited)


for (row, column) in low_points:
    visited = []
    checkAdjacent(row, column, -1, visited)
    # print(visited)
    basin_sizes.append(len(visited))
# print(basin_sizes)
largest = sorted(basin_sizes)[-3:]
print(
    f'The product of the 3 largest basin sizes is: {largest[0] * largest[1] * largest[2]}!')
