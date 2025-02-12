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

    balls = {
        "blue": {
            "obj": iobj.Circle(40, fill_color=BLUE),
            "y": 40,
            "velocity": 0,
            "mass": 1
        },
        "red": {
            "obj": iobj.Circle(40, fill_color=RED),
            "y": 170,
            "velocity": 0,
            "mass": 1
        }
    }
    
    ballAcceleration = 0.2
    ballMaxVelocity = 10

    jumped = False

    # Breaking when "q" is pressed
    while not "q" in basic_io.get_current_keys_down():
        # Double buffering
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)
        basic_io.clear_image()

        # Drawing
        basic_io.draw_object(iobj.Overlay([obj, 
                                iobj.Translate(balls["blue"]["obj"], 0, balls["blue"]["y"]), 
                                iobj.Translate(balls["red"]["obj"], 0, balls["red"]["y"])
                            ]), 300, 50)

        # Receiveing input
        if "u" in basic_io.get_current_keys_down() and not jumped:
            balls["red"]["velocity"] = -8
            jumped = True

        if "u" not in basic_io.get_current_keys_down():
            jumped = False

        # Moving the balls
        for color in balls:
            ball = balls[color]

            # Changing velocity
            if ball["velocity"] < ballMaxVelocity and ball["y"] < 300:
                ball["velocity"] += ballAcceleration

            # Adjusting velocity
            if ball["y"] + int(ball["velocity"]) > 300:
                ball["velocity"] = 300 - ball["y"]
            elif ball["y"] + int(ball["velocity"]) < 40:
                ball["velocity"] = 40 - ball["y"]

            ball["y"] += int(ball["velocity"])
        
        # Checking for collision
        if balls["blue"]["y"] + 40 > balls["red"]["y"]:
            # Calculating new velocities
            v1 = balls["blue"]["velocity"]
            v2 = balls["red"]["velocity"]
            m1 = balls["blue"]["mass"]
            m2 = balls["red"]["mass"]

            balls["blue"]["velocity"] = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
            balls["red"]["velocity"] = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

            # Adjusting velocities
            if balls["blue"]["y"] + 40 > balls["red"]["y"]:
                balls["blue"]["y"] = balls["red"]["y"] - 40
                balls["red"]["y"] = balls["blue"]["y"] + 40

        # Incrementing counters
        z = not z
        time.sleep(0.016)


    basic_io.wait_close()