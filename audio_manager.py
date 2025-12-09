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
        self.music_playing = None
        self.music_queued = None

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
            self.music_playing = "start"
            self.music_queued = "battle1"
            pygame.mixer.music.load(self.music_files.get(self.music_playing))
            pygame.mixer.music.play()
            pygame.mixer.music.queue(self.music_files.get(self.music_queued))

    def get_next_song(self):
        self.music_queued = f"battle{random.randint(1,3)}"
        """ # hardcoded playlist
        if self.music_playing == "battle1":
            self.music_queued = "battle2"
        if self.music_playing == "battle2":
            self.music_queued = "battle3"
        if self.music_playing == "battle3":
            self.music_queued = "battle1" """
        

    def play_continuous(self):
        self.music_playing = self.music_queued
        self.get_next_song()
        pygame.mixer.music.queue(self.music_files.get(self.music_queued))

Audio = AudioManager()
