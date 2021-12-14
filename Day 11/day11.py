file = open('./Day 11/input.txt')
octopodes = [[int(digit) for digit in line.strip()] for line in file]
# print(octopodes)

width = len(octopodes[0])
height = len(octopodes)

padded = [[0] * (width + 2) for _ in range(height + 2)]
for row in range(height):
    padded[row + 1][1:width+1] = octopodes[row]


def simulate_step() -> int:
    flashes = 0
    # print(f'----step {step}----')
    # print('starting:', padded)
    stack = []
    # Increment the board
    for row in range(1, height + 1):
        for column in range(1, width + 1):
            padded[row][column] += 1

    # Add all octopodes larger than 9 to stack
    for row in range(1, height + 1):
        for column in range(1, width + 1):
            if padded[row][column] > 9:
                stack.append((row, column))

    # Resolve stack, adding octopodes to stack that are exactly 9 before the flash affects them
    # print('incremented:', padded)
    while stack:
        row, column = stack.pop()
        flashes += 1

        for row_offset in [-1, 0, 1]:
            for column_offset in [-1, 0, 1]:
                row_adj = row + row_offset
                column_adj = column + column_offset
                if padded[row_adj][column_adj] == 9:
                    stack.append((row_adj, column_adj))
                padded[row_adj][column_adj] += 1
    # print('resolved:', padded)

    for row in range(1, height + 1):
        for column in range(1, width + 1):
            pass
    # Reset padded borders to 0 and flashed octopodes to 0
    for row in range(height + 2):
        for column in range(width + 2):
            is_edge = row == 0 or row == height + 1 or column == 0 or column == width + 1
            has_flashed = padded[row][column] > 9
            if is_edge or has_flashed:
                padded[row][column] = 0
    # print('reset:', padded)
    return flashes


# Part 1
flash_counter = 0
total_steps = 100
is_synchronized = False

step_counter = 0
# for step in range(1, total_steps + 1):
while not is_synchronized:
    if step_counter < total_steps:
        flash_counter += simulate_step()
    else:
        simulate_step()
    step_counter += 1
    if sum([sum(padded[row]) for row in range(len(padded))]) == 0:
        is_synchronized = True


print(
    f'The octopodes will have flashed {flash_counter} times after 100 steps!')
print(f'It requires {step_counter} steps to synchronize the flashing.')
