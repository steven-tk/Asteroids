import pygame

# Base class for game objects
class RectangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.width = width
        self.height = height
        self.position = pygame.Vector2(x - self.width/2, y - self.height/2)
        self.velocity = pygame.Vector2(0, 0)
       

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    def collides_with(self, other):
        # TODO quick hack emulating circles, fix after implementing proper hit-boxes
        r1 = self.height
        r2 = other.radius

        if self.position.distance_to(other.position) <= r1 + r2:
            return True
        else:
            return False



    # self.position()
    # returns vector

    # distance_to()
    # calcs distance to vector, returns float