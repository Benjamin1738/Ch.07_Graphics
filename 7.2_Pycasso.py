'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(500,500,"Benjamin")
arcade.set_background_color(arcade.color.PEACH)
arcade.start_render()

# for i in range(0,510,35):
#     arcade.draw_text("*",i,i,arcade.color.WHITE,40)
#White inside eye
arcade.draw_ellipse_filled(250,250,450,150,arcade.color.WHITE)
#outline eye
arcade.draw_ellipse_outline(250,250,450,150,arcade.color.BLACK,7)
#Puiple
arcade.draw_circle_filled(250,250,75,arcade.color.BROWN_NOSE,)

arcade.draw_circle_filled(250,250,35,arcade.color.BLACK)

#eye hair

for brow in range(150,370,20):
    arcade.draw_line(brow,320,brow,340,arcade.color.BLACK,1)


#hair
for eye1 in range(50,400,15):
    arcade.draw_text("/|]/]|",eye1,350,arcade.color.BLACK)

for eye2 in range(50,400,15):
    arcade.draw_text("/|]/]|",eye2,360,arcade.color.BLACK)
#brow
for i in range(150,370,20):
    arcade.draw_line(i,160,i,180,arcade.color.BLACK,1)
arcade.run()
arcade.finish_render()



