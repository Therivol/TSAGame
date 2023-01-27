from game.component.Collider import Collider
from game.object.Object import Object
import pygame as p
import math


class Collision:
    collision_layers = ["TERRAIN", "DEFAULT", "DEFAULT"]
    objects = {layer: {} for layer in collision_layers}
    grid_size = 64  # size of each grid cell
    grid = {}  # dictionary to store objects in each grid cell

    @staticmethod
    def add(obj):
        Collision.objects[obj.get_component(Collider).layer][obj.get_id()] = obj
        Collision.add_to_grid(obj)

    @staticmethod
    def remove(obj):
        collider = obj.get_component(Collider)
        del Collision.objects[collider.layer][obj.get_id()]
        Collision.remove_from_grid(obj)

    @staticmethod
    def clear():
        Collision.objects = {layer: {} for layer in Collision.collision_layers}
        Collision.grid = {}

    @staticmethod
    def process_removals():
        for layer in Collision.collision_layers:
            Collision.objects[layer] = {obj.get_id(): obj for obj in Collision.objects[layer]
                                        if not obj.is_queued_for_removal}

    @staticmethod
    def update():
        Collision.resolve()

    @staticmethod
    def resolve():
        for layer in Collision.collision_layers:
            for obj in Collision.objects[layer].values():
                collider = obj.get_component(Collider)

                if obj.transform.is_static:
                    continue
                for x in Collision.search_in_grid(collider):
                    hit = x.get_component(Collider)
                    if hit.is_trigger:
                        hit.set_manifold(True, collider)
                        continue

                    m = collider.intersects(hit)
                    if m.colliding:
                        collider.resolve_overlap(m)
                        collider.reset_manifold()

    @staticmethod
    def search_in_grid(collider):
        rect = collider.get_rect()
        grid_x = rect.x // Collision.grid_size
        grid_y = rect.y // Collision.grid_size
        overlapping_objects = []
        for i in range(grid_x - 1, grid_x + 2):
            for j in range(grid_y - 1, grid_y + 2):
                if i in Collision.grid and j in Collision.grid[i]:
                    overlapping_objects += Collision.grid[i][j]
        return overlapping_objects

    @staticmethod
    def search(collider):
        overlapping_objects = []

        # get the grid cells that the collider's rectangle occupies
        x1, y1 = int(collider.rect.left / Collision.grid_size), int(collider.rect.top / Collision.grid_size)
        x2, y2 = int(math.ceil(collider.rect.right / Collision.grid_size)) - 1, int(math.ceil(collider.rect.bottom / Collision.grid_size)) - 1

        # check objects in each occupied grid cell
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in Collision.grid:
                    for obj in Collision.grid[(x, y)]:
                        if obj.get_component(Collider).get_rect().colliderect(collider.get_rect()):
                            overlapping_objects.append(obj)

        return overlapping_objects

    @staticmethod
    def load_level(map_data, tile_size):
        i = 0
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    continue
                obj = Object(str(i))
                collider = Collider(obj)
                collider.set_rect(p.Rect(0, 0, tile_size, tile_size), (0, 0))
                collider.set_layer("TERRAIN")
                obj.add_component(collider)
                obj.transform.set_position((x * tile_size, y * tile_size))
                Collision.add(obj)

                i += 1

    @staticmethod
    def add_to_grid(obj):
        collider = obj.get_component(Collider)
        rect = collider.get_rect()
        grid_x = rect.x // Collision.grid_size
        grid_y = rect.y // Collision.grid_size

        if grid_x not in Collision.grid:
            Collision.grid[grid_x] = {}
        if grid_y not in Collision.grid[grid_x]:
            Collision.grid[grid_x][grid_y] = []

        Collision.grid[grid_x][grid_y].append(obj)

    @staticmethod
    def remove_from_grid(obj):
        collider = obj.get_component(Collider)
        rect = collider.get_rect()
        grid_x = rect.x // Collision.grid_size
        grid_y = rect.y // Collision.grid_size

        if grid_x in Collision.grid and grid_y in Collision.grid[grid_x]:
            if obj in Collision.grid[grid_x][grid_y]:
                Collision.grid[grid_x][grid_y].remove(obj)


class Time:
    time_started = 0
    delta_time_ns = 0
    last_time = 0

    @staticmethod
    def awake():
        Time.time_started = time.time_ns()
        Time.last_time = time.time_ns()

    @staticmethod
    def calculate_dt():
        Time.delta_time_ns = (time.time_ns() - Time.last_time)
        Time.last_time = time.time_ns()

    @staticmethod
    def delta():
        return Time.delta_time_ns / 1000000000

    @staticmethod
    def elapsed():
        return (time.time_ns() - Time.time_started) / 1000000000