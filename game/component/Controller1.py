import pygame as p

from game.component.Component import Component
from pygame.math import Vector2
from util.Input import Input
from game.component.Collider import Collider
from game.system.Collisions import Collision
from game.component.RigidBody import RigidBody


class Controller1(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.grounded = False
        self.ground = "TERRAIN"

    def late_update(self):
        self.grounded = False
        rect = self.owner.get_component(Collider).get_rect()
        new_rect = p.Rect(rect.bottomleft, (rect.width, 1))
        for obj in Collision.objects[self.ground].values():
            other_rect = obj.get_component(Collider).get_rect()
            if other_rect.colliderect(new_rect):
                self.grounded = True
                break

    def update(self):

        vector = Vector2()

        if self.grounded:
            vector.y = -2

        else:
            vector.y = self.owner.get_component(RigidBody).get_velocity().y

        if Input.get_key_down(p.K_w):
            vector.y = 500

        vector.x = (Input.get_key(p.K_a) - Input.get_key(p.K_d)) * 200

        if vector.x > 0:
            self.owner.sprite.flip_sprite(True)

        elif vector.x < 0:
            self.owner.sprite.flip_sprite(False)

        self.owner.get_component(RigidBody).set_velocity(vector)


