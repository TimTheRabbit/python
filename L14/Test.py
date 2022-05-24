from pycat.core import Window,Sprite,Color,Scheduler
import random
w = Window()
class Player (Sprite):
    def on_create(self):
        self.goto_random_position()
        self.scale = 25
        self.xsp = 10
        self.ysp = 10
        self.life = 3
        self.score = 0
        self.color = Color.CYAN
        self.bn = 0
        l.text = "48"
    def on_update(self, dt):
        if w.is_key_pressed('w'):
            self.y += self.ysp
        if w.is_key_pressed('s'):
            self.y -= self.ysp
        if w.is_key_pressed('a'):
            self.x -= self.xsp
        if w.is_key_pressed('d'):
            self.x += self.xsp
        if w.is_key_pressed('r'):
            self.goto_random_position()

    def on_left_click_anywhere(self):
        if self.bn <= 45:
            w.create_sprite(Player_B)
            w.create_sprite(Player_B2) 
            w.create_sprite(Player_B3)
            w.create_sprite(Player_B4)
            self.bn += 4
            l.text = str(45-self.bn)
            
    

class Player_B(Sprite):
    def on_create(self):
        self.add_tag("bullet")
        self.speed = 2.5
        self.scale = 5
        self.color = Color.WHITE
        self.position = p.position
        self.point_toward_mouse_cursor()
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
            p.bn-=1
            l.text = str(45-p.bn)
        self.move_forward(self.speed)
class Player_B2(Sprite):
    def on_create(self):
        self.add_tag("bullet")
        self.speed = 2.5
        self.scale = 5
        self.color = Color.AMBER
        self.position = p.position
        self.rotation = random.randint(0,360)
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
            p.bn-=1
            l.text = str(45-p.bn)
        self.move_forward(self.speed) 
class Player_B3(Sprite):
    def on_create(self):
        self.add_tag("bullet")
        self.speed = 15
        self.scale = 5
        self.color = Color.GREEN
        self.position = p.position
        self.point_toward_mouse_cursor()
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
            p.bn-=1
            l.text = str(45-p.bn)
        self.move_forward(self.speed)  
class Player_B4(Sprite):
    def on_create(self):
        self.add_tag("bullet")
        self.speed = 5
        self.scale = 2
        self.opacity = 5
        self.color = Color.BLUE
        self.position = p.position
        self.rotation = random.randint(0,360)
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
            p.bn-=1
            l.text = str(45-p.bn)
        self.move_forward(self.speed)
class Enemies(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.color = Color.RED
        self.speed = 2
        self.scale = 25
        self.point_toward_sprite(p)
        self.time = 0
        self.shottime = 2
    def on_update(self, dt):
        self.time += dt
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(p):
            self.delete()
            p.life -= 1
        if self.is_touching_any_sprite_with_tag("bullet"):
            self.delete()
            p.score += 1
        if self.time >= self.shottime:
            bullet = w.create_sprite(EnemyBullet)
            bullet.position = self.position
            bullet.point_toward_sprite(p)
            self.time = 0
class EnemyBullet(Sprite):
    def on_create(self):
        self.scale = 5
        self.speed = 6
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(p):
            self.delete()
            p.life -= 1



def create_enemies():
    w.create_sprite(Enemies)

Scheduler.update(create_enemies,2)
l = w.create_label(x = 150,y = 500)
p = w.create_sprite(Player)
w.run()