from utils.helper import *

def best_first_search(maze):
    start, goal = find_start_goal(maze)
    heap = [(heuristic(start, goal), start)]
    visited = set()
    came_from = {}

    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            return reconstruct_path(came_from, goal)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(heap, (heuristic(neighbor, goal), neighbor))
    return None
