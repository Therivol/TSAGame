from game.component.Collider import Collider
from game.object.Object import Object
import pygame as p


class Collision:
    collision_layers = ["DEFAULT", "TERRAIN", "ENTITY"]
    objects = {layer: {} for layer in collision_layers}

    @staticmethod
    def add(obj):
        Collision.objects[obj.get_component(Collider).layer][obj.get_id()] = obj

    @staticmethod
    def remove(obj):
        del Collision.objects[obj.get_component(Collider).layer][obj.get_id()]

    @staticmethod
    def clear():
        Collision.objects = {layer: {} for layer in Collision.collision_layers}

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
        for layer in Collision.objects:
            for obj in Collision.objects[layer].values():
                collider = obj.get_component(Collider)
                collider.reset_manifold()

                if obj.transform.is_static:
                    continue

                for x in Collision.search(collider):
                    hit = x.get_component(Collider)
                    if hit.is_trigger:
                        hit.set_manifold(True, collider)
                        continue

                    m = collider.intersects(hit)
                    if m.colliding:
                        collider.resolve_overlap(m)
                        collider.reset_manifold()

    @staticmethod
    def search(collider):
        overlapping_objects = []

        for layer in collider.collide_layers:
            for obj_id, obj in Collision.objects[layer].items():
                if obj.get_component(Collider) is collider:
                    continue
                if obj.get_component(Collider).get_rect().colliderect(collider.get_rect()):
                    overlapping_objects.append(obj)

        return overlapping_objects
