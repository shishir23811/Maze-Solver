from collections import deque
import heapq

def find_start_goal(maze):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
            elif val == 'G':
                goal = (i, j)
    return start, goal

def get_neighbors(pos, maze):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dx, dy in directions:
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            if maze[x][y] != '1':
                neighbors.append((x, y))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def print_maze(maze, path = []):
    maze_copy = [row[:] for row in maze]  # deep copy

    for (x, y) in path:
        if maze_copy[x][y] not in ['S', 'G']:
            maze_copy[x][y] = '*'

    for row in maze_copy:
        print(' '.join(row))
    print()