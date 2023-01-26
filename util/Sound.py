import pygame as p


class Sounds:

    @staticmethod
    def sound_ex(effect):
        mixed = p.mixer.Sound(effect)
        p.mixer.Sound.play(mixed)
