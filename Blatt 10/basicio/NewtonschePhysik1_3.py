from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
import time

if __name__ == '__main__':
    basic_io.start()

    z = True

    obj = iobj.VerticalStack([
        iobj.Rectangle(40, 40, fill_color=BLACK),
        iobj.Rectangle(2, 300, fill_color=BLACK),
        iobj.Rectangle(40, 40, fill_color=BLACK)
    ])

    ball = iobj.Circle(40, fill_color=RED)

    ballY = 40
    ballVelocity = 2

    # Breaking when "q" is pressed
    while not "q" in basic_io.get_current_keys_down():
        # Double buffering
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)
        basic_io.clear_image()

        # Drawing
        basic_io.draw_object(iobj.Overlay([obj, iobj.Translate(ball, 0, ballY)]), 300, 50)

        # Moving the ball
        if ballY < 300:
            ballY += ballVelocity

        # Incrementing counters
        z = not z
        time.sleep(0.016)


    basic_io.wait_close()