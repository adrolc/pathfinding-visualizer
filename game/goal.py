import pygame
from pygame.surface import Surface

class Goal(pygame.sprite.Sprite):
    def __init__(self, game, x: int, y: int):
        super().__init__()
        self.settings = game.settings
        self.image = self.create_image()
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def create_image(self) -> Surface:
        image = pygame.Surface((self.settings.field_size, self.settings.field_size))
        image.fill((255, 0, 0))
        return image

    def set_position(self, x: int, y: int):
        self.rect.x = x * self.settings.field_size
        self.rect.y = y * self.settings.field_size
