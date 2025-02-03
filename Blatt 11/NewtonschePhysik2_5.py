# All relevant changes are marked with "Changed" or "Added" comments

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
    ballAcceleration = 0.2
    ballMaxVelocity = 10

    # Added flag to only trigger jump once per press
    jumped = False
    inAir = True

    # Breaking when "q" is pressed
    while not "q" in basic_io.get_current_keys_down():
        # Double buffering
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)
        basic_io.clear_image()

        # Drawing
        basic_io.draw_object(iobj.Overlay([obj, iobj.Translate(ball, 0, ballY)]), 300, 50)

        # Receiveing input
        if "u" in basic_io.get_current_keys_down() and not jumped: # and not inAir:
            ballVelocity = -8
            # ballVelocity -= 8
            jumped = True
            inAir = True

        if "u" not in basic_io.get_current_keys_down():
            jumped = False

        # Moving the ball
        # Changed condition to allow moving if already on the ground
        if 40 <= ballY <= 300:
            # Changing velocity
            # Changed condition to only accelerate if in the air
            if ballVelocity < ballMaxVelocity and ballY < 300:
                ballVelocity += ballAcceleration

            # Adjusting velocity
            if ballY + int(ballVelocity) > 300:
                ballVelocity = 300 - ballY
                inAir = False
            # Added condition to stop ball from going through the ceiling
            elif ballY + int(ballVelocity) < 40:
                ballVelocity = 40 - ballY

            ballY += int(ballVelocity)

            # if ballY > 300:
            #     ballY = 300
            #     ballVelocity = 0
            # elif ballY < 40:
            #     ballY = 40
            #     ballVelocity = 0

        # Incrementing counters
        z = not z
        time.sleep(0.016)


    basic_io.wait_close()