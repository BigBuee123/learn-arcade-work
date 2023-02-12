import arcade  # needed to do anything with the arcade library

start = 0
tilt = 0


def on_draw(time_delta):
    global start, tilt
    start = start - 10
    tilt = (tilt + 10) % 360
    if start < 0:
        start = 75

    arcade.start_render()
    # draw the road
    arcade.draw_lrtb_rectangle_filled(0, 800, 400, 200, arcade.color.BLACK)

    # white lines
    for i in range(100, 800, 75):
        arcade.draw_lrtb_rectangle_filled(start + i, start + i + 50, 310, 300, arcade.color.WHITE)

    # car
    arcade.draw_polygon_filled([(25, 345), (50, 375), (350, 375), (375, 345)], arcade.color.GRAY)
    arcade.draw_rectangle_filled(200, 320, 350, 50, arcade.color.RED)
    arcade.draw_ellipse_filled(100, 300, 50, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(100, 300, 4, 30, arcade.csscolor.BLACK, tilt)
    arcade.draw_ellipse_filled(300, 300, 50, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(300, 300, 4, 30, arcade.csscolor.BLACK, tilt)
    arcade.draw_polygon_filled([(50, 375), (75, 400), (325, 400), (350, 375)], arcade.color.RED)

    # house
    arcade.draw_lrtb_rectangle_filled(400, 600, 550, 400, arcade.color.BEIGE)
    arcade.draw_triangle_filled(350, 550, 500, 650, 650, 550, arcade.color.DARK_BROWN)
    arcade.draw_lrtb_rectangle_filled(480, 520, 450, 400, arcade.color.BROWN)
    arcade.draw_ellipse_filled(510, 420, 4, 10, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(425, 455, 450, 425, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(545, 575, 450, 425, arcade.color.BLACK)

    arcade.finish_render()


arcade.open_window(800, 600, "My Drawing")
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
arcade.schedule(on_draw, 1 / 60)
arcade.run()
