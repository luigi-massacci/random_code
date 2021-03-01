##############################################################################
## Fails to draw a spiral of Theodorus, but the result is rather good looking
## 12/03/2018
##############################################################################


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

points = [
        [500, 500],
        [600, 500],
        [600, 400],
]

def draw_triag(points, color="blue", border=''):
    canvas.create_polygon(points, fill=color, outline=border)

palette = [0, 0, 0]
color = '#%02x%02x%02x' % (palette[0], palette[1], palette[2])

draw_triag(points, color=color)
root.update()

tot_angles = 45

zoom = 200

i = 3
while(True):
    points[1][0] = points[2][0]
    points[1][1] = points[2][1]

    angle = math.asin(1/math.sqrt(i)) * (180 / math.pi)
    tot_angles += angle


    if angle < 90:
        alpha = 90 - tot_angles
        # print(alpha)
        y = center - math.cos(alpha)*math.sqrt(i) * zoom
        x = center + math.sin(alpha)*math.sqrt(i) * zoom
    elif angle < 180:
        alpha = 180 - tot_angles
        y = center - math.sin(alpha)*math.sqrt(i) * zoom
        x = center - math.cos(alpha)*math.sqrt(i) * zoom
    elif angle < 270:
        alpha = 180 - tot_angles
        y = center - math.cos(alpha)*math.sqrt(i) * zoom
        x = center + math.sin(alpha)*math.sqrt(i) * zoom
    elif angle < 360:
        alpha = 360 - tot_angles
        y = center - math.sin(alpha)*math.sqrt(i) * zoom
        x = center - math.cos(alpha)*math.sqrt(i) * zoom
    elif angle > 360:
        alpha = -(360 - tot_angles)
        y = center + math.sin(alpha)*math.sqrt(i) * zoom
        x = center - math.cos(alpha)*math.sqrt(i) * zoom
        tot_angles = alpha

    points[2][0] = x
    points[2][1] = y

    for p in range(0, 3):
        palette[p] = random.randint(0, 255)

    # print(palette)
    color = '#%02x%02x%02x' % (palette[0], palette[1], palette[2])
    # print(color)
    draw_triag(points, color=color)
    time.sleep(0.1)
    root.update()

    ++i



root.mainloop()
