import numpy as np
file = open('./Day 4/input.txt', 'r')
input = [line.strip() for line in file]

# Remove first row
bingo_numbers = [int(number) for number in input.pop(0).split(',')]

# Read boards; 1 blank line, 5 number lines
boards = []
while input:
    board = [[int(number.strip()) for number in input[i+1].split()]
             for i in range(5)]
    input = input[6:]
    boards.append(board)


def checkWin(board, drawn_numbers):
    # Horizontal checks
    for row in board:
        if set(row) <= set(drawn_numbers):
            return True
    # Vertical checks
    for column in np.transpose(board):
        if set(column) <= set(drawn_numbers):
            return True
    np.transpose(board)  # flip it back
    return False


drawn_numbers = []
winning_board = []
losing_board = []
unwon_boards = boards[:]
while bingo_numbers:
    drawn_numbers.append(bingo_numbers.pop(0))
    # print(f'Drawn: {drawn_numbers}')
    # print(boards)
    for board in boards:
        if checkWin(board, drawn_numbers):
            if not winning_board:
                winning_board = board
                winning_numbers = drawn_numbers[:]
            if len(unwon_boards) == 1:
                losing_board = unwon_boards.pop()
                break
            else:
                unwon_boards.remove(board)
    boards = unwon_boards[:]
    if losing_board:
        break


sum_numbers = []
for row in winning_board:
    for number in row:
        if number not in winning_numbers:
            sum_numbers.append(number)
winning_total = sum(sum_numbers)
sum_numbers = []
for row in losing_board:
    for number in row:
        if number not in drawn_numbers:
            sum_numbers.append(number)
losing_total = sum(sum_numbers)

print(
    f'The sum of unmarked numbers is is: {winning_total} and the final number called was {winning_numbers[-1]} for a total score of {winning_total * winning_numbers[-1]} ')
print(
    f'The sum of unmarked numbers is is: {losing_total} and the final number called was {drawn_numbers[-1]} for a total score of {losing_total * drawn_numbers[-1]} ')
