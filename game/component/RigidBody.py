from game.component.Component import Component
from util.Time import Time
from pygame.math import Vector2
from util.Physics import Physics


class RigidBody(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.velocity = Vector2()

    def velocity_change(self, vel):
        self.velocity += vel

    def set_velocity(self, vel):
        self.velocity.update(vel)

    def get_velocity(self):
        return self.velocity

    def apply_gravity(self):
        self.velocity.y += Physics.gravity * Time.delta() * 100

    def update(self):
        self.apply_gravity()
        self.owner.transform.add_position_pos(-self.velocity * Time.delta())
