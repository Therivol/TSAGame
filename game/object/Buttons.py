from game.object.Button import Button
from util.TileMap import TileMap
from util.Collisions import Collision
from game.component.Sprite import Sprite
from util.Assets import Assets


class Button1a(Button):

    def __init__(self):
        super().__init__("Button1a")

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.sprite.load_image("assets/objects/buttondown.png", alpha=True)

        TileMap.set_tile(6, 11, "2")
        TileMap.set_tile(7, 11, "2")

    def reset(self):
        self.sprite.load_image("assets/objects/buttonup.png", alpha=True)

        TileMap.set_tile(6, 11, "0")
        TileMap.set_tile(7, 11, "0")


class Button2a(Button):

    def __init__(self):
        super().__init__("Button1a")

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.sprite.load_image("assets/objects/buttondown.png", alpha=True)

        TileMap.set_tile(25, 8, "2")
        TileMap.set_tile(27, 10, "2")
        TileMap.set_tile(25, 12, "2")

    def reset(self):
        self.sprite.load_image("assets/objects/buttonup.png", alpha=True)

        TileMap.set_tile(25, 8, "0")
        TileMap.set_tile(27, 10, "0")
        TileMap.set_tile(25, 12, "0")