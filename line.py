import pygame
import random

from game_object import GameObject
from input_box import InputBox


class Line(GameObject):
    def __init__(self, x, y, l, mode, orient, value, prev, col):
        self.orient = orient
        if self.orient == 'hor':
            GameObject.__init__(self, x, y, l, 20)
        elif self.orient == 'vert':
            GameObject.__init__(self, x, y, 20, l)
        self.mode = mode
        self.x = x
        self.y = y
        self.l = l
        self.value = value
        self.prev = prev
        self.col = col

    def draw(self, surface):
        if self.mode == 0:
            if self.orient == 'hor':
                pygame.draw.line(surface, (200, 200, 200), (self.x, self.y), (self.x + self.l, self.y))
            elif self.orient == 'vert':
                pygame.draw.line(surface, (200, 200, 200), (self.x, self.y), (self.x, self.y + self.l))

        if self.mode == 2:

            if self.orient == 'hor':
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y), (self.x + (self.l // 3), self.y))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (2 * self.l // 3), self.y), (self.x + self.l, self.y))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (self.l // 3), self.y - 10),
                                 (self.x + (2 * self.l // 3), self.y - 10))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (self.l // 3), self.y + 10),
                                 (self.x + (2 * self.l // 3), self.y + 10))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (self.l // 3), self.y - 10),
                                 (self.x + (self.l // 3), self.y + 10))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (2 * self.l // 3), self.y - 10),
                                 (self.x + (2 * self.l // 3), self.y + 10))

            elif self.orient == 'vert':
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y), (self.x, self.y + (self.l // 3)))
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y + (2 * self.l // 3)), (self.x, self.y + self.l))
                pygame.draw.line(surface, (0, 0, 0), (self.x - 10, self.y + (self.l // 3)),
                                 (self.x - 10, self.y + (2 * self.l // 3)))
                pygame.draw.line(surface, (0, 0, 0), (self.x + 10, self.y + (self.l // 3)),
                                 (self.x + 10, self.y + (2 * self.l // 3)))
                pygame.draw.line(surface, (0, 0, 0), (self.x - 10, self.y + (self.l // 3)),
                                 (self.x + 10, self.y + (self.l // 3)))
                pygame.draw.line(surface, (0, 0, 0), (self.x - 10, self.y + (2 * self.l // 3)),
                                 (self.x + 10, self.y + (2 * self.l // 3)))

        if self.mode == 4:

            if self.orient == 'hor':
                pygame.draw.line(surface, self.col, (self.x, self.y), (self.x + (self.l // 3), self.y))
                pygame.draw.line(surface, self.col, (self.x + (2 * self.l // 3), self.y), (self.x + self.l, self.y))
                pygame.draw.circle(surface, self.col, (self.x + (7 * self.l // 18), self.y), self.l // 16, 1)
                pygame.draw.circle(surface, self.col, (self.x + (9 * self.l // 18), self.y), self.l // 16, 1)
                pygame.draw.circle(surface, self.col, (self.x + (11 * self.l // 18), self.y), self.l // 16, 1)
                pygame.draw.polygon(surface, (255, 255, 255),
                                    [(self.x + (self.l // 3), self.y), (self.x + (2 * self.l // 3), self.y),
                                     (self.x + (2 * self.l // 3), self.y + 10), (self.x + (self.l // 3), self.y + 10),
                                     (self.x + (self.l // 3), self.y)], 0)

            elif self.orient == 'vert':
                pygame.draw.line(surface, self.col, (self.x, self.y), (self.x, self.y + (self.l // 3)))
                pygame.draw.line(surface, self.col, (self.x, self.y + (2 * self.l // 3)), (self.x, self.y + self.l))
                pygame.draw.circle(surface, self.col, (self.x, self.y + (7 * self.l // 18)), self.l // 16, 1)
                pygame.draw.circle(surface, self.col, (self.x, self.y + (9 * self.l // 18)), self.l // 16, 1)
                pygame.draw.circle(surface, self.col, (self.x, self.y + (11 * self.l // 18)), self.l // 16, 1)
                pygame.draw.polygon(surface, (255, 255, 255),
                                    [(self.x, self.y + (self.l // 3)), (self.x, self.y + (2 * self.l // 3)),
                                     (self.x + 10, self.y + (2 * self.l // 3)), (self.x + 10, self.y + (self.l // 3)),
                                     (self.x, self.y + (self.l // 3))], 0)

        if self.mode == 3:

            if self.orient == 'hor':
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y), (self.x + (2 * self.l // 5), self.y))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (3 * self.l // 5), self.y), (self.x + self.l, self.y))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (2 * self.l // 5), self.y - 10),
                                 (self.x + (2 * self.l // 5), self.y + 10))
                pygame.draw.line(surface, (0, 0, 0), (self.x + (3 * self.l // 5), self.y - 10),
                                 (self.x + (3 * self.l // 5), self.y + 10))

            elif self.orient == 'vert':
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y), (self.x, self.y + (2 * self.l // 5)))
                pygame.draw.line(surface, (0, 0, 0), (self.x, self.y + (3 * self.l // 5)), (self.x, self.y + self.l))
                pygame.draw.line(surface, (0, 0, 0), (self.x - 10, self.y + (2 * self.l // 5)),
                                 (self.x + 10, self.y + (2 * self.l // 5)))
                pygame.draw.line(surface, (0, 0, 0), (self.x - 10, self.y + (3 * self.l // 5)),
                                 (self.x + 10, self.y + (3 * self.l // 5)))

    def update(self, surface):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.bounds.collidepoint(pos):
                self.mode = (self.mode + 1) % 5
                if self.mode == 1:
                    self.mode += 1
                self.value = 1
                self.prev = 0
                self.color = (0, 0, 0)
                if self.mode == 3:
                    self.prev = 1
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            if self.bounds.collidepoint(pos) and self.mode > 1:
                if self.mode == 2:
                    txtbx = InputBox(self.x + 30, self.y + 30, pygame.font.SysFont("Arial", 20), 6, str(self.value),
                                     'Resistance', 'mOm')
                if self.mode == 4:
                    txtbx = InputBox(self.x + 30, self.y + 30, pygame.font.SysFont("Arial", 20), 6, str(self.value),
                                     'Inductance', 'H')
                if self.mode == 3:
                    txtbx = InputBox(self.x + 30, self.y + 30, pygame.font.SysFont("Arial", 20), 6, str(self.value),
                                     'Capacity', 'F')
                while 1:
                    events = pygame.event.get()

                    pygame.draw.rect(surface, (255, 255, 255), (self.x + 30, self.y + 30, 300, 50), 0)
                    pygame.draw.rect(surface, (0, 0, 0), (self.x + 30, self.y + 30, 300, 50), 2)
                    ans = txtbx.update(events)
                    if ans is not None:
                        self.value = int(ans)
                        break
                    txtbx.draw(surface)
                    pygame.display.flip()
