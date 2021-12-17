from dijkstar import Graph, find_path
file = open('./Day 15/input.txt')
input = [line.strip() for line in file]
# print(input)

graph = Graph()
width = len(input[0])
height = len(input)

for i, row in enumerate(input):
    for j, char in enumerate(row):
        if i != height - 1:
            # add in connection going down and up
            graph.add_edge((j, i), (j, i+1), int(input[i+1][j]))
            graph.add_edge((j, i+1), (j, i), int(input[i][j]))
        if j != width - 1:
            # add in connection to the right and left
            graph.add_edge((j, i), (j+1, i), int(input[i][j+1]))
            graph.add_edge((j+1, i), (j, i), int(input[i][j]))

print(find_path(graph, (0, 0), (height-1, width-1)).total_cost)

extended_input = []


def shift(row, shift):
    new_row = ''
    for char in row:
        new_row += str((int(char) + shift) % 9 or 9)
    return new_row


for j in range(5):
    for row in input:
        extended_input.append(shift(row, j))

for i, row in enumerate(extended_input):
    new_row = ''
    for j in range(5):
        new_row += shift(row, j)
    extended_input[i] = new_row

extended_graph = Graph()
extended_width = len(extended_input[0])
extended_height = len(extended_input)

for i, row in enumerate(extended_input):
    for j, char in enumerate(row):
        if i != extended_height - 1:
            # add in connection going down and up
            extended_graph.add_edge(
                (j, i), (j, i+1), int(extended_input[i+1][j]))
            extended_graph.add_edge(
                (j, i+1), (j, i), int(extended_input[i][j]))
        if j != extended_width - 1:
            # add in connection to the right and left
            extended_graph.add_edge(
                (j, i), (j+1, i), int(extended_input[i][j+1]))
            extended_graph.add_edge(
                (j+1, i), (j, i), int(extended_input[i][j]))
# print(extended_graph)
print(find_path(extended_graph, (0, 0),
      (extended_height-1, extended_width-1)).total_cost)
