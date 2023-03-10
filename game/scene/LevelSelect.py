from gui.element.Button import Button
from util.Settings import Settings
from util.Assets import Assets
from util.Input import Input
from util.Scenes import Scenes
from game.scene.Scene import Scene
import pygame as p


class LevelSelect(Scene):
    def __init__(self):
        super().__init__("LEVEL SELECT")
        self.shadow = None
        self.back_button = Button(p.Rect(384, 412, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

        self.button_1 = Button(p.Rect(132, 82, 64, 64), "assets/ui/button_2_idle.png",
                               "assets/ui/button_2_active.png")
        self.button_2 = Button(p.Rect(228, 82, 64, 64), "assets/ui/button_locked.png",
                               "assets/ui/button_locked.png")
        self.button_3 = Button(p.Rect(324, 82, 64, 64), "assets/ui/button_locked.png",
                               "assets/ui/button_locked.png")

        self.available_levels = [1]

    def awake(self):
        self.shadow = p.Surface((760, 444))
        self.shadow.fill((0, 0, 0))
        self.shadow.set_alpha(120)

    def update(self):
        if Input.get_key_down(p.K_ESCAPE) or self.back_button.update():
            Scenes.set_scene("MAIN MENU")

        if self.button_1.update() and 1 in self.available_levels:
            Scenes.set_scene("LEVEL")
            Scenes.get_scene("LEVEL").set_level('1')

        if self.button_2.update() and 2 in self.available_levels:
            Scenes.set_scene("LEVEL")
            Scenes.get_scene("LEVEL").set_level('2')

        if self.button_3.update() and 3 in self.available_levels:
            Scenes.set_scene("LEVEL")
            Scenes.get_scene("LEVEL").set_level('3')

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/default.png"), (0, 0))

        surf.blit(self.shadow, (100, 50))

        self.button_1.draw(surf)
        self.button_2.draw(surf)
        self.button_3.draw(surf)

        if 1 in self.available_levels:
            surf.blit(Assets.get_image("assets/ui/1.png", alpha=True), (132, 82))
        if 2 in self.available_levels:
            surf.blit(Assets.get_image("assets/ui/2.png", alpha=True), (228, 82))
        if 3 in self.available_levels:
            surf.blit(Assets.get_image("assets/ui/3.png", alpha=True), (324, 82))

        self.back_button.draw(surf)
        surf.blit(Assets.get_image("assets/ui/quit.png", alpha=True), (384, 412))

        return surf

    def open_level(self, level):
        if level not in self.available_levels:
            self.available_levels.append(level)

        if level == 1:
            self.button_1 = Button(p.Rect(132, 82, 64, 64), "assets/ui/button_2_idle.png",
                                   "assets/ui/button_2_active.png")

        elif level == 2:
            self.button_2 = Button(p.Rect(228, 82, 64, 64), "assets/ui/button_2_idle.png",
                               "assets/ui/button_2_active.png")

        elif level == 3:
            self.button_3 = Button(p.Rect(324, 82, 64, 64), "assets/ui/button_2_idle.png",
                               "assets/ui/button_2_active.png")
