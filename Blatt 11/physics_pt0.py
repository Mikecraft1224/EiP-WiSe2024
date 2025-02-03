from jguvc_eip import basic_io as bio
from jguvc_eip import image_objects as io
from jguvc_eip.colors import *
from time import sleep

# settings

# settings to play with
accelleration = 0.2

# constant stuff
field_x = 100
wire_length = 200
db_visible_buffer: int = 0
db_active_buffer: int = 1
pos = 0
speed = 0

while True:
    # double buffering
    bio.set_active_image(db_active_buffer)
    bio.set_visible_image(db_visible_buffer)
    bio.copy_image(db_visible_buffer, db_active_buffer)
    db_visible_buffer, db_active_buffer = db_active_buffer, db_visible_buffer
    bio.clear_image()

    # draw constant stuff
    rect1 = io.Rectangle(20, 20, fill_color=BLACK)  # top cube
    line = io.Rectangle(1, wire_length)  # line as a rectangle
    rect2 = io.Rectangle(20, 20, fill_color=BLACK)  # bottom rectangle
    base_obj = io.VerticalStack([rect1, line, rect2])  # stack everything

    # speed constantly increases by acceleration
    speed += accelleration

    # normal falling
    pos += speed

    # boundary check for bottom
    if pos >= wire_length:
        pos = wire_length
        speed = 0

    # draw ball in calculated pos
    ball = io.Circle(20, fill_color=RED)
    ball = io.Translate(ball, 0, int(pos))
    obj_stack = io.Overlay([base_obj, ball])

    # draw composite object
    bio.draw_object(obj_stack, field_x, 0)
    sleep(0.016)
