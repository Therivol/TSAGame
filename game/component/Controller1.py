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

    def early_update(self):
        self.grounded = False
        rect = self.owner.get_component(Collider).get_rect()
        for obj in Collision.objects[self.ground].values():
            other_rect = obj.get_component(Collider).get_rect()
            print(other_rect.top - rect.bottom < 3)
            if other_rect.top - rect.bottom < 3 and rect.centerx - other_rect.centerx < 16:
                self.grounded = True
                break

    def update(self):
        vector = Vector2()

        if self.grounded:
            vector.y = -2

        else:
            vector.y = self.owner.get_component(RigidBody).get_velocity().y

        vector.x = (Input.get_key(p.K_a) - Input.get_key(p.K_d)) * 200
        print(vector.y)

        self.owner.get_component(RigidBody).set_velocity(vector)


