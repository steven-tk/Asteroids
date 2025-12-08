import pygame
import random
import math
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SHRAPNEL_WIDTH, SHRAPNEL_HEIGHT
from audio_manager import Audio
from circleshape import CircleShape
from shrapnel import Shrapnel
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.density = random.uniform(0.8, 1.2)
        # Planar mass vs volumetric mass:
        #self.mass = self.density * (4/3) * math.pi * self.radius **3
        self.mass = math.pi * self.radius ** 2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def explode(self, min_size, max_size):
        num_shrapnel = random.randint(5,12)
        split_angle = 360 / num_shrapnel

        Audio.play_sound("asteroid_hit")
        for i in range(num_shrapnel):
            shrap_bolt = Shrapnel(self.position[0], self.position[1], SHRAPNEL_WIDTH, SHRAPNEL_HEIGHT)
            shrap_bolt.velocity = self.velocity.rotate(split_angle * i) * random.uniform(min_size, max_size)
    
    def overlap(self, other):
        delta = other.position - self.position
        dist = delta.length()
        overlap = self.radius + other.radius - dist

        if overlap > 0 and dist > 0:
            normal = delta / dist

            self.position -= normal * (overlap / 2)
            other.position += normal * (overlap / 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.explode(0.2, 1.5)
            return
        else:
            self.explode(1, 3)
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            speed_up = 1.2

            new1 = Asteroid(self.position[0], self.position[1], new_radius)
            new1.velocity = self.velocity.rotate(random_angle) * speed_up
            new2 = Asteroid(self.position[0], self.position[1], new_radius)
            new2.velocity = self.velocity.rotate(-random_angle) * speed_up

    def bounce(self, other, restitution=1.0):
        # project velocities onto normal and tangent
        normal = other.position - self.position
        if normal.length_squared() == 0:
            return

        normal = normal.normalize()
        tangent = pygame.Vector2(-normal.y, normal.x)
       
        v1n = self.velocity.dot(normal)
        v1t = self.velocity.dot(tangent)
        v2n = other.velocity.dot(normal)
        v2t = other.velocity.dot(tangent)

        # 1D elastic collision for normal components with restitution applied
        # Restitution reminder: (1.0 = perfectly elastic, <1 = some energy loss)
        m1 = self.mass
        m2 = other.mass
        new_v1n = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2) * restitution
        new_v2n = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2) * restitution

        # recombine scalar components into vectors
        self.velocity = tangent * v1t + normal * new_v1n
        other.velocity = tangent * v2t + normal * new_v2n

        # positional separation to resolve overlap
        overlap = (self.radius + other.radius) - (self.position.distance_to(other.position))
        if overlap > 0:
            # push each away proportional to their mass (so heavier moves less)
            total = m1 + m2
            if total > 0:
                self.position += -normal * (overlap * (m2 / total))
                other.position += normal * (overlap * (m1 / total))

       

        # old version:
        # self.overlap(other)
        # self.velocity -= 2 * self.velocity.dot(normal) * normal
        # other.velocity -= 2 * other.velocity.dot(-normal) * -normal
        






