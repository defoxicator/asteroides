from . import resources
import pyglet
import random
import math


def asteroids(number_of_asteroids, player_position, batch=None):
    """Randomly places asteroids on the field."""
    asteroids_coordinates: list = []
    for i in range(number_of_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y,
                                            batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids_coordinates.append(new_asteroid)
    return asteroids_coordinates


def player_lives(number_of_icons, batch=None):
    """Generate sprites placement for player lives."""
    player_lives_count = []
    for i in range(number_of_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=780-i*35, y=585, batch=batch)
        new_sprite.scale = 0.5
        player_lives_count.append(new_sprite)
    return player_lives_count


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)
