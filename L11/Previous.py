from pycat.core import Window,Sprite
w = Window()
image = ["img/1.jpg","img/2.jpg","img/3.jpg","img/4.jpg","img/5.jpg","img/6.jpg","img/7.jpg","img/8.jpg","img/9.jpg","img/10.jpg","img/bird.jpg"]


class Next(Sprite):
    def on_create(self):
        self.x = 1100
        self.y = 50
        self.image = "img/arrow1-a.png"
        self.state = 0
        self.pic = -1
    def on_left_click(self):
        self.state+=1
        self.pic = self.state%len(image)
        w.background_image = image[self.pic]
        
class Previous(Sprite):
    def on_create(self):
        self.x = 140
        self.y = 50
        self.image = "img/arrow1-b.png"
        next.state = 0
        next.pic = -1
    def on_left_click(self):
        next.state-=1
        next.pic = next.state%len(image)
        w.background_image = image[next.pic]
        

next = w.create_sprite(Next)
w.create_sprite(Previous)
w.run()       