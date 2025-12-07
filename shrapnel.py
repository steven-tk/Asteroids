import pygame
from constants import LINE_WIDTH, SHRAPNEL_LIFETIME
from rectangleshape import RectangleShape

class Shrapnel(RectangleShape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.lifetime = SHRAPNEL_LIFETIME
    
    def draw(self, screen):
        rect = (self.position[0], self.position[1], self.width, self.height)
        pygame.draw.rect(screen, "white", rect, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

        
# width=0 -> filled rectangle
# Rect(left, top, width, height)