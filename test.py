from main import execute
from utils.graph import graph

algorithms = ['DFS', 'BFS', 'BestFS', 'A*']

path_lengths, execution_times = execute(5,5)
graph(algorithms, path_lengths, execution_times, "5x5 Maze")

path_lengths, execution_times = execute(25,25)
graph(algorithms, path_lengths, execution_times, "25x25 Maze")

path_lengths, execution_times = execute(100,10)
graph(algorithms, path_lengths, execution_times, "100x10 Maze")

path_lengths, execution_times = execute(10,100)
graph(algorithms, path_lengths, execution_times, "10x100 Maze")

path_lengths, execution_times = execute(100,100)
graph(algorithms, path_lengths, execution_times, "100x100 Maze")









