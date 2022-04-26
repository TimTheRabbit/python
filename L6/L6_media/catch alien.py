from pycat.core import Window,Sprite,RotationMode,Scheduler,Player
from random import randint

w = Window(width=1200,height=600,background_image="underwater_04.png")


s_die = Player("die.wav")
s_hit = Player("hit.wav")
s_point = Player("point.wav")
s_win = Player("Cheer (1).wav")



class Ship(Sprite):
    def on_create(self):
        self.image = "saucer.png"
        self.x = 600
        self.y = 450
        self.scale = 0.3
        self.rotation = 0
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.score = 0
        self.has_won = False
        self.wintime = 0
    def on_update(self, dt):
        self.move_forward(randint(3,5))
        if self.x >= 1200:
            self.rotation = 180
        elif self.x <= 0:
            self.rotation = 0
        if not self.has_won:
            if self.score >= 50:
                s_win.play()
                self.has_won = True
                print("You win")
        else:
            self.wintime += dt
            if self.wintime >= 1:
                w.close()

class Alien(Sprite):
    def on_create(self):
        cos = randint(1,5)
        self.image = str(cos)+".png"
        self.scale = 0.3
        self.y = 50
        self.movement = 1
        self.xsp = randint(3,7)
        self.ysp = 10
        
    def on_update(self, dt):
        if self.movement == 1:
            self.ysp -= 0.5
            if self.y == 50:
                self.ysp = 10 
            self.x += self.xsp
            self.y += self.ysp
            if self.x >= 1200:
                self.delete()
        else:
            self.y += 50
            self.scale *= 0.9
            if self.y >= 600:
                self.delete()
                s_die.play()
            if self.is_touching_sprite(ship):
                self.delete()
                s_point.play()
                ship.score += 1
                print(str(ship.score))
                label_score.text  = ("score: " + str(ship.score))
        
            
        
    def on_left_click(self):
        self.movement = 2
        s_hit.play()



        
        
        
    
        



ship = w.create_sprite(Ship)
def create_alien():
   w.create_sprite(Alien) 
Scheduler.update(create_alien , 2)
label_score = w.create_label(text = "score: " + str(ship.score), x = 0 ,y = 590)
w.run()