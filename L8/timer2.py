from numpy import record
from pycat.core import Window,Sprite,Color,Label

w = Window(width=1200,height=600)

class ButtonStart(Sprite):
    def on_create(self):
        self.x = 300
        self.y = 200
        self.scale = 50
        self.color = Color.CYAN
    def on_left_click(self):
        timer.is_active = not timer.is_active
class ButtonReset(Sprite):
    def on_create(self):
        self.x = 500
        self.y = 200
        self.scale = 50
        self.color = Color.RED
    def on_left_click(self):
        timer.time = 0
        timer.text = str(timer.time)
class Timer(Label):
    def on_create(self):
        self.x = 200
        self.y = 500
        self.time = 0
        self.is_active = False
    def on_update(self, dt: float):
        if self.is_active:
            self.time += dt
            self.text = str(round(self.time,3))


class Recorder(Label):
    def on_create(self):
        self.x = 400
        self.y = 400
        self.num = 1

class Recordhandle(Sprite):
    def on_create(self):
        self.x = 800
        self.y = 200
        self.scale = 50
        self.color = Color.GREEN
    def on_left_click(self):
        record.text = str(record.num)+":"+str(round(timer.time,3))+"sec.\n"
        record.num += 1
        
        












w.create_sprite(ButtonReset)
w.create_sprite(ButtonStart)
w.create_sprite(Recordhandle)
timer = w.create_label(Timer)
record = w.create_label(Recorder)

w.run()