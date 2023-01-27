import pygame as p

from game.component.Component import Component
from pygame.math import Vector2
from util.Input import Input
from game.component.Collider import Collider
from game.system.Collisions import Collision
from game.component.RigidBody import RigidBody


class Controller(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.grounded = False
        self.can_jump = False
        self.ground = "TERRAIN"
        self.player = 0
        self.key_binds = []
        self.set_player(2)

    def set_player(self, player):
        self.player = player
        if player == 1:
            self.key_binds = [p.K_w, p.K_a, p.K_s, p.K_d]
        elif player == 2:
            self.key_binds = [p.K_UP, p.K_LEFT, p.K_DOWN, p.K_RIGHT]

    def early_update(self):
        self.can_jump = False
        self.grounded = False

        rect = self.owner.get_component(Collider).get_rect()
        under_rect = p.Rect(rect.bottomleft, (rect.width, 1))
        for obj in Collision.objects[self.ground].values():
            other_rect = obj.get_component(Collider).get_rect()
            if other_rect.colliderect(under_rect):
                self.grounded = True
                self.can_jump = True

        self.owner.get_component(RigidBody).set_gravity(not self.grounded)

    def update(self):

        vector = Vector2()

        if self.can_jump and Input.get_key(self.key_binds[0]):
            vector.y = 500
        elif self.grounded:
            vector.y = 0
        else:
            vector.y = self.owner.get_component(RigidBody).get_velocity_y()

        vector.x = (Input.get_key(self.key_binds[1]) - Input.get_key(self.key_binds[3])) * 200

        if vector.x > 0:
            self.owner.sprite.flip_sprite(True)

        elif vector.x < 0:
            self.owner.sprite.flip_sprite(False)

        self.owner.get_component(RigidBody).set_velocity(vector)


