from . import resources, physicalobject, util, asteroid
import pyglet
import random


def asteroids(number_of_asteroids, player_position, batch=None):
    """Randomly places asteroids on the field with random velocity not in proximity of the player"""
    asteroids_coordinates: list = []
    for i in range(number_of_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while util.distance(point_1=(asteroid_x, asteroid_y),
                            point_2=player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
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
