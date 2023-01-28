import pygame as p
from game.object.Object import Object

from game.component.Collider import Collider
from game.component.Sprite import Sprite
from game.component.RigidBody import RigidBody
from game.component.Controller import Controller
from game.component.Animator import Animator


class Player1(Object):
    def __init__(self):
        super().__init__("Player1")

        self.sprite = Sprite(self)
        self.sprite.load_image("assets/sprites/player1.png", alpha=True)

        self.collider = Collider(self)
        self.collider.set_layer("ENTITY")
        self.collider.set_rect(p.Rect(0, 0, 32, 64), (15, 0))
        self.collider.add_collide_layer("TERRAIN")

        self.rigid_body = RigidBody(self)

        self.controller = Controller(self)
        self.controller.set_player(1)

        self.animator = Animator(self)
        self.animator.add_animation("IDLE", "assets/animations/player1/idle")
        self.animator.add_animation("FLOATING", "assets/animations/player1/float")
        self.animator.add_animation("FALLING", "assets/animations/player1/falling")
        self.animator.add_animation("RUNNING", "assets/animations/player1/running")
        self.animator.play_animation("IDLE")

        self.add_component(self.sprite)
        self.add_component(self.collider)
        self.add_component(self.rigid_body)
        self.add_component(self.controller)
        self.add_component(self.animator)
