from game.object.Button import Button
from util.TileMap import TileMap
from util.Collisions import Collision


class Button1a(Button):

    def press(self):
        TileMap.set_tile(6, 11, "2")
        TileMap.set_tile(7, 11, "2")

    def reset(self):
        print("k")
        TileMap.set_tile(6, 11, "0")
        TileMap.set_tile(7, 11, "0")
