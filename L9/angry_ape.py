from pycat.core import Sprite,Window,Scheduler
from random import randint
w = Window()

class Ape(Sprite):
    def on_create(self):
        self.x = 640
        self.y = 320
        self.scale = 3
        self.wait()
    def wait(self):
        self.image = "img/ape_waiting.png"
        Scheduler.wait(1,self.change)
    
    def change(self):
        self.image = "img/ape_angry1.png"
        Scheduler.wait(0.5,self.angry)
    def angry(self):
        self.image = "img/ape_angry2.png"
        Scheduler.wait(1,self.throw)
    def throw(self):
        self.image = "img/ape_waiting.png"
        for _ in range(5):
            barrel=w.create_sprite(Barrel)   
        barrel.throw = True
        Scheduler.wait(1,self.wait)

    


class Barrel (Sprite):
    def on_create(self):
        self.throw = False
        self.x = ape.x
        self.y = ape.y
        self.is_visible = False
        self.angle = 45
        self.scale = 2
        self.image = "img/barrel1.png"
    def on_update(self, dt):
        if self.throw == True:
            self.angle = randint(45,135)
            self.rotation = self.angle
            self.is_visible = True
            self.move_forward(5)
        if self.x >= w.width:
            self.delete()
        elif self.x <= 0:
            self.delete()
        elif self.y >= w.height:
            self.delete()
        elif self.y <= 0:
            self.delete()



ape = w.create_sprite(Ape)


w.run()
