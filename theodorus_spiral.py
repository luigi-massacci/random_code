#####################################################################################
## Draws a spiral of Theodorus https://en.wikipedia.org/wiki/Spiral_of_Theodorus
## 12/03/2018
#####################################################################################
 

from tkinter import *
import math
import time
import tkinter as tk
import random

random.seed()
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000

root = Tk()
canvas = Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="#ffffcc")
canvas.pack()

center = 500
zoom = 50

points = [
        [center, center],
        [center + 1*zoom, center],
        [center+1*zoom, center-1*zoom],
]

def draw_triag(points, color="blue", border=''):
    canvas.create_polygon(points, fill=color, outline=border)

palette = [23, 38, 160]
color = '#%02x%02x%02x' % (palette[0], palette[1], palette[2])

draw_triag(points, color=color)
root.update()

tot_angles = 45


i = 3
while(True):
    points[1][0] = points[2][0]
    points[1][1] = points[2][1]

    angle = math.asin(1/math.sqrt(i)) * (180 / math.pi)
    tot_angles =  tot_angles + angle
    # print(angle)

    if tot_angles < 90:
        alpha = math.fabs(90 - tot_angles)
        y = center - (math.cos(alpha*math.pi/180)*math.sqrt(i)) * zoom
        x = center + (math.sin(alpha*math.pi/180)*math.sqrt(i)) * zoom
        # print(x-500)
    elif tot_angles < 180:
        alpha = math.fabs(180 - tot_angles)
        y = center - (math.sin(alpha*math.pi/180)*math.sqrt(i)) * zoom
        x = center - (math.cos(alpha*math.pi/180)*math.sqrt(i)) * zoom
    elif tot_angles < 270:
        alpha = math.fabs(270 - tot_angles)
        y = center + math.cos(alpha*math.pi/180)*math.sqrt(i) * zoom
        x = center - math.sin(alpha*math.pi/180)*math.sqrt(i) * zoom
    elif tot_angles < 360:
        alpha = math.fabs(360 - tot_angles)
        y = center + math.sin(alpha*math.pi/180)*math.sqrt(i) * zoom
        x = center + math.cos(alpha*math.pi/180)*math.sqrt(i) * zoom
    elif tot_angles > 360:
        alpha = math.fabs(360 - tot_angles)
        y = center - math.sin(alpha*math.pi/180)*math.sqrt(i) * zoom
        x = center + math.cos(alpha*math.pi/180)*math.sqrt(i) * zoom
        tot_angles = alpha

    points[2][0] = x
    points[2][1] = y

    for p in range(0, 3):
        palette[p] = random.randint(0, 255)

    # print(palette)
    color = '#%02x%02x%02x' % (palette[0], palette[1], palette[2])
    # print(color)
    draw_triag(points, color=color)
    time.sleep(0.5)
    root.update()

    i = i + 1



root.mainloop()
