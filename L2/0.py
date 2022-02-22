from pycat.core import Window
window = Window()
elephant = window.create_sprite()
fireball = window.create_sprite()
owl = window.create_sprite()
window.background_image="forest_background.jpg"
wish_x = input("Where do you want the owl to be locate? ")

elephant.image = "elephant.png"
elephant.x = 640
elephant.y=320
fireball.image = "fireball.gif"
fireball.x = 0
fireball.y=0
owl.image = "owl.gif"
owl.x = int(wish_x)
owl.y=0
owl.scale=5



window.run()
