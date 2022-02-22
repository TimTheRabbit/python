from pycat.core import Window,Sprite
from random import random,randint
w=Window()

class Owl(Sprite):
    def on_create(self):
        self.image = "owl.gif"
        self.set_random_color()
        self.goto_random_position()
        self.number = random()*10000
        self.scale = random()*10
        self.rotation = random()*360
        self.opacity = random()*55
        self.layer = randint(0,2)
class Tiger(Sprite):
    def on_create(self):
        self.image = "tiger.png"
        self.set_random_color()
        self.goto_random_position()
        self.number = random()*10000
        self.scale = random()*10
        self.rotation = random()*360
        self.opacity = random()*55
        self.layer = randint(0,2)

for i in range(50):
    owl=w.create_sprite(Owl)
    tiger=w.create_sprite(Tiger)
print(owl.number)
print(tiger.number)
w.run()