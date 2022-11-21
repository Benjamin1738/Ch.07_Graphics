'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window(300,260,"The Stars and Strips")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#Lines
for i in range(0,270,20):
    arcade.draw_line(0,i,310,i,arcade.color.BLACK,1)
#Blue background
arcade.draw_rectangle_filled(30,200,190,160,(0,40,104,255))

for r in range(10,260,40):
    arcade.draw_rectangle_filled(150,r,310,20,arcade.color.RED,0,)

#Blue rec
arcade.draw_rectangle_filled(30,200,225,160,(0,40,104,255))

#Stars

arcade.draw_text("*  *  *  *  *  *",0,230,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *  *",0,205,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *  *",0,180,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *  *",0,155,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *  *",0,130,arcade.color.WHITE,20,5)

#Second stars

arcade.draw_text("*  *  *  *  *",10,220,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *",10,195,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *",10,165,arcade.color.WHITE,20,5)
arcade.draw_text("*  *  *  *  *",10,145,arcade.color.WHITE,20,5)






arcade.finish_render()

arcade.run()