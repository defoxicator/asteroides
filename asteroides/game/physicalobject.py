import pyglet
from . import util


# Motion
class PhysicalObject(pyglet.sprite.Sprite):
    """Motion class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x: float = 0.0
        self.velocity_y: float = 0.0
        self.dead = False

    def check_boundaries(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def update(self, dt):
        """Update loop"""
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_boundaries()

    def collides_with(self, other_object):
        collision_distance = self.image.width / 2 + other_object.image.width / 2
        actual_distance = util.distance(self.position, other_object.position)

        return actual_distance <= collision_distance

    def handle_collision_with(self, other_object):
        self.dead = True
