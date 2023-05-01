from game.maze import Maze
from game.boards.boards import boards
from algorithms.BFS import BFS


if __name__ == '__main__':
    # game = Maze(board=boards[3], pathfinding_algorithm=BFS)
    # game = Maze(board_size=(40, 40), tick=10)
    game = Maze(board_size=(240, 135), pathfinding_algorithm=BFS)
    game.run_game()