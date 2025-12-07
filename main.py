import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shrapnel import Shrapnel






def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # ====================
    # Control Booleans
    # ====================
    bounce_on = True
    # ====================

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    Clock = pygame.time.Clock()

    p1_score = 0
    p2_score = 0

    shrapnels = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    AsteroidField1 = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Shrapnel.containers = (shrapnels, updatable, drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        for ast in asteroids:
            if ast.collides_with(Player1):
                log_event("player_hit")
                print(f"Game over! You've scored {p1_score}")
                sys.exit()

        if bounce_on == True:    
            for i, ast in enumerate(asteroids):
                for j, roid in enumerate(asteroids):
                    if j <= i:
                        continue  # skip self and already-handled pairs
                    if ast.collides_with(roid):
                        log_event("asteroid_collision")
                        ast.bounce(roid)



        for ast in asteroids:
            for pew in shots:
                if ast.collides_with(pew):
                    log_event("asteroid_shot")
                    ast.split()
                    pew.kill()
                    p1_score += 1

        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
