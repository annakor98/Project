import pygame
from count import count

from game_object import GameObject
from count import count
from count import color


class Button(GameObject):
    def __init__(self, x, y, w, h, color, font):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.font = font
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
        text = self.font.render('Count', 1, (0, 0, 0))
        surface.blit(text, (self.x + 15, self.y + 27))

    def update(self, grid, surface):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.bounds.collidepoint(pos) and color(grid) == (255, 0, 0):
                count(grid, surface)