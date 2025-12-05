import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        #__points = self.triangle()
        #pygame.draw.polygon(screen, "white", __points, LINE_WIDTH)
        pass