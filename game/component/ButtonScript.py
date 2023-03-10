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
            if not self.pressed:
                self.reset()

    def early_update(self):
        if self.pressed != self.last_pressed:
            if self.pressed:
                self.press()

    def press(self):
        self.owner.press()

    def reset(self):
        self.owner.reset()
