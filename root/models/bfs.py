from utils.helper import *

def bfs(maze):
    start, goal = find_start_goal(maze)
    queue = deque([start])
    visited = set([start])  
    came_from = {}

    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(came_from, goal)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)  
                came_from[neighbor] = current
                queue.append(neighbor)
    return None

