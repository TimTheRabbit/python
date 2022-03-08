from cmath import pi
from pycat.core import Window,KeyCode,Sprite
from pycat.core import RotationMode
w = Window(background_image="sea.png")


class Owl(Sprite):
    def on_create(self):
        self.image = "owl.gif"
        self.x = 0
        self.y = 640
        self.live = 20
        self.score = 0        
        self.rotation_mode = RotationMode.RIGHT_LEFT
    def on_update(self, dt):
        
        if w.is_key_down(KeyCode.UP):
            self.rotation = 90
        if w.is_key_down(KeyCode.DOWN):
            self.rotation = 270
        if w.is_key_down(KeyCode.LEFT):
            self.rotation = 180
        if w.is_key_down(KeyCode.RIGHT):
            self.rotation = 0
        if self.is_touching_any_sprite_with_tag("obstacle"):
            print(self.live)
            if self.live == 0:
                print("You Lose!")
                w.close()
            else:
                self.live -= 1
                label_live.text =  "life: " + str(self.live)
                self.x = 0
        self.move_forward(pi)
        if self.is_touching_any_sprite_with_tag("tiger"):
            print(self.score)
            if self.score == 30:
                print("You Win!")
                w.close()
            else:
                self.score += 1
                label_score.text =  "score: " + str(self.score)
                self.x = 0
class Obj1(Sprite):
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.image = "ork1.png"
        self.x = 1260
        self.y=640
        self.scale = 0.5
        self.add_tag("obstacle")
    def on_update(self, dt):
        if self.x >= 1260:
            self.rotation = 180
        if self.x <= 340:
            self.rotation = 0
        self.move_forward(pi)
class Obj2(Sprite):
    def on_create(self):
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.image = "tiger.png"
        self.goto_random_position()
        self.scale = 0.2
        self.add_tag("tiger")
    def on_update(self, dt):
        if self.x >= 1260:
            self.rotation = 180
        if self.x <= 640:
            self.rotation = 0
        self.move_forward(pi)



owl = w.create_sprite(Owl)
w.create_sprite(Obj1)
w.create_sprite(Obj2)
label_score = w. create_label(text = "score: " + str(owl.score), x = 0, y = 600)
label_live = w. create_label(text = "life: " + str(owl.live), x = 0 ,y = 630)
w.run()