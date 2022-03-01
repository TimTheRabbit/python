from pycat.core import Window,Sprite,KeyCode
w = Window()
class Owl(Sprite):
    def on_create(self):
        self.image = "owl.gif"
        self.x = 0
        self.y = 500
    def on_update(self, dt):
        if w.is_key_down(KeyCode.O):
            self.x += 10
        self.set_random_color()
        if self.x >= w.width:
            w.close()
            print("owl wins!")
class Fireball(Sprite):
    def on_create(self):
        self.image = "fireball.gif"
        self.x = 0
        self.y = 180
    def on_update(self, dt):
        if w.is_key_down(KeyCode.F):
            self.x += 10
        self.set_random_color()
        if self.x >= w.width:
            w.close()
            print("fireball wins!")
w.create_sprite(Owl)
w.create_sprite(Fireball)
w.run()