import random
import numpy
import pyglet

display = pyglet.canvas.get_display()
screen = display.get_screens()[-1] # Get the bigger screen (I use a laptop with a moniter)
window = pyglet.window.Window(fullscreen=True, caption="Dot Life", vsync=False, screen=screen)

time = 0.01 # Time between each increment (allows for slow mo and time elapse)

SCREEN_WIDTH, SCREEN_HEIGHT = window.get_size()[0], window.get_size()[1]

WIDTH, HEIGHT = 1000, 1000
CENTER_X, CENTER_Y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

BORDER = pyglet.graphics.Batch()
UP_BORDER = pyglet.shapes.Rectangle(x=CENTER_X-501, y=CENTER_Y+501, width=1003, height=1, color=(255, 255, 255), batch=BORDER)
BOTTOM_BORDER = pyglet.shapes.Rectangle(x=CENTER_X-501, y=CENTER_Y-501, width=1002, height=1, color=(255, 255, 255), batch=BORDER)
LEFT_BORDER = pyglet.shapes.Rectangle(x=CENTER_X-501, y=CENTER_Y-501, width=1, height=1002, color=(255, 255, 255), batch=BORDER)
RIGHT_BORDER = pyglet.shapes.Rectangle(x=CENTER_X+501, y=CENTER_Y-501, width=1, height=1003, color=(255, 255, 255), batch=BORDER)

#--------------------------------------------------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers):
    pass

@window.event
def on_key_release(symbol, modifiers):
    pass

#--------------------------------------------------------------------------------------------------------------

def update(dt):
    window.clear()

    BORDER.draw()

pyglet.clock.schedule_interval(update, time)
pyglet.app.run()