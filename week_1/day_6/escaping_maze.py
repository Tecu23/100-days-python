map = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
end_position = (2, 2)
start_position = (0, 0)

x = start_position[0]
y = start_position[1]

while end_position[0] != x and y != end_position[1]:
    x += 1
    y += 1

print("Reached End of Maze")