import re

file = open('./Day 2/input.txt', 'r')
input = [line.strip() for line in file]

# print(input)

horizontal = 0
depth = 0
depth_2 = 0
aim = 0

for command in input:
    match = re.match('([a-z]+) (\d)', command)
    direction = match.group(1)
    increment = int(match.group(2))
    if direction == 'forward':
        horizontal += increment
        depth_2 += aim * increment
        continue
    elif direction == 'up':
        depth -= increment
        aim -= increment
        continue
    elif direction == 'down':
        depth += increment
        aim += increment
        continue
print(f'The final product is {horizontal} x {depth} = {horizontal*depth}')
print(
    f'The revised final product is {horizontal} x {depth_2} = {horizontal*depth_2}')
