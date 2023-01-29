import pygame as p

from game.object.Object import Object
from game.component.Collider import Collider
from game.component.Sprite import Sprite
from game.component.ButtonScript import ButtonScript

from util.Assets import Assets


class Button(Object):
    def __init__(self):
        super().__init__(self)

        self.sprite = Sprite(self)
        self.sprite.set_surface(Assets.get_image("assets/objects/buttonup.png", alpha=True))

        self.collider = Collider(self)
        self.collider.set_layer("TERRAIN")
        self.collider.set_rect(p.Rect(0, 0, 14, 16), (1, 16))
        self.collider.is_trigger = True

        self.script = ButtonScript(self)

        self.transform.set_static(True)

        self.add_component(self.sprite)
        self.add_component(self.collider)
        self.add_component(self.script)

    def press(self):
        pass

    def reset(self):
        pass
