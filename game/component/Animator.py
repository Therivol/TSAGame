from dataclasses import dataclass
import pygame as p

from game.component.Component import Component
from game.component.Sprite import Sprite
from util.Assets import Assets


@dataclass
class Frame:
    image: p.Surface
    time_to: float


class Animation:
    def __init__(self, path):

        self.frames = []
        self.frame_length = 0
        self.last_change = 0
        self.curr = 0
        self.current_frame = None
        self.load(path)

    def load(self, path):
        with open(f"{path}/info.txt", "r") as file:
            for line in file:
                info = [time for time in line.split()]

        self.frame_length = len(info)
        for i, time in enumerate(info):
            self.frames.append(Frame(Assets.get_image(path + f"/{i + 1}.png", alpha=True), float(time) * 1000))

    def start(self):
        self.last_change = 0
        self.curr = 0

    def update(self, sprite):
        if p.time.get_ticks() - self.last_change > self.frames[self.curr].time_to:
            self.last_change = p.time.get_ticks()
            self.increment()
            self.current_frame = self.frames[self.curr].image
            sprite.set_surface(self.current_frame)

    def increment(self):
        self.curr = (self.curr + 1) % self.frame_length


class Animator(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.animations = {}
        self.playing = None

    def update(self):
        if self.playing:
            sprite = self.owner.get_component(Sprite)
            self.playing.update(sprite)

    def add_animation(self, name, path):
        self.animations[name] = Animation(path)

    def play_animation(self, name):
        if self.playing == self.animations[name]:
            return
        self.animations[name].start()
        self.playing = self.animations[name]
