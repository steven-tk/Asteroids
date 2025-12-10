import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLLISION_DIST, ASTEROID_MIN_RADIUS, SAVE_ZONE_RADIUS, PLAYER_INVUL_TIMER
from audio_manager import Audio
from logger import log_state, log_event
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shrapnel import Shrapnel



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # ====================
    # Debug Controls & Settings
    # ====================
    logging_on = False
    entity_check = False
    music_off = False

    bounce_off = False
    volumetric_mass = False
    player_two = False
    god_mode = False

    TICK = 120 # make a flag for it later


    # ====================
    # Game Init
    # ====================
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    Clock = pygame.time.Clock()
    MUSIC_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(MUSIC_END)
    if music_off:
        pass
    else:
        Audio.start_music()

    p1_score = 0
    p2_score = 0
    p1_lives = 3
    p2_lives = 3
    frame_count = 0
    pause = False

    # ====================
    # Groups & Containers
    # ====================
    shrapnels = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    always_updatable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Shrapnel.containers = (shrapnels, updatable, drawable)
    AsteroidField.containers = (updatable)

    # ====================
    # Object Init
    # ====================
    Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Player2 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField1 = AsteroidField(volumetric_mass)
    SaveZone = CircleShape(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SAVE_ZONE_RADIUS)


    # ====================
    # Game Loop
    # ====================
    while True:
        #if logging_on:
        #    log_state()
        dt = Clock.tick(TICK) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Game over! You've scored {p1_score}")
                return
            if event.type == MUSIC_END:
                Audio.play_continuous()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

        if pause:
            always_updatable.update()
        else:
            screen.fill("black")
            updatable.update(dt)
            always_updatable.update()
            for thing in drawable:
                thing.draw(screen)
            pygame.display.flip()
            
            ast_list = list(asteroids)

            if god_mode:
                pass
            else:
                for ast in ast_list:
                    if ast.position.distance_squared_to(Player1.position) > COLLISION_DIST**2:
                        continue
                    if ast.collides_with(Player1):
                        if Player1.invul_check():
                            Player1.teleport_to(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        else:
                            Player1.invul_timer = PLAYER_INVUL_TIMER
                            p1_lives -= 1
                            if p1_lives < 0:
                                print(f"Game over! You've scored {p1_score}")
                                sys.exit()
                            print(f"Player 1 got hit. You've got {p1_lives} left.")
                            for ast in ast_list:
                                if ast.position.distance_squared_to(SaveZone.position) < COLLISION_DIST**2:
                                    ast.explode(1, 3)
                                    ast.kill()
                            Player1.teleport_to(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    

            if bounce_off:
                pass
            else:
                for i, ast in enumerate(ast_list):
                    for roid in ast_list[i+1:]:
                        if ast.position.distance_squared_to(roid.position) > COLLISION_DIST**2:
                            continue
                        if ast.collides_with(roid):
                            ast.bounce(roid)


            for pew in shots:
                for ast in ast_list:
                    if ast.position.distance_squared_to(pew.position) > COLLISION_DIST**2:
                        continue
                    if ast.collides_with(pew):
                        ast.split(volumetric_mass)
                        pew.kill()
                        if ast.radius > ASTEROID_MIN_RADIUS:
                            p1_score += 2
                        else:
                            p1_score += 1


        if entity_check:
            frame_count += 1
            if frame_count % 60 == 0:
                print("Asteroids:", len(asteroids), "Shots:", len(shots), "Shrapnels:", len(shrapnels))

        

    


if __name__ == "__main__":
    main()
