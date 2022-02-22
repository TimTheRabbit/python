from pycat.core import Window
window = Window()

sprite1 = window.create_sprite()
sprite2 = window.create_sprite()
sprite3 = window.create_sprite()
sprite1.is_visible = False
sprite2.is_visible = False
sprite3.is_visible = False


s = input("What sprite do you wnt to see,fireball,owl or elephant? ")
number = input("How many?(1-3) ")
if s == "fireball":
    sprite1.image = "fireball.gif"
    sprite2.image = "fireball.gif"
    sprite3.image = "fireball.gif"
    if  number == "1":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
    if  number == "2":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
    if  number == "3":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
        x3 = int(input("Another x? "))
        y3 = int(input("Another y? "))
        size3 = int(input("Another size? "))
        rotation3 = int(input("Another rotation? "))
        sprite3.y = y3
        sprite3.x = x3
        sprite3.scale = size3
        sprite3.image_rotation =  rotation3
        sprite3.is_visible = True



if s == "owl":
    sprite1.image="owl.gif"
    sprite2.image="owl.gif"
    sprite3.image="owl.gif"
    if  number == "1":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
    if  number == "2":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
    if  number == "3":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
        x3 = int(input("Another x? "))
        y3 = int(input("Another y? "))
        size3 = int(input("Another size? "))
        rotation3 = int(input("Another rotation? "))
        sprite3.y = y3
        sprite3.x = x3
        sprite3.scale = size3
        sprite3.image_rotation =  rotation3
        sprite3.is_visible = True



if s == "elephant":
    sprite1.image="elephant.png"
    sprite2.image="elephant.png"
    sprite3.image="elephant.png"
    if  number == "1":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
    if  number == "2":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
    if  number == "3":
        x = int(input("How about x? "))
        y = int(input("How about y? "))
        size = int(input("How about size? "))
        rotation = int(input("How about rotation? "))
        sprite1.y = y
        sprite1.x = x
        sprite1.scale = size
        sprite1.image_rotation = rotation
        sprite1.is_visible = True
        x2 = int(input("Another x? "))
        y2 = int(input("Another y? "))
        size2 = int(input("Another size? "))
        rotation2 = int(input("Another rotation? "))
        sprite2.y = y2
        sprite2.x = x2
        sprite2.scale = size2
        sprite2.image_rotation = rotation2
        sprite2.is_visible = True
        x3 = int(input("Another x? "))
        y3 = float(input("Another y? "))
        size3 = int(input("Another size? "))
        rotation3 = int(input("Another rotation? "))
        sprite3.y = y3
        sprite3.x = x3
        sprite3.scale = size3
        sprite3.image_rotation =  rotation3
        sprite3.is_visible = True
         
msg = ("sprite image: " + str(sprite1.image) + "," + "sprite amount: " + str(number) + "," +
"sprite1 x: " + str(sprite1.x) + "," + "sprite1 y: " + str(sprite1.y) + "," + 
"sprite1 scale: " + str(sprite1.scale) + "," + "sprite1 rotation: " + str(sprite1.rotation))

print(msg)
print(type(msg))
print(type(x3))
print(type(y3))
print(type(window))
print(type(sprite1.is_visible))




window.run()