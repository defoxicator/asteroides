from game import resources, load
import pyglet

# Set up a window
game_window = pyglet.window.Window(800, 600)

# Set up a drawing batch
main_batch = pyglet.graphics.Batch()

# Set up top labels
score_label = pyglet.text.Label(text='Score: 0', x=10, y=460, batch=main_batch)
level_label = pyglet.text.Label(text='My Amazing Game',
                                x=game_window.width//2,
                                y=game_window.height-50,
                                anchor_x='center',
                                batch=main_batch)

# Initialize player
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300, batch=main_batch)
player_lives = load.player_lives(number_of_icons=3, batch=main_batch)

# Initialize asteroids
asteroids = load.asteroids(number_of_asteroids=3, player_position=player_ship.position,
                           batch=main_batch)

# Storing game objects to use in update loop
game_objects = [player_ship] + asteroids


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    # Pyglet clock counting dt
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
