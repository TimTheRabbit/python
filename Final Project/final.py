from pickle import FALSE, TRUE
from pycat.core import Window,Sprite,Color,Scheduler,KeyCode
import random


w = Window(width=1200,height=600)
class Player (Sprite):
    def on_create(self):
        self.x = 300
        self.y = 300
        self.scale = 25
        self.life = 3
        self.score = 0
        self.color = Color.CYAN
        self.bn = 0
        self.speed = 3
        self.is_move = FALSE
    def on_update(self, dt):
        if self.is_move == TRUE:
            self.move_forward(self.speed)
        if w.is_key_pressed("w"):
            if self.rotation < 90:
                self.rotation -= 10
            elif 90 < self.rotation <= 270:
                self.rotation += 10
            elif self.rotation > 270:
                self.rotation -= 10
        if w.is_key_pressed("s"):
            if self.rotation < 90:
                self.rotation += 10
            elif 90 < self.rotation <= 270:
                self.rotation -= 10
            elif self.rotation > 270:
                self.rotation += 10
        if w.is_key_pressed("a"):
            if self.rotation <= 0:
                self.rotation -= 10
            elif 0 < self.rotation <= 180:
                self.rotation += 10
            elif self.rotation > 180:
                self.rotation -= 10
        if w.is_key_pressed("d"):
            if self.rotation < 0:
                self.rotation += 10
            elif 0 < self.rotation <= 180:
                self.rotation -= 10
            elif self.rotation >= 180:
                self.rotation += 10
        if w.is_key_pressed("x"):
            self.goto_random_position()
        if w.is_key_pressed("t"):
            self.is_move = TRUE
        if w.is_key_pressed("f"):
            self.is_move = FALSE

        if w.is_key_down("e"):
            b1 = w.create_sprite(Bullet1)
            b1.type = "p1"
            b1.rotation = self.rotation
            b1.position = self.position

class Player2 (Sprite):
    def on_create(self):
        self.x = 900
        self.y = 300
        self.scale = 25
        self.life = 3
        self.score = 0
        self.color = Color.GREEN
        self.bn = 0
        self.is_move = FALSE
        self.speed = 3
        self.rotation = 180
    def on_update(self, dt):
        if self.is_move == TRUE:
            self.move_forward(self.speed)
        if w.is_key_pressed(KeyCode.UP):
            if self.rotation < 90:
                self.rotation -= 10
            elif 90 < self.rotation <= 270:
                self.rotation += 10
            elif self.rotation > 270:
                self.rotation -= 10
        if w.is_key_pressed(KeyCode.DOWN):
            if self.rotation < 90:
                self.rotation += 10
            elif 90 < self.rotation <= 270:
                self.rotation -= 10
            elif self.rotation > 270:
                self.rotation += 10
        if w.is_key_pressed(KeyCode.LEFT):
            if self.rotation <= 0:
                self.rotation -= 10
            elif 0 < self.rotation <= 180:
                self.rotation += 10
            elif self.rotation > 180:
                self.rotation -= 10
        if w.is_key_pressed(KeyCode.RIGHT):
            if self.rotation < 0:
                self.rotation += 10
            elif 0 < self.rotation <= 180:
                self.rotation -= 10
            elif self.rotation >= 180:
                self.rotation += 10
        if w.is_key_pressed("m"):
            self.goto_random_position()
        if w.is_key_pressed("j"):
            self.is_move = TRUE
        if w.is_key_pressed("o"):
            self.is_move = FALSE
        if w.is_key_down("k"):
            b1 = w.create_sprite(Bullet1)
            b1.type = "p2"
            b1.rotation = self.rotation
            b1.position = self.position

class Bullet1(Sprite):
    def on_create(self):
        self.type = "x"
        if self.type == "p1":
            self.add_tag("bf1")
            self.color = Color.CYAN
        if self.type == "p2":
            self.add_tag("bf2")
            self.color = Color.GREEN
        self.speed = 2.5
        self.scale = 5
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)

















b1 = w.create_sprite(Bullet1)
p = w.create_sprite(Player)
p2 = w.create_sprite(Player2)
w.run()