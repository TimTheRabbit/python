from pycat.core import Window,Sprite
from random import randint
w = Window()
class Particle (Sprite):
    def on_create(self):
        self.add_tag("particle")
        self.goto_random_position()
        self.rotation = randint(0,360)
        self.set_random_color()
        self.scale = randint(3,8)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
class Button(Sprite):
    def on_create(self):
        self.x = 200
        self.y = 200
        self.scale = 150
    def on_left_click(self):
        p_lst = w.get_sprites_with_tag("particle")
        for p in p_lst:
            p.color = (255,255,0)





w.create_sprite(Button)
for _ in range(100):    
    w.create_sprite(Particle)
w.run()