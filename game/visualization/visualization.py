import pygame


class Visualization:
    def __init__(self, game, algorithm):
        self.game = game
        self.algorithm = algorithm

    def draw_visited_fields(self):
        for node in self.algorithm.visited_fields:
            x, y = node.pos
            pygame.draw.rect(
                self.game.screen,
                (255, 159, 67),
                (
                    y * self.game.settings.field_size,
                    x * self.game.settings.field_size,
                    self.game.settings.field_size,
                    self.game.settings.field_size,
                ),
            )

    def draw_found_path(self):
        for node in self.algorithm.found_path:
            x, y = node.pos
            pygame.draw.rect(
                self.game.screen,
                (46, 134, 222),
                (
                    y * self.game.settings.field_size,
                    x * self.game.settings.field_size,
                    self.game.settings.field_size,
                    self.game.settings.field_size,
                ),
            )
