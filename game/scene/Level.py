import pygame as p
from game.scene.Scene import Scene
from util.TileMap import TileMap
from util.Settings import Settings
from util.Assets import Assets
from util.Input import Input
from util.Scenes import Scenes
from game.system.Collisions import Collision
from game.object.Player1 import Player1
from game.object.Player2 import Player2
from game.object.PushingBox import PushingBox
from game.system.ObjectCollection import ObjectCollection
from game.component.Controller import Controller

from game.component.Animator import Animation


class Level(Scene):
    def __init__(self):
        super().__init__("LEVEL")
        self.player1 = None
        self.player2 = None

    def awake(self):
        pass

    def set_level(self, level):
        self.clear()

        TileMap.set_level(level)

        self.player1 = Player1()
        self.player2 = Player2()

        # self.test = PushingBox()

        self.player1.transform.set_position((75, 350))
        self.player2.transform.set_position((80, 350))

        ObjectCollection.add(self.player1)
        ObjectCollection.add(self.player2)
        # ObjectCollection.add(self.test)
        Collision.add(self.player1)
        Collision.add(self.player2)
        # Collision.add(self.test)

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
        # self.test.sprite.draw(surf)

        return surf

    def exit(self):
        TileMap.clear()

