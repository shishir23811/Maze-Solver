from utils.helper import print_maze
from utils.vizualize import visualize_maze_with_path
from utils.maze_generator import generate_maze
from models.dfs import dfs
from models.bfs import bfs
from models.best_first import best_first_search
from models.a_star import a_star
from models.csp import csp_maze
from time import time

# path = dfs(maze)
# print("Visualizing DFS")
# visualize_maze_with_path(maze, path, "Depth First Search")

# path = bfs(maze)
# print("Visualizing BFS")
# visualize_maze_with_path(maze, path, "Bredth First Search")

# path = best_first_search(maze)
# print("Visualizing Best-First Search")
# visualize_maze_with_path(maze, path, "Best First Search")

# path = a_star(maze)
# print("Visualizing A* Search")
# visualize_maze_with_path(maze, path, "A* Search")

# path = csp_maze(maze)
# if path:
#     print("Visualizing CSP")
#     visualize_maze_with_path(maze, path, "Constraint Satisfaction Problem")

#---------------------------------------------------------------------------------------------------------------------------------

def execute(row, col):
    print("Maze Size: ", row, "x", col)
    print()
    maze = generate_maze(row, col)  # Generate a maze with 20 rows and 20 columns and a density of 0.3
    print("Generated Maze:")
    print_maze(maze)

    path_lengths, execution_times = [], []

    start = time()
    path  = dfs(maze)
    end   = time()
    print("Depth First Search:")
    print_maze(maze, path)
    print("path found: ", path)
    print("Length of path: ", len(path))
    print("Time taken: ", end-start)
    print()
    path_lengths.append(len(path))
    execution_times.append(end-start)

    start = time()
    path = bfs(maze)
    end = time()
    print("Breadth First Search:")
    print_maze(maze, path)
    print("path found: ", path)
    print("Length of path: ", len(path))
    print("Time taken: ", end-start)
    print()
    path_lengths.append(len(path))
    execution_times.append(end-start)

    start = time()
    path = best_first_search(maze)
    end = time()
    print("Best-First Search:")
    print_maze(maze, path)
    print("path found: ", path)
    print("length of path: ", len(path))
    print("Time taken: ", end-start)
    print() 
    path_lengths.append(len(path))
    execution_times.append(end-start)

    start = time()
    path = a_star(maze)
    end = time()
    print("A* Search:")
    print_maze(maze, path)
    print("path found:", path)
    print("Length of path: ", len(path))
    print("Time taken: ", end-start)
    print()
    path_lengths.append(len(path))
    execution_times.append(end-start)

    # start = time()
    # path = csp_maze(maze)
    # end = time()
    # if path:
    #     print("Constraint Satisfaction Problem")
    #     print_maze(maze, path)
    #     print("path found:", path)
    #     print("Length of path: ", len(path))
    #     print("Time taken: ", end-start)
    #     print()
    #     path_lengths.append(len(path))
    #     execution_times.append(end-start)

    return path_lengths, execution_times







