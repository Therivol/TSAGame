from util.Collisions import Collision
from game.component.Collider import Collider


class ObjectCollection:
    objects = []
    new_objects = []

    @staticmethod
    def add(*args):
        for new_object in args:
            ObjectCollection.new_objects.append(new_object)

    @staticmethod
    def early_update():
        for obj in ObjectCollection.objects:
            obj.early_update()

    @staticmethod
    def update():
        ObjectCollection.process_removals()
        ObjectCollection.process_new_objects()

        for obj in ObjectCollection.objects:
            obj.update()

    @staticmethod
    def late_update():
        for obj in ObjectCollection.objects:
            obj.late_update()

    @staticmethod
    def draw(canvas):
        for obj in ObjectCollection.objects:
            obj.draw(canvas)

    @staticmethod
    def process_new_objects():
        if len(ObjectCollection.new_objects) > 0:
            for obj in ObjectCollection.new_objects:
                obj.awake()

            for obj in ObjectCollection.new_objects:
                obj.start()

                if obj.get_component(Collider):
                    Collision.add(obj)

            ObjectCollection.objects += ObjectCollection.new_objects
            ObjectCollection.new_objects.clear()

    @staticmethod
    def process_removals():
        ObjectCollection.objects = [obj for obj in ObjectCollection.objects if not obj.is_queued_for_removal]

    @staticmethod
    def clear():
        ObjectCollection.objects.clear()
        ObjectCollection.new_objects.clear()
