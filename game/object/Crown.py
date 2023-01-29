from game.object.Object import Object
from game.component.Sprite import Sprite
import pygame as p
from game.component.Collider import Collider

from util.Assets import Assets


class Crown(Object):
    def __init__(self):
        super().__init__("Crown")

        self.win = False

        self.player1 = None
        self.player2 = None

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/crown.png", alpha=True))

        self.rect = p.Rect(self.transform.get_position_xy(), (32, 32))

        self.add_component(self.sprite)

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def set_position(self, pos):
        self.transform.set_position(pos)
        self.rect.topleft = pos

    def update(self):
        super(Crown, self).update()

        if self.player1.get_component(Collider).get_rect().colliderect(self.rect) and \
                self.player2.get_component(Collider).get_rect().colliderect(self.rect):
            self.win = True
