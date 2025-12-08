import pygame
import random
from constants import LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        sound1 = "assets/sounds/rescopicsound-plasma-ku-01.mp3"
        sound2 = "assets/sounds/rescopicsound-plasma-ku-02.mp3"
        sound3 = "assets/sounds/rescopicsound-plasma-ku-03.mp3"
        sound4 = "assets/sounds/rescopicsound-plasma-ku-04.mp3"
        sound5 = "assets/sounds/rescopicsound-plasma-ku-05.mp3"
        sound_list = (sound1,sound2, sound3, sound4, sound5)
        self.shot_sound = pygame.mixer.Sound(random.choice(sound_list))
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
