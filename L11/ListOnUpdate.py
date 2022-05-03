from pycat.core import Window,Sprite
from random import choice
w = Window()
image = ["img/2.jpg","img/3.jpg","img/4.jpg","img/5.jpg","img/1.jpg"]
class Img(Sprite):
    def on_create(self):
        self.time = 0
        self.x = 640
        self.y = 320
        self.is_visible = False
    def on_update(self, dt):
        self.time += dt
        if self.time >= 0.5:
            w.background_image = choice(image)
            self.time = 0

w.create_sprite(Img)
w.run()
