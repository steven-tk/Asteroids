import pygame

# Base class for game objects
class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, length, width):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.length = length
        self.width = width

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    def collides_with(self, other):
        r1 = self.length
        r2 = other.radius

        if self.position.distance_to(other.position) <= r1 + r2:
            return True
        else:
            return False



    # self.position()
    # returns vector

    # distance_to()
    # calcs distance to vector, returns float