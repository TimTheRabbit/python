from pycat.core import Window,Sprite
from random import random,randint
w = Window()
x = float(input("how fast do you want owl to fly? "))
y = float(input("how fast do you want tiger to run? "))
z = float(input("how fast do you want fireball to fly? "))

class Owl(Sprite):
    def on_create(self):
        self.image = "owl.gif"
        self.x = 0
        self.y = 500
    def on_update(self, dt):
        self.x += 3.1415926535897932384626433832795028841971693993751058209*x
        self.set_random_color()
        if self.x >= w.width:
            w.close()
            print("owl wins!")

      


class Tiger(Sprite):
    def on_create(self):
        self.image = "tiger.png"
        self.x = 0
        self.y = 180
    def on_update(self, dt):
        self.x += 3.1415926535897932384626433832795028841971693993751058209*y
        self.set_random_color()
        if self.x >= w.width:
            w.close()
            print("tiger wins!")

class Fireball(Sprite):
    def on_create(self):
        self.image = "fireball.gif"
        self.x = 0
        self.y = 180
    def on_update(self, dt):
        self.x += 8.31446261815324 * z
        self.set_random_color()
        if self.x >= w.width:
            w.close()
            print("fireball wins!")


w.create_sprite(Tiger)
w.create_sprite(Owl)
w.create_sprite(Fireball)
        
w.run()
