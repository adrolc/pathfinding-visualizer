from collections import deque
from .abstract_algorithm import AbstractAlgorithm


class Node:
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent


class BFS(AbstractAlgorithm):
    def __init__(self, game):
        self.game = game
        self.board = game.board
        self.start = Node(
            (self.game._player_initial_y, self.game._player_initial_x), None
        )
        self.queue = deque([self.start])
        self.visited = {self.start.pos}
        self.found = False

        self.visited_fields = []
        self.found_path = []

    def _process_neighbor(self, current, y, x):
        field = self.board[y][x]
        if field == self.game.settings.ID_GOAL:
            self.found = True
        elif field == self.game.settings.ID_EMPTY and (y, x) not in self.visited:
            self.queue.append(Node((y, x), current))
            self.visited.add((y, x))

    def find(self, step_by_step=True):
        if step_by_step:
            if self.found == False:
                self._find()
        else:
            while not self.found:
                self._find()

    def _find(self):
        current = self.queue.popleft()
        self.visited_fields.append(current)
        y, x = current.pos

        # up
        if y > 0:
            self._process_neighbor(current, y - 1, x)

        # down
        if y < self.game.settings.fields_y - 1:
            self._process_neighbor(current, y + 1, x)

        # right
        if x < self.game.settings.fields_x - 1:
            self._process_neighbor(current, y, x + 1)

        # left
        if x > 0:
            self._process_neighbor(current, y, x - 1)

    def follow_found_path(self, step_by_step=True):
        if not self.found:
            return

        if step_by_step:
            self._follow_found_path()
        else:
            while True:
                self._follow_found_path()
                if not self.c.parent:
                    return

    def _follow_found_path(self):
        if not self.found_path:
            self.c = self.visited_fields[-1]
            self.found_path.append(self.c)
        elif self.c.parent:
            self.c = self.c.parent
            self.found_path.append(self.c)