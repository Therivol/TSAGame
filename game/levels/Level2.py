import pygame as p

from game.levels.Level import Level
from game.object.Buttons import Button2a, Button2b, Switch2a
from game.object.Crown import Crown
from util.Scenes import Scenes


class Level2(Level):
    def __init__(self):
        super().__init__()

        self.button2a = None
        self.button2b = None
        self.switch2a = None
        self.crown = None

    def awake(self):
        super().awake()

        self.button2a = Button2a()
        self.button2b = Button2b()
        self.switch2a = Switch2a()
        self.crown = Crown()
        self.crown.set_players(self.player1, self.player2)

        self.reset()

        self.button2a.transform.set_position((800, 96))
        self.button2b.transform.set_position((736, 96))
        self.switch2a.transform.set_position((896, 416))
        self.crown.set_position((32, 384))

        self.add_object(self.button2a)
        self.add_object(self.button2b)
        self.add_object(self.switch2a)
        self.add_object(self.crown)

    def update(self):
        if self.crown.win:
            Scenes.set_scene("LEVEL SELECT")
            Scenes.get_scene("LEVEL SELECT").open_level(3)

        if not self.player1.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)) or \
                not self.player2.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)):
            self.reset()

    def reset(self):

        self.player1.transform.set_position((64, 32))
        self.player1.rigid_body.set_velocity((0, 0))

        self.player2.transform.set_position((832, 32))
        self.player2.rigid_body.set_velocity((0, 0))
