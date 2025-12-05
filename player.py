import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape

# Player Class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        __points = []
        __points = self.triangle()
        pygame.draw.polygon(screen, "white", __points, LINE_WIDTH) 
        
        

    def update(self, dt):
        # needs doing
        pass

