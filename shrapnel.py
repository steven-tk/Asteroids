import pygame
from constants import LINE_WIDTH, SHRAPNEL_LENGTH, SHRAPNEL_WIDTH
from rectangleshape import RectangleShape

class Shot(RectangleShape):
    def __init__(self, x, y, SHRAPNEL_LENGTH,SHRAPNEL_WIDTH):
        super().__init__(x, y, SHRAPNEL_LENGTH,SHRAPNEL_WIDTH)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
