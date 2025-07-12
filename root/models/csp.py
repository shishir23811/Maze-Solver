from utils.helper import *

def csp_maze(maze):
    start, goal = find_start_goal(maze)
    max_depth = 30 

    def backtrack(path, visited):
        if path[-1] == goal:
            return path
        if len(path) >= max_depth:
            return None
        for neighbor in get_neighbors(path[-1], maze):
            if neighbor not in visited:
                result = backtrack(path + [neighbor], visited | {neighbor})
                if result:
                    return result
        return None

    return backtrack([start], {start})


