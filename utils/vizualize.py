import matplotlib.pyplot as plt
import numpy as np

def visualize_maze_with_path(maze, path, subtitle):
    color_map = {
        '0': 0,  # Open path (black)
        '1': 1,  # Wall (green)
        'S': 2,  # Start
        'G': 3   # Goal
    }

    grid = np.zeros((len(maze), len(maze[0])))
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            grid[i][j] = color_map.get(cell, 0)

    # Custom colormap: 0=black, 1=green, 2=start, 3=goal
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['black', 'green', 'black', 'black'])  # custom base colors

    fig, ax = plt.subplots()
    ax.imshow(grid, cmap=cmap, origin='upper')

    # Draw thin grid lines
    ax.set_xticks(np.arange(-0.5, len(maze[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(maze), 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=0.5)

    # Draw path in red
    if path:
        y_coords, x_coords = zip(*path)
        ax.plot(x_coords, y_coords, color='red', linewidth=2, marker='o', markersize=5, label='Path')

    # Annotate start and goal
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                ax.text(j, i, 'S', ha='center', va='center', color='green', fontsize=12, fontweight='bold')
            elif cell == 'G':
                ax.text(j, i, 'G', ha='center', va='center', color='blue', fontsize=12, fontweight='bold')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.suptitle(subtitle, fontsize=14)
    plt.legend()
    plt.show()
