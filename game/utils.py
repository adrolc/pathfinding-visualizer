import pygame


def draw_grid(screen, settings):
    for x in range(0, settings.screen_width, settings.field_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, settings.screen_height))
    for y in range(0, settings.screen_height, settings.field_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (settings.screen_width, y))
