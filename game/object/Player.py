import pygame as p
from game.object.Object import Object

from game.component.Collider import Collider
from game.component.Sprite import Sprite
from game.component.RigidBody import RigidBody
from game.component.Controller1 import Controller1
from game.component.Animator import Animator, Animation


class Player(Object):
    def __init__(self):
        super().__init__("Player")

        self.sprite = Sprite(self)
        self.sprite.load_image("assets/sprites/player.png", alpha=True)

        self.collider = Collider(self)
        self.collider.set_rect(p.Rect(0, 0, 32, 64), (15, 0))
        self.collider.add_collide_layer("TERRAIN")

        self.rigid_body = RigidBody(self)

        self.controller = Controller1(self)

        self.animator = Animator(self)
        self.animator.add_animation("IDLE RIGHT", "assets/animations/player1/idle")
        self.animator.play_animation("IDLE RIGHT")

        self.transform.set_position((150, 100))

        self.add_component(self.sprite)
        self.add_component(self.collider)
        self.add_component(self.rigid_body)
        self.add_component(self.controller)
        self.add_component(self.animator)
