import pygame
import sys
from line import Line
from button import Button
from count import color

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Circuits')
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
grid = []
for i in range(100, 600, 100):
    for j in range(100, 700, 100):
        grid.append(Line(j, i, 100, 0, 'hor', 1, 0, (0, 0, 0)))

for i in range(100, 500, 100):
    for j in range(100, 800, 100):
        grid.append(Line(j, i, 100, 0, 'vert', 1, 0, (0, 0, 0)))

while 1:
    clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    for a in grid:
        a.update(screen)
        a.draw(screen)
    button = Button(710, 510, 80, 80, color(grid), pygame.font.SysFont("Arial", 20))
    button.update(grid, screen)
    button.draw(screen)
    pygame.display.flip()