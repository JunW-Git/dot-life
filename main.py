import random
import numpy
import pyglet

width, height = 1000, 1000
window = pyglet.window.Window(width, height)
fullscreen = True
window.set_fullscreen(fullscreen=fullscreen)

#--------------------------------------------------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers):
    pass

@window.event
def on_key_release(symbol, modifiers):
    global fullscreen
    if symbol == pyglet.window.key.F:
        if fullscreen == True:
            fullscreen = False
            window.set_fullscreen(fullscreen=fullscreen)
        else:
            fullscreen = True
            window.set_fullscreen(fullscreen=fullscreen)

#--------------------------------------------------------------------------------------------------------------

pyglet.app.run()