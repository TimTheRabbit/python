from pycat.core import Window,Sprite
w = Window()
image = ["img/2.jpg","img/3.jpg","img/4.jpg"]
w.background_image = "img/1.jpg"

class Button(Sprite):
    def on_create(self):
        self.x = 350
        self.y = 50
        self.scale = 100
        self.set_random_color()
    def on_left_click(self):
        w.background_image = image[0]
class Button2(Sprite):
    def on_create(self):
        self.x = 700
        self.y = 50
        self.scale = 100
        self.set_random_color()
    def on_left_click(self):
        w.background_image = image[1]
class Button3(Sprite):
    def on_create(self):
        self.x = 1050
        self.y = 50
        self.scale = 100
        self.set_random_color()
    def on_left_click(self):
        w.background_image = image[2]



w.create_sprite(Button)
w.create_sprite(Button2)
w.create_sprite(Button3)
w.run()