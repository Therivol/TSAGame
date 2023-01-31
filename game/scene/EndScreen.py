from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets
from util.Audio import Audio
from game.scene.Scene import Scene
from gui.element.Button import Button
import pygame as p


class EndScreen(Scene):
    def __init__(self):
        super().__init__("END SCREEN")

        self.menu_button = Button(p.Rect(384, 239, 192, 64), "assets/ui/button_1_idle.png",
                                  "assets/ui/button_1_active.png")

    def awake(self):
        pass

    def update(self):
        if self.menu_button.update():
            Scenes.set_scene("MAIN MENU")

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/default.png"), (0, 0))

        self.menu_button.draw(surf)

        surf.blit(Assets.get_image("assets/ui/title.png", alpha=True), (352, 50))

        surf.blit(Assets.get_image("assets/ui/thankyou.png", alpha=True), (224, 350))

        surf.blit(Assets.get_image("assets/ui/menu.png", alpha=True), (384, 239))

        return surf

    def enter(self):
        if not Audio.current_track == "assets/sounds/level.wav":
            pass
            # Audio.play_track("assets/sounds/level.wav")
