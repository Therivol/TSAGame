from game.component.Component import Component
from game.component.Collider import Collider
from game.component.Sprite import Sprite


class ButtonScript(Component):

    def __init__(self, owner):
        super().__init__(owner)

        self.pressed = False
        self.last_pressed = False

    def update(self):
        self.last_pressed = self.pressed
        self.pressed = self.owner.get_component(Collider).is_triggered()

        if self.pressed != self.last_pressed:
            if self.pressed:
                self.press()
            else:
                self.reset()

    def press(self):
        self.owner.get_component(Sprite).load_image("assets/objects/buttondown.png", alpha=True)
        self.owner.press()

    def reset(self):
        self.owner.get_component(Sprite).load_image("assets/objects/buttonup.png", alpha=True)
        self.owner.reset()
