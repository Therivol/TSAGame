from game.object.Player1 import Player1
from game.object.Player2 import Player2

from util.Collisions import Collision
from util.ObjectCollection import ObjectCollection

from game.component.Sprite import Sprite
from game.component.Collider import Collider


class Level:

    def __init__(self):
        self.objects = []
        self.player1 = None
        self.player2 = None

    def awake(self):
        self.player1 = Player1()
        self.player2 = Player2()

        self.add_object(self.player1)
        self.add_object(self.player2)

    def add_object(self, obj):
        self.objects.append(obj)
        ObjectCollection.add(obj)
        if obj.get_component(Collider):
            Collision.add(obj)

    def update(self):
        pass

    def get_surface(self):
        pass

    def draw(self, surf):
        for obj in self.objects:
            obj.get_component(Sprite).draw(surf)
