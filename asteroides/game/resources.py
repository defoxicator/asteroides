import pyglet

# Find the resources
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()


# Center images function
def center_image(image):
    """Sets an image's anchor point to its center."""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


# Load the resources
player_image = pyglet.resource.image('player.png')
center_image(player_image)

bullet_image = pyglet.resource.image('bullet.png')
center_image(bullet_image)

asteroid_image = pyglet.resource.image('asteroid.png')
center_image(asteroid_image)
