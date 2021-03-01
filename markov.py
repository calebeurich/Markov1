import turtle
import random
import numpy as np

ITERATIONS = 200


s = turtle.getscreen()
t = turtle.Turtle()
turtle.screensize(canvwidth=500, canvheight=500) 

initial_direction = [.25, .25, .25, .25]
directions = [90, 0, 270, 180]
direction_keys = {90:0, 0:1, 270:2, 180:3}
#direction matrix where the order is N,E,S,W
#.5 chance to go straight, .25 chance to change 90 degrees
direction_matrix = [
    [.5, .25, 0, .25], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [.25, 0, .25, .5]
    ]

initial_color = [1, 0, 0, 0, 0, 0]
color_keys = {"red":0, "orange":1, "yellow":2, "green":3, "blue":4, "purple":5}
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_matrix = [
    [.5, .5, 0, 0, 0, 0], 
    [0, .5, .5, 0, 0, 0], 
    [0, 0, .5, .5, 0, 0], 
    [0, 0, 0, .5, .5, 0],
    [0, 0, 0, 0, .5, .5],
    [.5, 0, 0, 0, 0, .5],
    ]

initial_size = [.25, .25, .25, .25]
size_keys = {1:0, 2.5:1, 5:2, 10:3}
sizes = [1, 2.5, 5, 10]
size_matrix = [
    [.5, .5, 0, 0], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [0, 0, .5, .5]
    ]

def pick_attribute(attributes, matrix):
    new_attribute = np.random.choice(attributes, p=matrix)
    return new_attribute

def markov_start():
    first_direction = np.random.choice(directions, p=initial_direction)
    first_color = np.random.choice(colors, p=initial_color)
    first_size = np.random.choice(sizes, p = initial_size)
    return [first_direction, first_color, first_size]

def markov_continue(previous_direction, previous_color, previous_size):
    new_direction = pick_attribute(directions, direction_matrix[direction_keys.get(previous_direction)])
    new_color = pick_attribute(colors, color_matrix[color_keys.get(previous_color)])
    new_size = pick_attribute(sizes, size_matrix[size_keys.get(previous_size)])
    return [new_direction, new_color, new_size]

def move(direction, color, size):
    t.setheading(direction)
    t.color(color)
    t.pensize(size)
    t.forward(random.randrange(0, 10))

def main():
    initial_values = markov_start()
    move(initial_values[0], initial_values[1], initial_values[2])
    for i in range(ITERATIONS):
        if i == 0:
            previous_values = initial_values
        new_values = markov_continue(previous_values[0], previous_values[1], previous_values[2])
        move(new_values[0], new_values[1], new_values[2])
        previous_values = new_values

if __name__ == "__main__": 
    main() 