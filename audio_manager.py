import pygame
import random

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "blaster1": pygame.mixer.Sound("audio/sounds/rescopicsound-plasma-ku-01.mp3"),
            "blaster2": pygame.mixer.Sound("audio/sounds/rescopicsound-plasma-ku-02.mp3"),
            "blaster3": pygame.mixer.Sound("audio/sounds/rescopicsound-plasma-ku-03.mp3"),
            "blaster4": pygame.mixer.Sound("audio/sounds/rescopicsound-plasma-ku-04.mp3"),
            "blaster5": pygame.mixer.Sound("audio/sounds/rescopicsound-plasma-ku-05.mp3"),
            "asteroid_hit1": pygame.mixer.Sound("audio/sounds/rescopicsound-hit-ping-01.mp3")
        }
        self.music_files = {
            "start": "audio/music/juhani-junkala-start.wav",
            "battle1": "audio/music/juhani-junkala-level1.wav",
            "battle2": "audio/music/juhani-junkala-level2.wav",
            "battle3": "audio/music/juhani-junkala-level3.wav",
            "menu": "audio/music/juhani-junkala-ending.wav"
        }

    def play_sound(self, name, random_range=1):
        sound_id = f"{name}{random.randint(1,random_range)}"
        sound = self.sounds.get(sound_id)

        if sound:
            sound.play()
        else:
            print(f"Sound '{sound_id}' not found.")


    def start_music(self):
        if pygame.mixer.music.get_busy():
            pass
        else:
            first_track = self.music_files.get("start")
            pygame.mixer.music.load(first_track)
            pygame.mixer.music.play()


    def queue_music(self, name):
        next_song = None

        #logic based on name

        pygame.mixer.music.queue()
        return next_song


    def play_music(self, name, loop=True):
        pass
    
    
            # logic for checking current song, queueing next using queue_music and running through list of songs (battle1-3)
            # check if i should use pygame.mixer.music.unload


Audio = AudioManager()
