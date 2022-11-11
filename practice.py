import arcade
arcade.open_window(600,600,"My Drawing",)
arcade.set_background_color((arcade.color.IMPERIAL_BLUE))

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,300,200,0,arcade.color.DEEP_CHAMPAGNE)
arcade.draw_rectangle_filled(300,300,400,400,arcade.color.AFRICAN_VIOLET,45)
arcade.draw_rectangle_outline(300,300,400,400,arcade.color.BRICK_RED,3,45)
#points/lines
arcade.draw_point(300,300,arcade.color.BLACK,3)
arcade.draw_line(100,100,500,500,arcade.color.CORAL,4)
#Circles/ellipes
arcade.draw_circle_filled(300,300,50,arcade.color.YELLOW_ORANGE,)
arcade.draw_circle_outline(300,300,50,arcade.color.BLACK,)
arcade.draw_ellipse_filled(400,400,100,50,arcade.color.BOTTLE_GREEN,45)

#polygon
point_list=((100,100),(120,400),(200,400),(100,150))
arcade.draw_polygon_filled(point_list,arcade.color.BISQUE)

#text

arcade.draw_text("PyCasso",200,550,arcade.color.CORAL,20)

#picture

# mypic = arcade.load_texture("python.png")
# arcade.draw_texture_rectangle(500,100,mypic.width,mypic.height,mypic,0,200)

#Rails looped
for i in range(0,610,20):
    arcade.draw_rectangle_filled(i,60,10,30,arcade.color.BOTTLE_GREEN)


#Fence rails
arcade.draw_rectangle_filled(300,67,600,5,(255,255,255))
arcade.draw_rectangle_filled(300,52,600,5,(255,255,255))


radius = 50
y=50
for i in range(3):
    arcade.draw_circle_filled(100,y,radius,(255,255,255))
    y=y+1.8*radius
    radius=radius*.8
#Drawing End
arcade.finish_render()



arcade.run()