from turtle import *
import colorgram

#We are writing this code only to extract colors
# rgb_colors = []
# colors = colorgram.extract("unnamed.jpg", 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


#Copy the list after running your code and paste it in the program

import turtle as t
from turtle import Screen
import colorgram
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (239, 245, 241), (236, 239, 244), (150, 75, 50), (223, 201, 135), (53, 94, 124), (169, 153, 43), (138, 31, 20), (134, 163, 184), (197, 92, 73), (48, 121, 88), (71, 44, 36), (145, 178, 149), (15, 98, 71), (162, 142, 158), (233, 176, 164), (104, 76, 79), (55, 45, 49), (36, 60, 74), (183, 205, 171), (19, 86, 90), (144, 18, 21), (83, 148, 129), (36, 67, 93), (13, 72, 63), (163, 102, 105), (179, 192, 206), (107, 126, 153)]

t.colormode(255) #0,255
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
