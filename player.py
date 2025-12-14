import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_LIVES, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, SCREEN_WIDTH, SCREEN_HEIGHT
from audio_manager import Audio
from circleshape import CircleShape
from shot import Shot

# Player Class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.invul_timer = 0
        self.out_of_bounds = False
        self.lives = PLAYER_LIVES
        self.score = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        __points = self.triangle()
        pygame.draw.polygon(screen, "white", __points, LINE_WIDTH) 
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_e]:
            self.strafe(dt)
        if keys[pygame.K_q]:
            self.strafe(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown -= dt
        self.invul_timer -= dt
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def strafe(self, dt):
        pass

    def shoot(self):
        if self.cooldown >0:
            pass
        else:
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            location = self.position + pygame.Vector2(0,PLAYER_RADIUS).rotate(self.rotation)
            bullet = Shot(location[0], location[1], SHOT_RADIUS)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            Audio.play_sound("blaster", 5)

    def invul_check(self):
        if self.invul_timer > 0:
            return True
        else:
            return False

    def teleport_to(self, x=(None), y=None):
        if x is None:
            x = SCREEN_WIDTH / 2
        if y is None:
            y = SCREEN_HEIGHT / 2
        self.position = pygame.Vector2(x, y)

    def check_bounds(self):
        if (
            0 > self.position.x
            or self.position.x > SCREEN_WIDTH
            or 0 > self.position.y
            or self.position.y > SCREEN_HEIGHT
        ):
            self.out_of_bounds = True
