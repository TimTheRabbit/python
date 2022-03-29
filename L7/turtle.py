from pycat.core import Window,Sprite
from pycat.extensions.turtle import Turtle

w = Window()
t = w.create_sprite(Turtle)
t.x = 5
t.y = 320
t.rotation = 0
t.set_random_color()
for i in range(3):
    t.move_forward(100)
    t.turn_right(120)

w.run()