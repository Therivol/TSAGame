import pygame as p
from game.scene.Scene import Scene
from util.TileMap import TileMap
from util.Settings import Settings
from util.Assets import Assets
from util.Input import Input
from util.Scenes import Scenes
from util.Audio import Audio
from util.Collisions import Collision
from game.object.Player1 import Player1
from game.object.Player2 import Player2
from game.object.Button1a import Button1a
from util.ObjectCollection import ObjectCollection

from game.levels.Level1 import Level1


class Level(Scene):
    def __init__(self):
        super().__init__("LEVEL")

        self.level = None

    def awake(self):
        pass

    def set_level(self, level):
        if level == '1':
            self.level = Level1()

        elif level == '2':
            pass

        elif level == '3':
            pass

        self.clear()

        TileMap.set_level(level)

    def clear(self):
        TileMap.clear()
        Collision.clear()
        ObjectCollection.clear()

    def early_update(self):
        ObjectCollection.early_update()

    def update(self):
        ObjectCollection.update()
        Collision.update()

        if Input.get_key_down(p.K_ESCAPE):
            Scenes.set_scene("PAUSE")


    def late_update(self):
        ObjectCollection.late_update()

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.blit(Assets.get_image("assets/backgrounds/level.png"), (0, 0))
        TileMap.render(surf)
        self.player1.sprite.draw(surf)
        self.player2.sprite.draw(surf)
        self.button.sprite.draw(surf)

        return surf

    def exit(self):
        pass

    def enter(self):
        pass