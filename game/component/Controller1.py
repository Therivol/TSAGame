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
        self.can_jump = False
        self.ground = "TERRAIN"

    def early_update(self):
        self.can_jump = False
        self.grounded = False
        rect = self.owner.get_component(Collider).get_rect()
        new_rect = p.Rect(rect.bottomleft, (rect.width, 1))
        for obj in Collision.objects[self.ground].values():
            other_rect = obj.get_component(Collider).get_rect()
            if other_rect.colliderect(new_rect):
                self.grounded = True
                self.can_jump = True
                break

        self.owner.get_component(RigidBody).set_gravity(not self.grounded)

    def update(self):

        vector = Vector2()

        if self.can_jump and Input.get_key(p.K_w):
            print("jump!")
            vector.y = 500
        else:
            vector.y = self.owner.get_component(RigidBody).get_velocity().y

        vector.x = (Input.get_key(p.K_a) - Input.get_key(p.K_d)) * 200

        if vector.x > 0:
            self.owner.sprite.flip_sprite(True)

        elif vector.x < 0:
            self.owner.sprite.flip_sprite(False)

        self.owner.get_component(RigidBody).set_velocity(vector)


