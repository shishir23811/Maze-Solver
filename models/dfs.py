from utils.helper import * 
def dfs(maze):
    start, goal = find_start_goal(maze)
    stack = [start]
    visited = set()
    came_from = {}

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return reconstruct_path(came_from, goal)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                came_from[neighbor] = current
                stack.append(neighbor)
    return None
