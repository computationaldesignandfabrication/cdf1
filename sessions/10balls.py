import random, pygame as pg, pygamebg
import math
(width, height) = (500, 300)
canvas = pygamebg.open_window(width, height, "Balls")

balls = []
timet=0
for i in range(10):
    r = 30
    x = i*50 +30
    y = 150
    color = (255-i*5,255-i*4,255-i*6)
    freq = i+1
    dx, dy = 0, 0
    balls.append((x, y, dx, dy, r, color, freq))
    
def new_frame():
    global balls
    global timet
    for i in range(10):
        x, y, dx, dy, r, color, freq = balls[i]
        timet=timet+1
        dy=((i+5)/2)*math.cos(freq*timet/360)
        (x, y) = (x + dx, y + dy)
        balls[i] = (x, y, dx, dy, r, color, freq)
    canvas.fill(pg.Color("darkgray"))
    for x, y, dx, dy, r, color, freq in balls:
        pg.draw.circle(canvas, color, (x, y), r, 12-freq)

pygamebg.frame_loop(50, new_frame)