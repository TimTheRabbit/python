from pycat.core import Window,KeyCode,Sprite
w = Window(background_image="sea.png")

class Owl(Sprite):
    def on_create(self):
        self.image = "owl.gif"
    def on_update(self, dt):
        if w.is_key_down(KeyCode.UP):
            self.rotation = 90
        if w.is_key_down(KeyCode.DOWN):
            self.rotation = 270
        if w.is_key_down(KeyCode.LEFT):
            self.rotation = 180
        if w.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
        self.move_forward(3.141592653589793238462643383279502)



w.create_sprite(Owl)
w.run()