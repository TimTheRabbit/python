from pycat.core import Window,Sprite,KeyCode,RotationMode,Scheduler
from random import random,randint

w = Window(width=1200,height=600,background_image="img/beach_03.png")

class Player(Sprite):
    def on_create(self):
        self.add_tag("cat")
        self.image = "img/cat.png"
        self.x = 600
        self.life = 20
        self.score = 0
        self.y = 50
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.speed = 5
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -= self.speed
            self.rotation = 180
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x += self.speed
            self.rotation = 0
        if self.life <= 0:
            w.close()
            print("You lose!")
        if self.is_touching_any_sprite_with_tag("tri"):
            self.life -= 1
            label_life.text  = ("life: " + str(self.life))
        if self.is_touching_any_sprite_with_tag("gem"):
            self.score += 1
            label_score.text  = ("score: " + str(self.score))
        if self.score >= 50:
            w.close()
            print("You win!")
        if self.is_touching_any_sprite_with_tag("power"):
            self.speed += 0.5 
            
class Triangle(Sprite):
    def on_create(self):
        self.y = 600
        self.add_tag("tri")
        self.x = randint(0,1200)
        self.image = "img/gem_shiny01.png"
        self.scale = 0.3
        
    def on_update(self, dt):
        self.y -= 5
        if self.is_touching_any_sprite_with_tag("cat"):
            self.delete()
        if self.y <= 20:
            self.delete()
        
class Gem(Sprite):
    def on_create(self):
        self.y = 600
        self.add_tag("gem")
        self.x = randint(0,1200)
        self.costume = randint(0,3)
        if self.costume == 0:
            self.image = "img/gem_shiny02.png"
        if self.costume == 1:
            self.image = "img/gem_shiny03.png"
        if self.costume == 2:
            self.image = "img/gem_shiny04.png"
        if self.costume == 3:
            self.image = "img/gem_shiny05.png"
        self.scale = 0.3
        
    def on_update(self, dt):
        self.y -= 5
        if self.is_touching_any_sprite_with_tag("cat"):
            self.delete()
        if self.y <= 20:
            self.delete()

class Timer(Sprite):
    def on_create(self):
        self.is_visible = False
        self.wait_time = randint(1,3)
        self.current_time = 0
    def on_update(self, dt):
        self.current_time += dt
        if self.current_time >= self.wait_time:
            self.current_time = 0
            self.wait_time = randint(1,5)
            if randint(1,3) == 1:
                create_gem()
            elif randint == 2:    
                create_gem()
            elif randint == 3:    
                create_tri()
            elif randint == 4:    
                create_tri()
            else:
                create_power()
                
class Power(Sprite):
    def on_create(self):
        self.y = 600
        self.add_tag("power")
        self.x = randint(0,1200)
        self.image = "img/speed_powerup.png"
        self.scale = 0.3
    def on_update(self, dt):
        self.y -= 5
        if self.is_touching_any_sprite_with_tag("cat"):
            self.delete()
        if self.y <= 20:
            self.delete()
        
        
def create_tri():
    w.create_sprite(Triangle)   
def create_gem():
    w.create_sprite(Gem)
def create_power():
    w.create_sprite(Power)
player = w.create_sprite(Player)
w.create_sprite(Timer)

label_score = w.create_label(text = "score: " + str(player.score), x = 0, y = 560)
label_life = w.create_label(text = "life: " + str(player.life), x = 0 ,y = 590)
label_life.color = (0,0,0)
label_score.color = (0,0,0)
w.run()