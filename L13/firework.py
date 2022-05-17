from pycat.core import Window,Sprite
import random 
w = Window()
class Creator(Sprite):
    def on_left_click_anywhere(self):
        for _ in range(10):
            p = w.create_sprite(Particle) 
            p.position = w.mouse_position
            p.rotation = random.randint(60,120)
            p.speed = 1+random.random()
class Particle(Sprite):
    def on_create(self):
        self.speed = 0
        self.time = 0
        self.scale = 5
    def on_update(self, dt):
        self.time += dt
        self.move_forward(10)
        if self.time>0.5:
            for _ in range(36):
                s = w.create_sprite(Smoke)
                s.position = self.position
                s.rotation = random.randint(60,120)
                s.scale = 2.5
                self.delete
class Smoke(Sprite):
    def on_create(self):
        self.time = 0
        self.opacity = 50

    def on_update(self, dt):
        self.time += dt
        if self.time<=3:
            self.move_forward(1)
            self.opacity+=2
        else:
            self.y -= 2
            self.opacity -= 10 

w.create_sprite(Creator)    
w.run()            