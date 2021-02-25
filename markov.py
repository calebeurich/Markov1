from PIL import Image
import turtle
import random
import numpy as np

s = turtle.getscreen()
t = turtle.Turtle()

initial_direction = [.25, .25, .25, .25]
directions = [(90, 0), (0, 1), (270, 2), (180, 3)]
#direction matrix where the order is N,E,S,W
#.5 chance to go straight, .25 chance to change 90 degrees
direction_matrix = [
    [.5, .25, 0, .25], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [.25, 0, .25, .5]
    ]

initial_color = [1, 0, 0, 0, 0, 0]
colors = [("red", 0), ("orange", 1), ("yellow", 2), ("green", 3), ("blue", 4), ("purple", 5)]
color_matrix = [
    [.5, .5, 0, 0, 0, 0], 
    [0, .5, .5, 0, 0, 0], 
    [0, 0, .5, .5, 0, 0], 
    [0, 0, 0, .5, .5, 0],
    [0, 0, 0, 0, .5, .5],
    [.5, 0, 0, 0, 0, .5],
    ]

initial_size = [.25, .25, .25, .25]
sizes = [(1, 0), (2.5, 1), (5, 2), (10, 3)]
size_matrix = [
    [.5, .5, 0, 0], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [0, 0, .5, .5]
    ]

def pick_attribute(attribute, matrix, attributes):
    new_direction = np.random.choice(attributes, p=matrix[attribute])
    return new_direction

def markov_start():
    first_direction = np.random.choice(directions, p=initial_direction)
    first_color = np.random.choice(colors, p=initial_color)
    first_size = np.random.choice(sizes, p = initial_size)
    move(first_direction, first_color, first_size)
    return

def markov_continue(direction, color, size):
    #need to use attributes to index transition matrix
    new_direction = pick_attribute(directions, direction_matrix[direction[1]])
    new_color = pick_attribute(colors, color_matrix[color[1]])
    new_size = pick_attribute(sizes, size_matrix[size[1]])
    move(new_direction, new_color, new_size)

def move(direction, color, size):
    t.setheading(direction[0])
    t.color(color[0])
    t.pensize(size[0])
    t.forward(random.randrange(0, 100))
    return



#REL_PATH = "C:/Users/User/Desktop/CC/Markov1/images/"

def main():
    markov_start()
    for i in range(50):
        markov_continue()

    #initialize values



    #im = Image.open(REL_PATH + "lakers.png")
    #im.rotate(45).show()

    return

if __name__ == "__main__": 
    main() 