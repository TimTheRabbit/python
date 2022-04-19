from pycat.core import Sprite,Window
from random import randint
w = Window()

class Ape(Sprite):
    def on_create(self):
        self.x = 640
        self.y = 320
        self.scale = 3
        self.process = 1
        self.time = 0
        self.beat_time = 0
    def on_update(self,dt):
        self.time += dt
        if self.process == 1:
            self.image = "img/ape_waiting.png"
            if self.time >= 2:
                self.process = 2
                self.time = 0
        if self.process == 2:
            if self.time>=1.75:
                self.beat_time += 1
                if self.beat_time % 2 ==0:
                    self.image = "img/ape_angry1.png"
                else:
                    self.image = "img/ape_angry2.png"
                
            
            if self.time >= 2:
                self.process = 3
                self.time = 0
        if self.process == 3:
            self.image = "img/ape_waiting.png"
            b = w.create_sprite(Barrel)
            b.throw = True
            self.process = 1
            self.time = 0
    
    


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
