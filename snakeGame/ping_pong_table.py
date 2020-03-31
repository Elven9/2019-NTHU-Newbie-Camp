from pyglet import window, clock, app, image

from game_object import *

# Create Game Window
window = window.Window(800, 600)

# Create Central Clock
clock = clock.get_default()

# Load Resource
r_basketball = image.load("./assets/basketball.png")

# Game logic
# Create Ball
ball = Ball(window.width / 2.0, window.height / 2.0, r_basketball)

# Update function
def update(ad):
    # Clear Window
    window.clear()

    ball.update_position(ball.x + 1)

    # Draw Other Object
    ball.draw()

# Add motion to game.
clock.schedule(update)

# Run App
app.run()