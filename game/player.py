import pygame
from pygame.surface import Surface
from pygame.sprite import Group
from pygame.rect import Rect


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x: int, y: int):
        super().__init__()
        self.settings = game.settings
        self.image = self.create_image()
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def create_image(self) -> Surface:
        image = pygame.Surface((self.settings.field_size, self.settings.field_size))
        image.fill((0, 255, 0))
        return image

    def update(self, walls: Group):
        keys = pygame.key.get_pressed()
        dx, dy = self.get_move_direction(keys)

        if not self.is_collision(dx, dy, walls):
            self.move(dx, dy)

    def set_position(self, x: int, y: int):
        self.rect.x = x * self.settings.field_size
        self.rect.y = y * self.settings.field_size

    def get_move_direction(self, keys: tuple[int, ...]) -> tuple[int, int]:
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.settings.field_size
        if keys[pygame.K_RIGHT]:
            dx = self.settings.field_size
        if keys[pygame.K_UP]:
            dy = -self.settings.field_size
        if keys[pygame.K_DOWN]:
            dy = self.settings.field_size
        return dx, dy

    def move(self, dx: int, dy: int):
        self.rect.x += dx
        self.rect.y += dy

    def is_collision(self, dx: int, dy: int, walls: Group) -> bool:
        future_rect = self.rect.move(dx, dy)
        return self.is_out_of_bounds(future_rect) or self.is_colliding_with_walls(future_rect, walls)

    def is_out_of_bounds(self, rect: Rect) -> bool:
        return (
            rect.left < 0
            or rect.right > self.settings.screen_width
            or rect.top < 0
            or rect.bottom > self.settings.screen_height
        )

    def is_colliding_with_walls(self, rect: Rect, walls: Group) -> bool:
        for wall in walls:
            if wall.rect.colliderect(rect):
                return True
        return False
