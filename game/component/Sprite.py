import pygame as p
from game.component.Component import Component
from game.component.Transform import Transform

from util.Assets import Assets


class Sprite(Component):
    def __init__(self, owner):
        super().__init__(owner)
        self.image = p.Surface((0, 0))
        self.draw_layer = "DEFAULT"
        self.flip = False

    def load_image(self, path, alpha=False):
        self.image = Assets.get_image(path, alpha)

    def set_surface(self, surf):
        self.image = surf

    def flip_sprite(self, flip):
        self.flip = flip

    def draw(self, surf):
        if self.flip:
            surf.blit(p.transform.flip(self.image, True, False), self.owner.transform.get_position_xy())
        else:
            surf.blit(self.image, self.owner.transform.get_position_xy())
