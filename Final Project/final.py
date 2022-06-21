from pycat.core import Window,Sprite,Color,Scheduler,KeyCode
import random





w = Window(width=1200,height=600)
class Player (Sprite):
    def on_create(self):
        self.x = 300
        self.y = 300
        self.scale = 1
        self.life = 10
        self.score = 0
        self.image = "p1.png"
        self.bn = 0
        self.speed = 2.5
        self.layer = 0
        self.time = 0
        self.changetime = 0.6
        self.guntype = 1
        self.add_tag("players")
    def power(self):
        
        if power.image == 'pointx2.png':
            self.score *= 2
            
            p1score.text = "P1 Score:" + str(self.score)
        elif power.image == 'pointx3.png':
            self.score *= 3
            
            p1score.text = "P1 Score:" + str(self.score)
        elif power.image == 'lifex2.png':
            self.life *= 2
            
            p1life.text = "P1 Life:" + str(self.life)
        elif power.image == 'life_full.png':
            self.life  = 10
            
            p1life.text = "P1 Life:" + str(self.life)
        
    def hurt(self):
        self.life -= 1
        p1life.text = "P1 Life:" + str(self.life) 
    def getpoint(self):
        self.score += 5
        p1score.text = "P1 Score:" + str(self.score)
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
        if w.is_key_down("f"):
            self.guntype += 1
        if w.is_key_down("e"):
            self.image = "p1a.png"
            if self.guntype%3 == 1:
                b1 = w.create_sprite(BulletNormal)
                b1.add_tag("p1b")
                b1.rotation = self.rotation
                b1.position = self.position
            if self.guntype %3 == 2:
                b1 = w.create_sprite(BulletSpeed)
                b1.add_tag("p1b")
                b1.rotation = self.rotation
                b1.position = self.position
            if self.guntype %3 == 0:
                b1 = w.create_sprite(BulletAuto)
                b1.add_tag("p1b")
                b1.position = self.position
            if self.changetime <= self.time:    
                self.image = "p1.png"
                self.time = 0
        if self.life <= 0:
            Scheduler.cancel_update(create_enemy)
            p2.score += 20
            p2score.text = "P2 Score:" + str(p2.score)
            w.delete_all_sprites()
            
            if self.score >= p2.score:
                w.create_label(text = "P1 win!!!",color = Color.BLUE,font_size = 100,x = 640,y = 320)
            elif self.score <= p2.score:
                w.create_label(text = "P2 win!!!",color = Color.GREEN,font_size = 100,x = 640,y = 320)
            elif self.score == p2.score:
                w.create_label(text = "Tied!!!",color = Color.RED,font_size = 100,x = 640,y = 320)
            
            

class Player2 (Sprite):
    def on_create(self):
        self.x = 900
        self.y = 300
        self.add_tag("players")
        self.scale = 1
        self.life = 10
        self.score = 0
        self.bn = 0
        self.speed = 2.5
        self.image = "p2.png"
        self.rotation = 0
        self.time = 0
        self.changetime = 0.6
        self.layer = 0
        self.guntype = 1
    def getpoint(self):
        self.score += 5
        p2score.text = "P2 Score:" + str(self.score)
    def hurt(self):
        self.life -= 1
        p2life.text = "P2 Life:" + str(self.life)
    def power(self):
        
        if power.image  == 'pointx2.png':
            self.score *= 2
            p2score.text = "P2 Score:" + str(self.score)
        elif power.image == 'pointx3.png':
            self.score *= 3
            p2score.text = "P2 Score:" + str(self.score)
        elif power.image == 'lifex2.png':
            self.life *= 2
            p2life.text = "P2 Life:" + str(self.life)
        elif power.image == 'life_full.png':
            self.life  = 10
            p2life.text = "P2 Life:" + str(self.life)
        
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
        if w.is_key_down("n"):
            self.guntype += 1
        if w.is_key_down("k"):   
            self.image = "p2a.png"
            if self.guntype%3 == 1:
                b1 = w.create_sprite(BulletNormal)
                b1.add_tag("p2b")
                b1.rotation = self.rotation+180
                b1.position = self.position
                print(self.guntype)
            if self.guntype %3 == 2:
                b1 = w.create_sprite(BulletSpeed)
                b1.add_tag("p2b")
                b1.rotation = self.rotation+180
                b1.position = self.position
                print(self.guntype)
            if self.guntype %3 == 0:
                b1 = w.create_sprite(BulletAuto)
                b1.add_tag("p2b")
                b1.position = self.position
                print(self.guntype)
            if self.changetime <= self.time:    
                    self.image = "p2.png"
                    self.time = 0
        if self.life <= 0:
            Scheduler.cancel_update(create_enemy)
            p1.score += 20
            p1score.text = "P1 Score:" + str(p1.score)
            w.delete_all_sprites()
            
            if self.score >= p1.score:
                w.create_label(text = "P2 win!!!",color = Color.GREEN,font_size = 100,x = 640,y = 320)
            elif self.score <= p1.score:
                w.create_label(text = "P1 win!!!",color = Color.BLUE,font_size = 100,x = 640,y = 320)
            elif self.score == p1.score:
                w.create_label(text = "Tied!!!",color = Color.RED,font_size = 100,x = 640,y = 320)
        


