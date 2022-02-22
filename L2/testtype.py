from pycat.core import Window
w=Window()
sprite1=w.create_sprite()
sprite1.x=90
sprite1.y=3.14159265358979323846264338
sprite1.is_visible=True
msg=("hello")
print(type(msg))
print(type(sprite1.x))
print(type(sprite1.y))
print(type(w))
print(type(sprite1.is_visible))
print(type(Window))
print(type(sprite1))
w.run()