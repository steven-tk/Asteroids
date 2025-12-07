import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SHRAPNEL_WIDTH, SHRAPNEL_HEIGHT
from circleshape import CircleShape
from shrapnel import Shrapnel
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self, min_size, max_size):
        num_shrapnel = random.randint(5,12)
        split_angle = 360 / num_shrapnel
        log_event("asteroid_explode")

        for i in range(num_shrapnel):
            shrap_bolt = Shrapnel(self.position[0], self.position[1], SHRAPNEL_WIDTH, SHRAPNEL_HEIGHT)
            shrap_bolt.velocity = self.velocity.rotate(split_angle * i) * random.uniform(min_size, max_size)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.explode(0.2, 1.5)
            return
        else:
            log_event("asteroid_split")
            self.explode(1, 3)
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            speed_up = 1.2

            new1 = Asteroid(self.position[0], self.position[1], new_radius)
            new1.velocity = self.velocity.rotate(random_angle) * speed_up
            new2 = Asteroid(self.position[0], self.position[1], new_radius)
            new2.velocity = self.velocity.rotate(-random_angle)
    