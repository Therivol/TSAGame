from game.component.Component import Component
from util.Time import Time
from pygame.math import Vector2
from util.Physics import Physics
import pygame as p


class RigidBody(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.velocity = Vector2()
        self.gravity = True

    def velocity_change(self, vel):
        self.velocity += vel

    def set_velocity(self, vel):
        self.velocity.update(vel)

    def set_velocity_x(self, x):
        self.velocity.x = x

    def set_velocity_y(self, y):
        self.velocity.y = y

    def get_velocity(self):
        return self.velocity

    def get_velocity_x(self):
        return self.velocity.x

    def get_velocity_y(self):
        return self.velocity.y

    def set_gravity(self, gravity):
        self.gravity = gravity

    def apply_gravity(self, multiplier=1):
        if self.gravity:
            self.velocity.y += Physics.gravity * multiplier * Time.delta() * 100

    def update(self):
        self.apply_gravity()
        self.owner.transform.add_position_pos(-self.velocity * Time.delta())
