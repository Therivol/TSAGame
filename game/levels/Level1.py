import pygame as p

from game.levels.Level import Level
from game.object.Button1a import Button1a


class Level1(Level):
    def __init__(self):
        super().__init__()

        self.button1a = Button1a()

        self.player1.transform.set_position((75, 350))
        self.player2.transform.set_position((80, 350))
        self.button1a.transform.set_position((896, 384))

        self.add_object(self.button1a)

    def update(self):
        if not self.player1.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)):
            self.player1.transform.set_position((75, 350))
            self.player1.rigid_body.set_velocity((0, 0))

        if not self.player2.collider.get_rect().colliderect(p.Rect(0, 0, 960, 1144)):
            self.player2.transform.set_position((80, 350))
            self.player2.rigid_body.set_velocity((0, 0))