class BulletNormal(Sprite):
    def on_create(self):
        
        self.speed = 3
        self.scale = 5
        self.layer = 0
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)
        if "p1b" in self.tags:
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
        if "p2b" in self.tags:
            if self.is_touching_sprite(p1):
                self.delete()
                p1.hurt()
class BulletSpeed(Sprite):
    def on_create(self):
        self.color = Color.GREEN
        self.speed = 10
        self.layer = 0
        self.scale = 5
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)
        if "p1b" in self.tags:
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
        if "p2b" in self.tags:
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
class BulletAuto(Sprite):
    def on_create(self):
        self.color = Color.YELLOW
        self.speed = 5
        self.scale = 2.5
        self.layer = 0
        if "p1b"in self.tags:
            self.pointx = p2.x
            self.pointy = p2.y
            self.point_toward(self.pointx,self.pointy)
        if "p2b"in self.tags:
            self.point_toward_sprite(p1)
    def on_update(self, dt):        
        if self.is_touching_window_edge():
            self.delete()
        self.move_forward(self.speed)
        if "p1b" in self.tags:
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
        if "p1b" in self.tags:
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
class Enemies(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.color = Color.RED
        self.speed = 2
        self.scale = 25
        self.time = 0
        self.layer = 0
        self.shottime = 2
        self.onattack = random.randint(1,2)
    def on_update(self, dt):
        if self.onattack == 1:
            self.point_toward_sprite(p1)
        if self.onattack == 2:
            self.point_toward_sprite(p2)
        self.time += dt
        self.move_forward(self.speed)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(p1):
            p1.hurt()
            self.delete()
            
        if self.is_touching_sprite(p2):
            p2.hurt()
            self.delete()    
        if self.is_touching_any_sprite_with_tag("p1b"):
            p1.getpoint()
            print("touch p1b")
            self.delete()    
        if self.is_touching_any_sprite_with_tag("p2b"):
            p2.getpoint()
            print("touch p2b")
            self.delete()
        
        if self.time >= self.shottime:
            ebullet = w.create_sprite(EnemyBullet)
            ebullet.position = self.position
            if self.onattack == 1:
                ebullet.point_toward_sprite(p1)
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
        self.layer = 0
    def on_update(self, dt):
        
        if self.is_touching_window_edge():
            self.delete() 
        if self.point == 1:   
            self.point_toward_sprite(p1)
            if self.is_touching_sprite(p1):
                self.move_forward(-self.speed)
                self.delete()
                p1.hurt()
        if self.point == 2: 
            self.move_forward(self.speed) 
            self.point_toward_sprite(p2) 
            if self.is_touching_sprite(p2):
                self.delete()
                p2.hurt()
class Power(Sprite):
    def on_create(self):
        self.scale = 1
        self.order = ['life_full.png',
                      'lifex2.png',
                      'pointx2.png',
                      'pointx3.png']
        
        self.time = 0
        self.change_costume()
        self.is_visible = True
        

    def on_update(self, dt):
        self.time += dt
        
        
        if self.time >= 5: 
            
            self.change_costume()
        if self.is_touching_sprite(p1):
            p1.power()
            self.change_costume()
            
        if self.is_touching_sprite(p2):
            p2.power()
            self.change_costume()
            
            
            


    def change_costume(self):
        self.time = 0
        self.goto_random_position()
        self.image = random.choice(self.order)














def create_enemy():
    w.create_sprite(Enemies)
Scheduler.update(create_enemy,2)
p1 = w.create_sprite(Player)
p2 = w.create_sprite(Player2)
p1life = w.create_label(text = "P1 Life:10")
p2life = w.create_label(text = "P2 Life:10",x = 1050)
p1score = w.create_label(text = "P1 Score:0",y = 570)
p2score = w.create_label(text = "P2 Score:0",x = 1050,y = 570)
power = w.create_sprite(Power)
w.run()