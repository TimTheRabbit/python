from pickle import FALSE, TRUE
from pycat.core import Window,Sprite,Color,Scheduler,KeyCode
import random


w = Window(width=1200,height=600)
class Player (Sprite):
    def on_create(self):
        self.x = 300
        self.y = 300
        self.scale = 1
        self.life = 3
        self.score = 0
        self.image = "p1.png"
        self.bn = 0
        self.speed = 3
        self.time = 0
        self.changetime = 0.6
        self.guntype = 1
        
    def on_update(self, dt):
        self.time += dt
        if w.is_key_pressed("w"):
           self.move_forward(self.speed) 
        if w.is_key_pressed("s"):
            self.move_forward(-self.speed)
        if w.is_key_pressed("a"):
            self.rotation += 5
        if w.is_key_pressed("d"):
            self.rotation -= 5
        if w.is_key_pressed("q"):
            self.goto_random_position()
        if w.is_key_pressed("f"):
            self.guntype += 1
        if w.is_key_down("e"):
            self.image = "p1a.png"
            if self.guntype%2 == 1:
                b1 = w.create_sprite(BulletNormal)
                b1.type = "p1"
                b1.rotation = self.rotation
                b1.position = self.position
            if self.guntype %2 == 0:
                b1 = w.create_sprite(BulletSpeed)
                b1.type = "p1"
                b1.rotation = self.rotation
                b1.position = self.position
            if self.changetime <= self.time:    
                self.image = "p1.png"
                self.time = 0
            

class Player2 (Sprite):
    def on_create(self):
        self.x = 900
        self.y = 300
        self.scale = 1
        self.life = 3
        self.score = 0
        self.bn = 0
        self.speed = 3
        self.image = "p2.png"
        self.rotation = 0
        self.time = 0
        self.changetime = 0.6
        self.guntype = 1
    def on_update(self, dt):   
        self.time += dt    
        if w.is_key_pressed(KeyCode.UP):
            self.move_forward(-self.speed)
        if w.is_key_pressed(KeyCode.DOWN):
            self.move_forward(self.speed)
        if w.is_key_pressed(KeyCode.LEFT):
            self.rotation += 5 
        if w.is_key_pressed(KeyCode.RIGHT):
            self.rotation -= 5
        if w.is_key_pressed("m"):
            self.goto_random_position()
        if w.is_key_pressed("n"):
            self.guntype += 1
        if w.is_key_down("k"):   
            self.image = "p2a.png"
            if self.guntype%2 == 1:
                b1 = w.create_sprite(BulletNormal)
                b1.type = "p2"
                b1.rotation = self.rotation
                b1.position = self.position
            if self.guntype %2 == 0:
                b1 = w.create_sprite(BulletSpeed)
                b1.type = "p2"
                b1.rotation = self.rotation
                b1.position = self.position
                if self.changetime <= self.time:    
                    self.image = "p2.png"
                    self.time = 0

class BulletNormal(Sprite):
    def on_create(self):
        self.type = "x"
        self.add_tag("bullet")
        self.speed = 2.5
        self.scale = 5
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)
        if self.type == "p1":
            if self.is_touching_sprite(p2):
                self.delete()
                p2.life -= 1
        if self.type == "p2":
            if self.is_touching_sprite(p):
                self.delete()
                p.life -= 1
class BulletSpeed(Sprite):
    def on_create(self):
        self.type = "x"
        self.add_tag("bullet")
        self.color = Color.GREEN
        self.speed = 2.5
        self.scale = 10
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)
        if self.type == "p1":
            if self.is_touching_sprite(p2):
                self.delete()
                p2.life -= 1
        if self.type == "p2":
            if self.is_touching_sprite(p):
                self.delete()
                p.life -= 1
class Enemies(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.color = Color.RED
        self.speed = 2
        self.scale = 25
        self.time = 0
        self.shottime = 2
        self.onattack = random.randint(1,2)
    def on_update(self, dt):
        if self.onattack == 1:
            self.point_toward_sprite(p)
        if self.onattack == 2:
            self.point_toward_sprite(p2)
        self.time += dt
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(p):
            self.delete()
            p.life -= 1
            p.score += 1
        if self.is_touching_sprite(p2):
            self.delete()
            p2.life -= 1
            p2.score += 1
        if self.is_touching_any_sprite_with_tag("bullet"):
            self.delete()
            p.score += 1
        if self.time >= self.shottime:
            ebullet = w.create_sprite(EnemyBullet)
            ebullet.position = self.position
            if self.onattack == 1:
                ebullet.point_toward_sprite(p)
                ebullet.point = 1
                self.onattack = 2
            if self.onattack == 2:
                ebullet.point_toward_sprite(p2)
                ebullet.point = 2
                self.onattack = 1
            self.time = 0
class EnemyBullet(Sprite):
    def on_create(self):
        self.point = 0
        self.scale = 5
        self.speed = 6
    def on_update(self, dt):
        
        if self.is_touching_window_edge():
            self.delete() 
        if self.point == 1:   
            self.point_toward_sprite(p)
            if self.is_touching_sprite(p):
                self.move_forward(-self.speed)
                self.delete()
                p.life -= 1
        if self.point == 2: 
            self.move_forward(self.speed) 
            self.point_toward_sprite(p2) 
            if self.is_touching_sprite(p2):
                self.delete()
                p2.life -= 1
















def create_enemy():
    w.create_sprite(Enemies)
Scheduler.update(create_enemy,2)
p = w.create_sprite(Player)
p2 = w.create_sprite(Player2)
w.run()