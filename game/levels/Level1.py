import pygame as p

from game.levels.Level import Level
from game.object.Buttons import Button1a, Button1b
from game.object.Crown import Crown
from util.Scenes import Scenes


class Level1(Level):
    def __init__(self):
        super().__init__()

        self.button1a = None
        self.button1b = None
        self.crown = None

    def awake(self):
        super().awake()

        self.button1a = Button1a()
        self.button1b = Button1b()
        self.crown = Crown()
        self.crown.set_players(self.player1, self.player2)

        self.button1a.transform.set_position((896, 384))
        self.button1b.transform.set_position((32, 160))

        self.reset()

        self.crown.set_position((576, 96))

        self.add_object(self.button1a)
        self.add_object(self.button1b)
        self.add_object(self.crown)

    def update(self):
        if self.crown.win:
            Scenes.set_scene("LEVEL SELECT")
            Scenes.get_scene("LEVEL SELECT").open_level(2)

        if not self.player1.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)) or \
                not self.player2.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)):
            self.reset()

    def reset(self):

        self.player1.transform.set_position((100, 350))
        self.player1.rigid_body.set_velocity((0, 0))

        self.player2.transform.set_position((148, 350))
        self.player2.rigid_body.set_velocity((0, 0))
