import pygame as p


class Audio:
    current_track = None

    @staticmethod
    def play_sound(effect):
        mixed = p.mixer.Sound(effect)
        p.mixer.Sound.play(mixed)

    @staticmethod
    def play_track(file):
        Audio.current_track = file
        p.mixer.music.load(file)
        p.mixer.music.play(loops=100, start=0.0, fade_ms=0)

    @staticmethod
    def stop_track():
        if Audio.current_track:
            p.mixer.music.unload()
