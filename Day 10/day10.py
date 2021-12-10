file = open('./Day 10/input.txt', 'r')
input = [line.strip() for line in file]

braces = {'(': ')', '[': ']', '{': '}', '<': '>'}
syntax_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_points = {')': 1, ']': 2, '}': 3, '>': 4}

syntax_score = 0
autocomplete_scores = []

for line in input:
    stack = []
    autocomplete_score = 0
    is_corrupted = False
    for character in line:
        if character in braces.keys():
            stack.append(character)
            continue
        else:
            last = stack.pop()
            if character != braces[last]:
                print(
                    f'Expected {braces[last]}, but found {character} instead.')
                syntax_score += syntax_points[character]
                is_corrupted = True
                break
    if is_corrupted:
        continue

    # If nothing wrong was encountered, the stack must still exist and the line is incomplete
    while stack:
        last = stack.pop()
        autocomplete_score *= 5
        autocomplete_score += autocomplete_points[braces[last]]
    autocomplete_scores.append(autocomplete_score)

print(syntax_score)
print(sorted(autocomplete_scores)[int(len(autocomplete_scores)/2-0.5)])
