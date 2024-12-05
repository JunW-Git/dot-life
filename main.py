import random
import numpy as np
import pyglet

#--------------------------------------------------------------------------------------------------------------

display = pyglet.canvas.get_display()
screen = display.get_screens()[-1] # Get the bigger screen (I use a laptop with a moniter)
window = pyglet.window.Window(fullscreen=True, caption="Dot Life", vsync=False, screen=screen)

STEP = 0.1 # Time between each increment (allows for slow mo and time elapse)

WIDTH, HEIGHT = window.get_size()[0], window.get_size()[1]
CENTER_X, CENTER_Y = WIDTH / 2, HEIGHT / 2

RED = ((255, 0, 0))
YELLOW = ((255, 255, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))
PURPLE = ((145, 0, 255))
COLOURS = [RED, YELLOW, GREEN, BLUE, PURPLE]

RANGE = 2000 # Must be above 2 (excluding 2)
REPULSION = 3 # Make sure particles are too close
MAX_SPEED = 2 # Max velocity that is added/removed every increment (not actually max speed it can travel)
POPULATION = 2
EQUAL = False # Population of each particle is equal
locations = [] # [x, y, (r, g, b), x_vel, y_vel]

def rng_force():
    return round(random.uniform(-1*MAX_SPEED, MAX_SPEED), 2)

if EQUAL:
    for n in range(POPULATION//5):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, RED, rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False
    for n in range(POPULATION//5):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, YELLOW, rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False
    for n in range(POPULATION//5):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, GREEN, rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False
    for n in range(POPULATION//5):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, BLUE, rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False
    for n in range(POPULATION//5):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, PURPLE, rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False
else:
    for n in range(POPULATION):
        dupe = True # Prevent dots in the same spot
        while dupe:
            values = [random.randint(0, WIDTH*100)/100, random.randint(0, HEIGHT*100)/100, random.choice([RED, YELLOW, GREEN, BLUE, PURPLE]), rng_force(), rng_force()]
            if values in locations:
                pass
            else:
                locations.append(values)
                dupe = False

RANDOM_FORCE = False # Provide a random force
V_max_matrix = [[], [], [], [], []]
if RANDOM_FORCE:
    for i in range(5):
        for n in range(5):
            V_max_matrix[i].append(round(random.uniform(-1, 1), 2)) # Generate random weight between -1 and 1 (2 decimal places)
    V_max_matrix = np.dot(V_max_matrix, [MAX_SPEED])
else:
    V_max_matrix = [[1*MAX_SPEED, 0.6*MAX_SPEED, 0.2*MAX_SPEED, -0.4*MAX_SPEED, -1*MAX_SPEED], 
                    [-0.6*MAX_SPEED, -1*MAX_SPEED, 0.2*MAX_SPEED, -0.4*MAX_SPEED, -0.3*MAX_SPEED], 
                    [1*MAX_SPEED, 0.6*MAX_SPEED, 0.3*MAX_SPEED, -0.4*MAX_SPEED, 0.8*MAX_SPEED], 
                    [0*MAX_SPEED, 0.4*MAX_SPEED, 0.7*MAX_SPEED, 0*MAX_SPEED, -0.7*MAX_SPEED], 
                    [0.2*MAX_SPEED, -0.2*MAX_SPEED, 0.6*MAX_SPEED, -0.4*MAX_SPEED, -0.1*MAX_SPEED]]

#--------------------------------------------------------------------------------------------------------------

def calculate_distance(x1, y1, x2, y2):
    dist = abs(float((np.sqrt((x1-x2)**2+(y1-y2)**2)))) # Pythag
    x, y = abs(float(x2-x1)), abs(float(y2-y1))
    return dist, x, y

def force_equation(max_matrix):
    global MAX_SPEED, RANGE, REPULSION, COLOURS, V_max_matrix

    force_equation_matrix = [[[], [], [], [], []], 
                             [[], [], [], [], []], 
                             [[], [], [], [], []], 
                             [[], [], [], [], []], 
                             [[], [], [], [], []]]

    count = 0
    for row in max_matrix:
        for max in row:
            m1, c1 = max / 2, -1 * max

            m2 = max / (REPULSION - RANGE) # Calculate gradient for force equation
            c2 = max - ((REPULSION * max) / (REPULSION - RANGE)) # Calculate y-intercept value
            force_equation_matrix[count//5][count%5].append([m1, c1])
            force_equation_matrix[count//5][count%5].append([m2, c2])
            count += 1
    return force_equation_matrix

force_equation_matrix = force_equation(V_max_matrix)
    
def calculate_force(colour1, x_vel1, y_vel1, colour2, x_vel2, y_vel2, distance, x_distance, y_distance, force_equations):
    colour_index1 = COLOURS.index(colour1)
    colour_index2 = COLOURS.index(colour2)

    new_d = 0
    if distance <= 2: # Repulsion when close than range of 2.
        new_d = force_equations[colour_index1][colour_index2][0][0] * distance + force_equations[colour_index1][colour_index2][0][1]
    else: # Force for when range is in 2 - 10 zone.
        new_d = force_equations[colour_index1][colour_index2][1][0] * distance + force_equations[colour_index1][colour_index2][1][1]
    
    proportional = new_d / distance # Find proportion (to calculate x_d and y_d since they are similar triangles)
    x_new = proportional * x_vel1
    y_new = proportional * y_vel1

    return x_new, y_new

def calculate_position(x, y, x_vel, y_vel): # Calculate the new positions
    return x+x_vel, y+y_vel

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
    index = 0
    for [x1, y1, colour1, x_vel1, y_vel1] in locations[:-1]:
        count = 0
        for [x2, y2, colour2, x_vel2, y_vel2] in locations[index+1:]:
            distance, x_distance, y_distance = calculate_distance(x1, y1, x2, y2)
            if [x1, y1] == [x2, y2]: # For some reason there's always some 2 dots on (0, 0)
                pass
            elif distance <= 10: # If within range for force to occur
                locations[index][0], locations[index][1] = calculate_force(colour1, x_vel1, y_vel1, colour2, x_vel2, y_vel2, distance, x_distance, y_distance, force_equation_matrix)
                locations[index+1+count][0], locations[index+1+count][1] = calculate_force(colour2, x_vel2, y_vel2, colour1, x_vel1, y_vel1, distance, x_distance, y_distance, force_equation_matrix)
            else: # If out of range, do nothing
                pass
            count += 1
        index += 1

    # Draw all dots
    pop = pyglet.graphics.Batch()
    dots = []
    for loc in locations:
        dot = pyglet.shapes.Circle(loc[0], loc[1], 5, color=loc[2], batch=pop)
        dots.append(dot)
    pop.draw()

pyglet.clock.schedule_interval(update, STEP)
pyglet.app.run()