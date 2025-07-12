from utils.helper import *

def a_star(maze):
    start, goal = find_start_goal(maze)
    heap = [(0 + heuristic(start, goal), 0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while heap:
        _, cost, current = heapq.heappop(heap)
        if current == goal:
            return reconstruct_path(came_from, goal)
        for neighbor in get_neighbors(current, maze):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(heap, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None
