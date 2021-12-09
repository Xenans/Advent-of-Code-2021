file = open('./Day 8/input.txt', 'r')
input = [line.strip() for line in file]

count_1478 = 0
output_sum = 0
for line in input:
    signal_patterns = line.split()[:10]
    outputs = line.split()[-4:]

    # Part one is simple
    for output_digit in outputs:
        is_1478 = len(output_digit) == 2 or len(output_digit) == 3 or len(
            output_digit) == 4 or len(output_digit) == 7
        if is_1478:
            count_1478 += 1

    # ---Part 2 logic---
    # Length map:
    # 0 : 6 -
    # 1 : 2 (Known)
    # 2 : 5 |
    # 3 : 5 |
    # 4 : 4 (Known)
    # 5 : 5 |
    # 6 : 6 -
    # 7 : 3 (Known)
    # 8 : 7 (Known)
    # 9 : 6 -

    # Map from digit to confused character input
    digit_map = {}
    # Map from actual character (position) to confused character
    character_map = {}

    for digit in signal_patterns:
        characters = set(sorted(digit))
        # 1 gives us C|F
        if len(characters) == 2:
            digit_map[1] = characters
        # 7 gives us A|C|F
        elif len(characters) == 3:
            digit_map[7] = characters
        # 4 gives us B|C|D|F
        elif len(characters) == 4:
            digit_map[4] = characters
        # 8 gives us A|B|C|D|E|F (which tells us nothing)
        elif len(characters) == 7:
            digit_map[8] = characters

    # We know A from 7 - 1
    character_map['a'] = digit_map[7] - digit_map[1]

    # We know B|D from 4 - 1
    temp_bd = digit_map[4] - digit_map[1]
    # We know 6 is the 6 length number that doesn't match 1
    for digit in signal_patterns:
        characters = set(sorted(digit))
        if len(characters) == 6 and not digit_map[1] <= characters:
            digit_map[6] = characters
    # We know C from 1 - 6
    character_map['c'] = digit_map[1] - digit_map[6]
    # We know F by extension
    character_map['f'] = digit_map[1] - character_map['c']
    # We know 3 is 7 with 2 additional digits. One of those digits is unique and is g, the other is the D from 4-1
    for digit in signal_patterns:
        characters = set(sorted(digit))
        if len(characters) == 5 and digit_map[7] <= characters:
            digit_map[3] = characters
    # So we know D and G
    character_map['g'] = digit_map[3] - digit_map[7] - temp_bd
    character_map['d'] = digit_map[3] - digit_map[7] - character_map['g']
    # We know B from extension by 4
    character_map['b'] = temp_bd - digit_map[3]
    # By elimination we know E
    character_map['e'] = digit_map[8] - digit_map[3] - character_map['b']
    # Assign the rest of the digits
    digit_map[0] = digit_map[8] - character_map['d']
    digit_map[2] = digit_map[8] - character_map['b'] - character_map['f']
    digit_map[5] = digit_map[8] - character_map['c'] - character_map['e']
    digit_map[6] = digit_map[8] - character_map['c']
    digit_map[9] = digit_map[8] - character_map['e']

    # Inverse the mapping to make it easier to use
    # Sorted tuples are hashable
    output_map = {
        tuple(sorted(list(digit_map[digit]))): digit for digit in digit_map.keys()}
    # print(line)
    # print(digit_map)
    # print(character_map)
    # print(output_map)

    output = ''
    for output_digit in outputs:
        output += str(output_map[tuple(sorted(list(output_digit)))])
    # print(int(output))
    output_sum += int(output)


print(count_1478)
print(output_sum)
