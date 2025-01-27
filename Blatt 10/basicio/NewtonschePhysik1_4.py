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
    ballVelocity = 0
    ballAcceleration = 0.1
    ballMaxVelocity = 10

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
            # Changing velocity
            if ballVelocity < ballMaxVelocity:
                ballVelocity += ballAcceleration

            # Adjusting velocity
            if ballY + int(ballVelocity) > 300:
                ballVelocity = 300 - ballY

            ballY += int(ballVelocity)

        # Incrementing counters
        z = not z
        time.sleep(0.016)


    basic_io.wait_close()