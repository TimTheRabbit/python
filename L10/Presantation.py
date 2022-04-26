from numpy import dtype
from pycat.core import Window,Sprite,Scheduler,KeyCode,RotationMode
from random import randint

w = Window(is_sharp_pixel_scaling=True)

class Diamond(Sprite):
    def on_create(self):
        self.x = randint(60,1200)
        self.y = 640
        self.image = "img/crystal-a.png"
        self.score = 0
    def on_update(self, dt):
        self.y -= 5
        if self.y <= 50:
            self.delete()
        if self.is_touching_sprite(player):
            self.score += 1
            self.delete()
class Player(Sprite):
    def on_create(self):
        self.x = 640
        self.y = 320
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.image = "img/STOP.png"
        self.scale = 2.5
    
    def on_update(self,dt):
        if w.is_key_down(KeyCode.LEFT):
            Scheduler.wait(0,self.on_left)

    def on_left(self):
        self.rotation = 180
        self.x -= 20
        print(self.x)
        if w.is_key_down(KeyCode.RIGHT):
            Scheduler.wait(0,self.on_right)
        if w.is_key_down(KeyCode.DOWN):
            Scheduler.wait(0,self.on_slide)
    def on_right(self):
        self.rotation = 0
        self.x += 5
        print(self.x)
        if w.is_key_down(KeyCode.LEFT):
            Scheduler.wait(0,self.on_left)
        if w.is_key_down(KeyCode.DOWN):
            Scheduler.wait(0,self.on_slide)
    def on_slide(self):
        self.image = "img/SLIDE2.png"
        self.move_forward(3)
        if w.is_key_down(KeyCode.LEFT):
            Scheduler.wait(0,self.on_left)
        if w.is_key_down(KeyCode.RIGHT):
            Scheduler.wait(0,self.on_right)

WAIT=1
ANGRY1 = 2
ANGRY2 = 3
THROW = 4
class Enemy(Sprite):
    def on_create(self):
        self.x = 640
        self.y = 50
        self.image = "img/frank-a.png"
        self.scale = 0.2
        self.time = 0
        self.repeat = 0

        self.state = WAIT
    def on_update(self, dt):
        if self.state == WAIT:
            self.wait(dt)
        if self.state == ANGRY1:
            self.angry1(dt)
        if self.state == ANGRY2:
            self.angry2(dt)
        if self.state == THROW:
            self.throw(dt)
        
    def wait(self,dt):
        self.time += dt
        if self.time >= 2:
            self.image = "img/frank-c.png"
            self.time = 0
            self.state = ANGRY1
    def angry1(self ,dt):
        self.time += dt
        if self.time >= 0.5:
            self.image = "img/frank-c2.png"
            self.state = ANGRY2
    def angry2(self ,dt):
        self.time += dt
        if self.time >= 1:
            if self.repeat >= 2: 
                self.image = "img/frank-d.png"
                self.state = THROW
            else: 
                self.image = "img/frank-c.png"
                self.repeat += 1
                self.state = ANGRY1
    def throw(self,dt):
        self.time += dt
        if self.time >= 2:
            self.state = WAIT
            self.time =0

    



def create_diamond():
    w.create_sprite(Diamond)

Scheduler.update(create_diamond,1)
player = w.create_sprite(Player)
enemy = w.create_sprite(Enemy)

w.run()