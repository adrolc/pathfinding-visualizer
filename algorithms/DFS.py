from collections import deque
from .abstract_algorithm import AbstractAlgorithm


class Node:
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent


class DFS(AbstractAlgorithm):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.board = game.board
        self.start = Node(
            (self.game._player_initial_y, self.game._player_initial_x), None
        )
        self.stack = [self.start]
        self.visited = {self.start.pos}

    def _process_neighbor(self, current, y, x):
        field = self.board[y][x]
        if field == self.game.settings.ID_GOAL:
            self.found = True
        elif field == self.game.settings.ID_EMPTY and (y, x) not in self.visited:
            self.stack.append(Node((y, x), current))
            self.visited.add((y, x))

    def find(self, step_by_step=True, visualization_speed=1):
        if step_by_step:
            if self.found == False:
                self._find(visualization_speed)
        else:
            while not self.found:
                self._find(1)

    def _find(self, visualization_speed):
        for i in range(visualization_speed):
            if self.found:
                break
            current = self.stack.pop()
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

    def follow_found_path(self, step_by_step=True, visualization_speed=1):
        if not self.found:
            return

        if step_by_step:
            self._follow_found_path(visualization_speed)
        else:
            while True:
                self._follow_found_path(1)
                if not self.c.parent:
                    return

    def _follow_found_path(self, visualization_speed):
        for i in range(visualization_speed):
            if not self.found_path:
                self.c = self.visited_fields[-1]
                self.found_path.append(self.c)
            elif self.c.parent:
                self.c = self.c.parent
                self.found_path.append(self.c)
            else:
                break
