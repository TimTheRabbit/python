from pycat.core import Window,Sprite
from random import randint
w = Window()
class Particle (Sprite):
    def on_create(self):
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.set_random_color()
        self.scale = randint(3,8)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()






for _ in range(100):    
    w.create_sprite(Particle)
w.run()