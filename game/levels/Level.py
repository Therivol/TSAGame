from game.object.Player1 import Player1
from game.object.Player2 import Player2

from util.Collisions import Collision
from util.ObjectCollection import ObjectCollection


class Level:

    def __init__(self):
        self.objects = []

        self.player1 = Player1()
        self.player2 = Player2()

        self.add_object(self.player1)
        self.add_object(self.player2)

    def add_object(self, obj):
        self.objects.append(obj)
        ObjectCollection.add(obj)
        Collision.add(obj)

    def early_update(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    def get_surface(self):
        pass
