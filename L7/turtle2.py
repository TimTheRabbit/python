from tkinter import S
from pycat.core import Window,Sprite,Scheduler
from pycat.extensions.turtle import Turtle

w = Window()
t = w.create_sprite(Turtle)
t.x = 60
t.y = 0
t.rotation = 0
t.set_random_color()
def draw_a_regular_polygon(length,side):
    r = 360/side
    for _ in range(side):
        t.move_forward(length)
        t.rotation += r

#def drawer():
for _ in range(20):
    for _ in range(20):
        draw_a_regular_polygon(50,4)
        t.rotation += 30
        t.goto_random_position()
for _ in range(20):
    for _ in range(20):
        draw_a_regular_polygon(50,3)
        t.rotation += 30
        t.goto_random_position()



#Scheduler.update(drawer)

w.run()