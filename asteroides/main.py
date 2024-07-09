"""Main module of the game"""
from game import load, player
import pyglet


# Set up a window
game_window = pyglet.window.Window(800, 600)

# Set up a drawing batch
main_batch = pyglet.graphics.Batch()

# Set up top labels
score_count: int = 0
score_label = pyglet.text.Label(text=f'Score: 0', x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text='Asteroides',
                                x=400, y=575,
                                anchor_x='center',
                                batch=main_batch)

# Initialize player
player_ship = player.Player(x=400, y=300, batch=main_batch)

# Initialize player lives
player_lives = load.player_lives(number_of_lives=3, batch=main_batch)

# Initialize asteroids
asteroids = load.asteroids(number_of_asteroids=3, player_position=player_ship.position,
                           batch=main_batch)

# Game over text
game_over_overlay = pyglet.text.Label(text='GAME OVER',
                                              color=[255, 255, 255, 135],
                                              font_size=50,
                                              x=400, y=-100,
                                              anchor_x='center',
                                              anchor_y='center',
                                              batch=main_batch)

game_over_screen = pyglet.text.Label(text='GAME OVER',
                                     color=[254, 32, 32, 185],
                                     font_size=48,
                                     x=400, y=-100,
                                     anchor_x='center',
                                     anchor_y='center',
                                     batch=main_batch)

# Storing game objects to use in update loop
game_objects = [player_ship] + asteroids

# Moving the ship
game_window.push_handlers(player_ship.key_handler)

for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)


@game_window.event
def on_draw():
    """Drawing to screen"""
    game_window.clear()
    main_batch.draw()


def update(dt):
    """Update loop"""
    global score_count

    for (i, obj1) in enumerate(game_objects):
        for (_, obj2) in list(enumerate(game_objects))[i+1:]:
            if not obj1.dead and not obj2.dead:
                if obj1.collides_with(obj2):
                    obj1.handle_collision_with(obj2)
                    obj2.handle_collision_with(obj1)

    to_add: list = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    for to_remove in [obj for obj in game_objects if obj.dead]:
        # Scoring
        if to_remove.is_scorable:
            score_count += 1
            score_label.text = f'Score: {score_count}'

        to_remove.delete()
        game_objects.remove(to_remove)

    game_objects.extend(to_add)

    # Game Over screen
    if player_ship.dead:
        game_over_overlay.y = 300
        game_over_screen.y = 300


if __name__ == '__main__':
    # Pyglet clock counting dt
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
