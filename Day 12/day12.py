import re
file = open('./Day 12/input.txt')
input = [line.strip() for line in file]
# print(input)


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.is_small = re.match('^[a-z]+$', name)

    def connect(self, cave: 'Cave'):
        self.connections.append(cave)
        cave.connections.append(self)


start_cave = None
end_cave = None
caves = {}

for path in input:
    match = re.match('(.+)-(.+)', path)
    cave1 = match.group(1)
    cave2 = match.group(2)

    if cave1 not in caves.keys():
        caves[cave1] = Cave(cave1)
    if cave2 not in caves.keys():
        caves[cave2] = Cave(cave2)
    caves[cave1].connect(caves[cave2])

paths_1 = 0
paths_2 = 0


def traverse_1(cave: Cave, visited):
    path = visited[:]
    path.append(cave.name)
    if cave.name == 'end':
        # print(path)
        return 1
    if cave.is_small and cave.name in visited:
        return 0

    sum = 0
    for connected in cave.connections:
        sum += traverse_1(connected, path)
    return sum


def traverse_2(cave: Cave, visited, visited_twice):
    path = visited[:]
    path.append(cave.name)
    if cave.name == 'end':
        # print(path)
        return 1
    if cave.name == 'start' and visited:
        return 0
    if cave.is_small and cave.name in visited and visited_twice:
        return 0
    if cave.is_small and cave.name in visited:
        visited_twice = True

    sum = 0
    for connected in cave.connections:
        sum += traverse_2(connected, path, visited_twice)
    return sum


print(
    f"There are {traverse_1(caves['start'], [])} paths given the first set of rules")
print(
    f"There are {traverse_2(caves['start'], [], False)} paths given the second set of rules")
