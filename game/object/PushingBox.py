import pygame as p

from game.object.Object import Object
from game.component.Collider import Collider
from game.component.Sprite import Sprite
from game.component.RigidBody import RigidBody

from util.Assets import Assets


class PushingBox(Object):
    def __init__(self):
        super().__init__(self)

        self.sprite = Sprite(self)
        self.sprite.set_surface(p.image.scale(Assets.get_image("assets/sprites/box.png"), (32, 32)))

        self.collider = Collider(self)
        self.collider.set_layer("TERRAIN")
        self.collider.set_rect(p.Rect(0, 0, 32, 32), (0, 0))

        self.rigid_body = RigidBody(self)

        self.add_component(self.sprite)
        self.add_component(self.collider)
        self.add_component(self.rigid_body)
