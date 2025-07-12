import random

def generate_maze(rows, cols, wall_prob=0.3):
    # Initialize maze with open paths
    maze = [['0' for _ in range(cols)] for _ in range(rows)]

    # Randomly add walls
    for i in range(rows):
        for j in range(cols):
            if random.random() < wall_prob:
                maze[i][j] = '1'

    # Carve a guaranteed path from top-left to bottom-right
    x, y = 0, 0
    while (x, y) != (rows - 1, cols - 1):
        maze[x][y] = '0'  # clear the cell in the path
        if x < rows - 1 and (y == cols - 1 or random.choice([True, False])):
            x += 1
        elif y < cols - 1:
            y += 1
    maze[x][y] = '0'  # clear the goal cell

    # Set start and goal
    maze[0][0] = 'S'
    maze[rows - 1][cols - 1] = 'G'

    return maze
