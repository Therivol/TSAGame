import pygame as p

from game.levels.Level import Level
from game.object.Buttons import Button3a, Button3b, Switch3a, Switch3b
from game.object.Crown import Crown
from util.Scenes import Scenes
from game.scene.EndScreen import EndScreen


class Level3(Level):
    def __init__(self):
        super().__init__()

        self.button3a = None
        self.button3b = None
        self.switch3a = None
        self.switch3b = None
        self.crown = None

    def awake(self):
        super().awake()

        self.button3a = Button3a()
        self.button3b = Button3b()
        self.switch3a = Switch3a()
        self.switch3b = Switch3b()
        self.crown = Crown()
        self.crown.set_players(self.player1, self.player2)

        self.reset()

        self.button3a.transform.set_position((32, 384))
        self.button3b.transform.set_position((32, 128))
        self.switch3a.transform.set_position((352, 320))
        self.switch3b.transform.set_position((896, 320))
        self.crown.set_position((800, 128))

        self.add_object(self.button3a)
        self.add_object(self.button3b)
        self.add_object(self.crown)
        self.add_object(self.switch3a)
        self.add_object(self.switch3b)

    def update(self):
        if self.crown.win:
            Scenes.add_scene(EndScreen())
            Scenes.set_scene("END SCREEN")

        if not self.player1.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)) or \
                not self.player2.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)):
            self.reset()

    def reset(self):
        self.player1.transform.set_position((100, 320))
        self.player1.rigid_body.set_velocity((0, 0))

        self.player2.transform.set_position((148, 416))
        self.player2.rigid_body.set_velocity((0, 0))
