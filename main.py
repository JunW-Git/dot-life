import random
import numpy as np
import pyglet

display = pyglet.canvas.get_display()
screen = display.get_screens()[-1] # Get the bigger screen (I use a laptop with a moniter)
window = pyglet.window.Window(fullscreen=True, caption="Dot Life", vsync=False, screen=screen)

STEP = 0.05 # Time between each increment (allows for slow mo and time elapse)

WIDTH, HEIGHT = window.get_size()[0], window.get_size()[1]
CENTER_X, CENTER_Y = WIDTH / 2, HEIGHT / 2

RED = ((255, 0, 0))
YELLOW = ((255, 255, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))
PURPLE = ((145, 0, 255))

RANGE = 10 # Must be above 2 (excluding 2)
MAX_SPEED = 3
POPULATION = 5000
EQUAL = True # Population of each particle is equal
locations = [] # [x, y, (r, g, b), x_force, y_force]

if EQUAL:
    for n in range(POPULATION//5):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), RED, random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])
    for n in range(POPULATION//5):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), YELLOW, random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])
    for n in range(POPULATION//5):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), GREEN, random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])
    for n in range(POPULATION//5):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), BLUE, random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])
    for n in range(POPULATION//5):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), PURPLE, random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])
else:
    for n in range(POPULATION):
        locations.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), random.choice([RED, YELLOW, GREEN, BLUE, PURPLE]), random.randint(0, MAX_SPEED), random.randint(0, MAX_SPEED)])

RANDOM_FORCE = False # Provide a random force
force_matrix = [[], [], [], [], []]
if RANDOM_FORCE:
    for i in range(5):
        for n in range(5):
            force_matrix[i].append(round(random.unform(-1, 1), 2)) # Generate random weight between -1 and 1 (2 decimal places)
else:
    force_matrix = [[1*MAX_SPEED], [0.6*MAX_SPEED], [0.2*MAX_SPEED], [-0.4*MAX_SPEED], [-1*MAX_SPEED], 
                    [-0.6*MAX_SPEED], [-1*MAX_SPEED], [0.2*MAX_SPEED], [-0.4*MAX_SPEED], [-0.3*MAX_SPEED], 
                    [1*MAX_SPEED], [0.6*MAX_SPEED], [0.3*MAX_SPEED], [-0.4*MAX_SPEED], [0.8*MAX_SPEED], 
                    [0*MAX_SPEED], [0.4*MAX_SPEED], [0.7*MAX_SPEED], [0*MAX_SPEED], [-0.7*MAX_SPEED], 
                    [0.2*MAX_SPEED], [-0.2*MAX_SPEED], [0.6*MAX_SPEED], [-0.4*MAX_SPEED], [-0.1*MAX_SPEED]]


#--------------------------------------------------------------------------------------------------------------

def calculate_distance(x1, y1, x2, y2):
    abs(np.sqrt((x1-x2)^2+(y1-y2)^2)) # Pythag

def force_equation(range, min, max):
    pass

def calculate_force(colour1, x_force1, y_force1, colour2, x_force2, y_force2, distance):
    pass

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

    # Find dots within range
    for [x1, y1, colour1, x_force1, y_force1] in locations:
        for [x2, y2, colour2, x_force1, y_force1] in locations:
            if [x1, y1] == [x2, y2]: # Stop it from comparing itself
                pass
            else:
                distance = calculate_distance(x1, y1, x2, y2)
                if distance <= 10:
                    pass

    # Draw all dots
    pop = pyglet.graphics.Batch()
    dots = []
    for loc in locations:
        dot = pyglet.shapes.Circle(loc[0], loc[1], 1, color=loc[2], batch=pop)
        dots.append(dot)
    pop.draw()

pyglet.clock.schedule_interval(update, STEP)
pyglet.app.run()