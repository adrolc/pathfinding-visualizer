import pygame
import sys
from typing import Callable, Dict
from .player import Player
from .wall import Wall
from .goal import Goal
from .settings import Settings
from .boards.board_generator import create_maze, DEFAULT_MAZE_SIZE
from .utils import draw_grid
from .visualization.visualization import Visualization


class Maze:
    def __init__(
        self,
        board=None,
        board_size: tuple[int, int] = None,
        pathfinding_algorithm: Callable = None,
        tick: int = 0,
    ):
        pygame.init()

        self.initialize_board(board, board_size)
        self.settings = Settings(self)
        self.setup_display()
        self.object_list = self.create_object_list()
        self.init_objects()
        self.tick = tick

        # PathFinding algorithm (must be initialized after objects)
        if pathfinding_algorithm:
            self.visualization = Visualization(self, pathfinding_algorithm(self))

    def initialize_board(self, board, board_size: tuple[int, int]):
        if board:
            self.board = board
        else:
            if not board_size:
                board_size = DEFAULT_MAZE_SIZE
            self.board = create_maze(board_size[0], board_size[1])
            self.board[1][0] = Settings.ID_PLAYER
            self.board[board_size[1] - 2][board_size[0] - 1] = Settings.ID_GOAL

    def setup_display(self):
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Maze game")
        self.clock = pygame.time.Clock()

    def create_object_list(self) -> Dict[int, Callable]:
        return {
            Settings.ID_WALL: self.init_walls,
            Settings.ID_PLAYER: self.init_player,
            Settings.ID_GOAL: self.init_goal,
        }

    def init_objects(self):
        self.walls = pygame.sprite.Group()
        for row in range(self.settings.fields_y):
            for col in range(self.settings.fields_x):
                self.init_object_at_position(col, row)

    def init_object_at_position(self, x: int, y: int):
        for object_id, init_func in self.object_list.items():
            if self.board[y][x] == object_id:
                init_func(x, y)

    def init_goal(self, x: int, y: int):
        self.goal = Goal(self, x, y)

    def init_player(self, x: int, y: int):
        self.player = Player(self, x, y)
        # Remember starting position for game reset function
        self._player_initial_x = x
        self._player_initial_y = y

    def init_walls(self, x: int, y: int):
        self.walls.add(Wall(self, x, y))

    def reset_game(self):
        self.init_player(self._player_initial_x, self._player_initial_y)

    def run_game(self):
        while True:
            self.handle_events()
            self.update_objects()
            self.check_win_condition()
            self.draw_screen()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_objects(self):
        self.player.update(self.walls)
        self.visualization.algorithm.find(step_by_step=True)
        self.visualization.algorithm.follow_found_path(step_by_step=True)

    def check_win_condition(self):
        if self.player.rect.colliderect(self.goal.rect):
            print("Congratulations! You made it to the finish line!")
            pygame.quit()
            sys.exit()

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        self.visualization.draw_visited_fields()
        self.visualization.draw_found_path()
        draw_grid(self.screen, self.settings)
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.draw(self.screen)
        self.screen.blit(self.goal.image, self.goal.rect)
        pygame.display.flip()
        self.clock.tick(self.tick)
