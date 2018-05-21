import pygame


class InputBox:
    def __init__(self, x, y, font_name, maxlength, value, name, unit):

        self.x = x
        self.y = y
        self.font_name = font_name
        self.maxlength = maxlength
        self.value = value
        self.name = name
        self.unit = unit

    def draw(self, surface):
        text = self.font_name.render(self.name + ': ' + self.value + ' ' + self.unit, 1, (0, 0, 0))
        surface.blit(text, (self.x, self.y))

    def update(self, events):

        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_0:
                    self.value += '0'
                elif event.key == pygame.K_1:
                    self.value += '1'
                elif event.key == pygame.K_2:
                    self.value += '2'
                elif event.key == pygame.K_3:
                    self.value += '3'
                elif event.key == pygame.K_4:
                    self.value += '4'
                elif event.key == pygame.K_5:
                    self.value += '5'
                elif event.key == pygame.K_6:
                    self.value += '6'
                elif event.key == pygame.K_7:
                    self.value += '7'
                elif event.key == pygame.K_8:
                    self.value += '8'
                elif event.key == pygame.K_9:
                    self.value += '9'
                elif event.key == pygame.K_BACKSPACE:
                    self.value = self.value[:-1]
                elif event.key == pygame.K_RETURN:
                    return self.value

        if len(self.value) > self.maxlength >= 0:
            self.value = self.value[:-1]
