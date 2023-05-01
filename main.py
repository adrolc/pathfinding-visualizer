from game.maze import Maze
from game.boards.boards import boards
from algorithms.BFS import BFS


if __name__ == '__main__':
    # game = Maze(board_size=(40, 30), pathfinding_algorithm=BFS)
    # game = Maze(board=boards[3], pathfinding_algorithm=BFS)
    game = Maze(board_size=(50, 50), pathfinding_algorithm=BFS, tick=0)
    # game = Maze(board_size=(384, 216), pathfinding_algorithm=BFS)
    game.run_game()

    # bfs = BFS(game)
    # bfs.find()
    