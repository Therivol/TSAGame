import math
import pygame
import time


class OldTime:
    time_started = 0
    delta_time_ns = 0
    last_time = 0

    @staticmethod
    def awake():
        Time.time_started = pygame.time.get_ticks()
        Time.last_time = pygame.time.get_ticks()

    @staticmethod
    def start_frame():
        Time.last_time = pygame.time.get_ticks()

    @staticmethod
    def calculate_dt():
        Time.delta_time_ns = (pygame.time.get_ticks() - Time.last_time)

    @staticmethod
    def delta():
        return Time.delta_time_ns / 1000

    @staticmethod
    def elapsed():
        return (pygame.time.get_ticks() - Time.time_started) / 1000


class Time:
    time_started = 0
    delta_time_ns = 0
    last_time = 0

    @staticmethod
    def awake():
        Time.time_started = time.time_ns()
        Time.last_time = time.time_ns()

    @staticmethod
    def start_frame():
        Time.last_time = time.time_ns()

    @staticmethod
    def calculate_dt():
        Time.delta_time_ns = (time.time_ns() - Time.last_time)

    @staticmethod
    def delta():
        return Time.delta_time_ns / 1000000000 * 2

    @staticmethod
    def elapsed():
        return (time.time_ns() - Time.time_started) / 1000000000