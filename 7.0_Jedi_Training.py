#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

arcade.open_window(500,400)
arcade.set_background_color((arcade.color.ALMOND))
#Background Color

arcade.start_render()


#PINK Rectangle
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)

#Lines Checkers
for i in range(0,510,20):
    arcade.draw_line(i,0,i,400,arcade.color.BLACK)
for i in range(0,410,20):
    arcade.draw_line(0,i,500,i,arcade.color.BLACK)

#Circle
arcade.draw_circle_filled(250,200,48,arcade.color.WISTERIA)

#Angled Rectangle
arcade.draw_rectangle_filled(200,270,40,20,arcade.color.BRICK_RED,-45)
#Text
arcade.draw_text("I Love you. I Know",20,165,arcade.color.RED,16,25)

#Diag Line
arcade.draw_line(80,20,120,60,arcade.color.BLUE)

#Red Dot
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)

#Pac man
arcade.draw_arc_filled(400,300,150,150,arcade.color.YELLOW,30,330)


arcade.finish_render()

arcade.run()