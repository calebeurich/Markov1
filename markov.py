'''
Caleb Eurich
CSCI 3725
M3
March 1, 2021
This file contains the Markov Cat Rainbow Generator system. This file uses turtle to generate rainbow lines using the markov property. The three
attributes, direction, color, and pensize, have their own transistion matricies that are used by the markov functions to generate visual art. 
The output is a conglomerate of ranibow lines that can be fun to look at!
'''

import turtle
import random
import numpy as np

#global variables
ITERATIONS = 1000
MIN_LINE_LENGTH = 5
MAX_LINE_LENGTH = 10

#define turtle variables
s = turtle.getscreen()
t = turtle.Turtle()
turtle.screensize(canvwidth=500, canvheight=500)
t.speed(10)
turtle.hideturtle()

#set turtle to nyan cat
#had trouble with relative filepaths, so next 3 lines can be commented out or modified with correct path. 
my_filepath = "C:/Users/User/Desktop/CC/Markov1" #replace with your filepath
#turtle.register_shape(my_filepath + "/assets/nyan.gif")
#t.shape(MY_FILEPATH + "/assets/nyan.gif")

initial_direction = [.25, .25, .25, .25] #initial direction probability
directions = [90, 0, 270, 180]
direction_keys = {90: 0, 0: 1, 270: 2, 180: 3} #dictionary to associate direction with index in transition matrix
#direction matrix where the order is N,E,S,W
#.5 chance to go straight, .25 chance to change 90 degrees
direction_matrix = [
    [.5, .25, 0, .25], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [.25, 0, .25, .5]
    ]

initial_color = [1, 0, 0, 0, 0, 0] #initial color probability
color_keys = {"red": 0, "orange": 1, "yellow": 2, "green": 3, "blue": 4, "purple": 5} #dictionary to associate color with index in transition matrix
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#.5 chance to remain the same color, or advance one color in the rainbow
color_matrix = [
    [.5, .5, 0, 0, 0, 0], 
    [0, .5, .5, 0, 0, 0], 
    [0, 0, .5, .5, 0, 0], 
    [0, 0, 0, .5, .5, 0],
    [0, 0, 0, 0, .5, .5],
    [.5, 0, 0, 0, 0, .5],
    ]

initial_size = [.25, .25, .25, .25] #initial pensize probability
size_keys = {1: 0, 2.5: 1, 5: 2, 10: 3} #dictionary to associate size with transition matrix
sizes = [1, 2.5, 5, 10]
#.5 chance to remain the same size, .5 chance to change size one order split between options
size_matrix = [
    [.5, .5, 0, 0], 
    [.25, .5, .25, 0], 
    [0, .25, .5, .25], 
    [0, 0, .5, .5]
    ]

'''
helper function to pick a new attribute based off the markov property
@param attributes: array of attributes ex ["red", "orange", etc...]
@param matrix: the line in the corresponding attribute's transistion matrix which alligns to that specific direction, color, or size
@return new_attribute: a selected new attribute based on the markov property such as "red"
'''
def pick_attribute(attributes, matrix):
    new_attribute = np.random.choice(attributes, p=matrix)
    return new_attribute

'''
function that returns initial attributes based off of initial propabilities
@return array: an array of the first chosen direction, color, and size
'''
def markov_start():
    first_direction = np.random.choice(directions, p=initial_direction)
    first_color = np.random.choice(colors, p=initial_color)
    first_size = np.random.choice(sizes, p = initial_size)
    return [first_direction, first_color, first_size]

'''
function that returns new attributes based off of previous attributes while following the markov property
@param previous_direction: previous direction used
@param previous_color: previous color used
@param previous_size: previous size used
@return array: an array with the new direction, color, and size chosen with the markov property
'''
def markov_continue(previous_direction, previous_color, previous_size):
    new_direction = pick_attribute(directions, direction_matrix[direction_keys.get(previous_direction)])
    new_color = pick_attribute(colors, color_matrix[color_keys.get(previous_color)])
    new_size = pick_attribute(sizes, size_matrix[size_keys.get(previous_size)])
    return [new_direction, new_color, new_size]

'''
helper function that moves the turtle object as specified by the current attributes
@param direction: direction
@param color: turtle color
@param size: pensize
'''
def move(direction, color, size):
    t.setheading(direction)
    t.color(color)
    t.pensize(size)
    t.forward(random.randrange(MIN_LINE_LENGTH, MAX_LINE_LENGTH))

'''
main function to initialize values then continue the markov chain for a set number of iterations. 
This function also calls the move function to draw with turtle using the correct attributes for each iteration. 
'''
def main():
    initial_values = markov_start()
    move(initial_values[0], initial_values[1], initial_values[2])
    for i in range(ITERATIONS):
        if i == 0: # feed in initial values if this is the first iteration
            previous_values = initial_values
        new_values = markov_continue(previous_values[0], previous_values[1], previous_values[2])
        move(new_values[0], new_values[1], new_values[2])
        previous_values = new_values #set the next set of previous values to the values that were just used
    t.hideturtle()
    turtle.hideturtle()
    turtle.exitonclick()
    

if __name__ == "__main__": 
    main() 