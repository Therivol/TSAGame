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


class Button1b(Button):

    def __init__(self):
        super().__init__("Button1a")

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.sprite.load_image("assets/objects/buttondown.png", alpha=True)

        TileMap.set_tile(25, 8, "2")
        TileMap.set_tile(21, 10, "2")
        TileMap.set_tile(25, 12, "2")

    def reset(self):
        self.sprite.load_image("assets/objects/buttonup.png", alpha=True)

        TileMap.set_tile(25, 8, "0")
        TileMap.set_tile(21, 10, "0")
        TileMap.set_tile(25, 12, "0")


class Button2a(Button):
    def __init__(self):
        super().__init__("Button1a")

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.sprite.load_image("assets/objects/buttondown.png", alpha=True)

        TileMap.set_tile(9, 8, "2")
        TileMap.set_tile(10, 8, "2")
        TileMap.set_tile(11, 8, "2")

    def reset(self):
        self.sprite.load_image("assets/objects/buttonup.png", alpha=True)

        TileMap.set_tile(9, 8, "0")
        TileMap.set_tile(10, 8, "0")
        TileMap.set_tile(11, 8, "0")


class Button2b(Button):
    def __init__(self):
        super().__init__("Button1a")

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.sprite.load_image("assets/objects/buttondown.png", alpha=True)

        TileMap.set_tile(17, 10, "2")
        TileMap.set_tile(18, 10, "2")
        TileMap.set_tile(19, 10, "2")

    def reset(self):
        self.sprite.load_image("assets/objects/buttonup.png", alpha=True)

        TileMap.set_tile(17, 10, "0")
        TileMap.set_tile(18, 10, "0")
        TileMap.set_tile(19, 10, "0")

class Switch2a(Button):
    def __init__(self):
        super().__init__("Button1a")

        self.on = False

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/leverleft.png", alpha=True))

        self.add_component(self.sprite)

    def press(self):
        self.on = not self.on
        if self.on:
            self.sprite.load_image("assets/objects/leverright.png", alpha=True)

            TileMap.set_tile(2, 15, "2")
            TileMap.set_tile(3, 15, "2")
            TileMap.set_tile(8, 15, "2")
            TileMap.set_tile(9, 15, "2")
            TileMap.set_tile(14, 15, "2")
            TileMap.set_tile(15, 15, "2")
            TileMap.set_tile(20, 15, "2")
            TileMap.set_tile(21, 15, "2")

        if not self.on:
            self.sprite.load_image("assets/objects/leverleft.png", alpha=True)

            TileMap.set_tile(2, 15, "0")
            TileMap.set_tile(3, 15, "0")
            TileMap.set_tile(8, 15, "0")
            TileMap.set_tile(9, 15, "0")
            TileMap.set_tile(14, 15, "0")
            TileMap.set_tile(15, 15, "0")
            TileMap.set_tile(20, 15, "0")
            TileMap.set_tile(21, 15, "0")
