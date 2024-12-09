from jguvc_eip import basic_io
from jguvc_eip import image_objects
from jguvc_eip.colors import *
from random import randint
from time import sleep
from typing import Optional, List


def nzr_int():
    result = randint(1, 5)
    if randint(1, 2) == 1:
        result = -result
    return result


if __name__ == '__main__':
    basic_io.start()
    basic_io.print_message('This is a simple basic_io demo.')
    basic_io.print_message('  - Press n (next) or p (prev) to cycle demos (ellipses, other shapes,'
                           ' mouse-painter, event logger, image_objects test).')
    basic_io.print_message('  - Press d to enable/disable double buffering.')
    basic_io.print_message('  - Press 1..3 to change resolution (1=320x240, 2=640x480, 3=1024x768;'
                           ' background color changes slightly;'
                           ' ctrl+1/2/3/4 changes zoom level.')
    basic_io.print_message('  - Press s to enable/disable slow mode.')
    basic_io.print_message('  - Press q (or ctrl-q) to quit.')

    slow_mode: bool = False
    double_buffer: bool = True
    db_visible_buffer: int = 0
    db_active_buffer: int = 1
    demo: int = 0
    demo_names: List[str] = ['Random Ellipses Demo', 'Lines & Rectangles Demo', 'Polygons Demo',
                             'Painter Demo', 'Event Logger', '"image_objects.py" Test', 'Text Input Test',
                             'Random Points Test']
    num_demos: int = len(demo_names)

    shape_name: List[str] = ['circle', 'rectangle', 'text', 'ellipse', 'polygon',
                             'vstack', 'hstack', 'overlay', 'transform']
    shape_index: int = 0
    num_shapes: int = len(shape_name)

    poly = [[randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)],
            [randint(0, 639), randint(0, 479)]]

    drift = [[nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()],
             [nzr_int(), nzr_int()]]

    col_index = 0
    pix_col = [128, 128, 128]

    loaded_images: List[int] = []

    while True:
        if double_buffer:
            basic_io.set_active_image(db_active_buffer)
            basic_io.set_visible_image(db_visible_buffer)
            basic_io.copy_image(db_visible_buffer, db_active_buffer)
            db_visible_buffer, db_active_buffer = db_active_buffer, db_visible_buffer
        else:
            basic_io.set_active_image(0)
            basic_io.set_visible_image(0)

        if demo == 0:

            foreground_color: Optional[RGBColor] = SHADES_OF_BLUE[randint(3, 6)]
            background_color: Optional[RGBColor] = BLACK
            if randint(1, 2) == 2:
                foreground_color = SHADES_OF_RED[randint(3, 6)]
            if randint(1, 5) == 1:
                foreground_color = None
            if randint(1, 5) == 1:
                background_color = None
            basic_io.draw_ellipse(randint(0, 639), randint(0, 479), randint(1, 300), randint(1, 300),
                                  foreground_color, background_color, 2)
        elif demo == 1:

            if randint(1, 2) == 2:
                color: RGBColor = SHADES_OF_VIOLET[randint(0, 6)]
                basic_io.draw_line(randint(0, 639), randint(0, 479), randint(0, 639), randint(0, 479), color, 2)
            else:
                color = SHADES_OF_GREEN[randint(0, 6)]
                basic_io.draw_rectangle(randint(0, 639), randint(0, 479),
                                        randint(0, 639), randint(0, 479), None, color, 2)

        elif demo == 2:

            color_drift: RGBColor = ORANGE
            if randint(1, 2) == 2:
                col_index += 1
                if col_index > 6:
                    col_index = 0
                color_drift: RGBColor = SHADES_OF_ORANGE[col_index]
            poly_tuple = []
            for i in range(len(poly)):
                poly[i][0] += drift[i][0]
                poly[i][1] += drift[i][1]
                if poly[i][0] >= 640:
                    poly[i][0] = 639
                    drift[i][0] = -drift[i][0]
                if poly[i][1] >= 480:
                    poly[i][1] = 479
                    drift[i][1] = -drift[i][1]
                if poly[i][0] < 0:
                    poly[i][0] = 0
                    drift[i][0] = -drift[i][0]
                if poly[i][1] < 0:
                    poly[i][1] = 0
                    drift[i][1] = -drift[i][1]
                poly_tuple.append((poly[i][0], poly[i][1]))
                if randint(1, 1000) == 1:
                    drift[i][randint(0, 1)] = nzr_int()

            b_col = None
            if randint(1, 5) == 1:
                if randint(1, 2) == 1:
                    b_col = WHITE
                else:
                    b_col = SHADES_OF_YELLOW[randint(4, 6)]

            basic_io.draw_polygon(poly_tuple, b_col, color_drift, 2)

        elif demo == 3:
            current_keys_down: List[str] = basic_io.get_current_keys_down()
            if "left_mouse_button" in current_keys_down:
                m_coords = basic_io.get_current_mouse_position()
                basic_io.draw_circle(m_coords[0], m_coords[1], 10)
            elif "right_mouse_button" in current_keys_down:
                m_coords = basic_io.get_current_mouse_position()
                basic_io.draw_circle(m_coords[0], m_coords[1], 50, WHITE, WHITE)

        elif demo == 4:
            pass
        elif demo == 5:
            basic_io.draw_rectangle(0, 110, 2000, 2000, WHITE, None, 0)
            basic_io.draw_text(16, 116, "Testing image objects library.")
            basic_io.draw_text(16, 132, "Shape: "
                               + shape_name[shape_index] + " (Press a (prev) / b (next) to cycle shapes.)")
            basic_io.draw_rectangle(0, 160, 639, 319, (240, 240, 240), BLACK)
            # shape_name: List[str] = ['circle', 'rectangle', 'text',
            # 'ellipse', 'polygon', 'vstack', 'hstack', 'overlay']
            if shape_index == 0:
                basic_io.draw_object(image_objects.Circle(50, RED), 1, 161)
            elif shape_index == 1:
                basic_io.draw_object(image_objects.Rectangle(300, 200, SKY), 1, 161)
            elif shape_index == 2:
                basic_io.draw_object(image_objects.Text('Text test'), 1, 161)
            elif shape_index == 3:
                basic_io.draw_object(image_objects.Ellipse(100, 200, GREEN, None), 1, 161)
            elif shape_index == 4:
                basic_io.draw_object(image_objects.Polygon([(0, 10), (50, 10), (50, 0), (70, 20),
                                                            (50, 40), (50, 30), (0, 30)], PINK), 1, 161)
            elif shape_index == 5:
                basic_io.draw_object(image_objects.VerticalStack([
                    image_objects.Text("-- French Flag --", bold=True),
                    image_objects.VerticalStack([
                        image_objects.Rectangle(350, 80, RED, None),
                        image_objects.Rectangle(350, 80, WHITE, None),
                        image_objects.Rectangle(350, 80, BLUE, None)
                    ])
                ], 5), 1, 161)
            elif shape_index == 6:
                basic_io.draw_object(image_objects.VerticalStack([
                    image_objects.Text("-- Italian Flag --", italic=True, fixed_width=False),
                    image_objects.HorizontalStack([
                        image_objects.Rectangle(100, 200, GREEN, None),
                        image_objects.Rectangle(100, 200, WHITE, None),
                        image_objects.Rectangle(100, 200, RED, None)
                    ])
                ], 5), 1, 161)
            elif shape_index == 7:
                basic_io.draw_object(image_objects.VerticalStack([
                    image_objects.Text("-- Japanese Flag --", fixed_width=False),
                    image_objects.Overlay([
                        image_objects.Rectangle(350, 240, WHITE, None),
                        image_objects.Translate(
                            image_objects.Circle(130, RED, None), 110, 55
                        ),
                    ])
                ], 5), 1, 161)
            elif shape_index == 8:
                basic_io.draw_object(
                    image_objects.VerticalStack(
                        [
                            image_objects.Text("-- A lot of transformations --", fixed_width=False),
                            image_objects.Overlay(
                                [
                                    image_objects.Circle(300, (255, 255, 255)),
                                    image_objects.Translate(
                                            image_objects.Scale(
                                            image_objects.Overlay(
                                                [
                                                    image_objects.Circle(300, (250, 250, 250)),
                                                    image_objects.Translate(
                                                        image_objects.Scale(
                                                            image_objects.Circle(300, (240, 240, 240)), 0.7
                                                        ),
                                                        -47, -47
                                                    )
                                                ]
                                            ), 0.7
                                        ),
                                        -47, -47
                                    ),
                                    image_objects.Translate(
                                        image_objects.Overlay(
                                            [
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE),   0),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY),  30),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE),  60),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY),  90),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE), 120),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY), 150),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE), 180),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY), 210),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE), 240),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY), 270),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30, BLUE), 300),
                                                image_objects.Rotate(image_objects.Rectangle(270, 30,  SKY), 330)
                                            ]
                                        ),
                                        330, 135
                                    )
                                ]
                            )
                        ],
                        5
                    ),
                    1, 161
                )
        elif demo == 6:
            basic_io.draw_text(16, 100, "Press [i] to input some text.",
                               BLACK, WHITE)
            basic_io.draw_text(16, 120, "Press [a] to add an image by specifying its filename.",
                               BLACK, WHITE)
            if len(loaded_images) > 0:
                basic_io.draw_image(randint(0, 600), randint(200, 400), randint(0, len(loaded_images)-1))

        elif demo == 7:
            basic_io.draw_pixel(randint(0, 639), randint(0, 479), (pix_col[0], pix_col[1], pix_col[2]))
            for i in range(3):
                pix_col[i] += randint(-1, 1)
                if pix_col[i] < 0:
                    pix_col[i] = 0
                if pix_col[i] > 255:
                    pix_col[i] = 255
            d7_mx, d7_my = basic_io.get_current_mouse_position()
            d7_col = basic_io.read_pixel(d7_mx, d7_my)
            basic_io.draw_text(10, 100, 'Color under mouse is: ' + str(d7_col) + '        ', BLACK, WHITE)

        basic_io.draw_text(5, 5, demo_names[demo], background_color=WHITE)
        status: str = '('
        if double_buffer:
            status += "double buffer on,"
        else:
            status += "double buffer off,"
        if slow_mode:
            status += "slow)"
        else:
            status += "fast)"
        basic_io.draw_text(5, 25, status, background_color=WHITE)

        key = basic_io.get_last_key_pressed_event()

        if demo == 4:
            if key != '':
                basic_io.print_message("key pressed: <" + key + ">")
            keys_down: List[str] = basic_io.get_current_keys_down()
            num_key_down: int = 0
            basic_io.draw_rectangle(10, 110, 2000, 2000, WHITE, None, 0)
            basic_io.draw_text(16, 116, 'Keys currently pressed:')
            if len(keys_down) == 0:
                basic_io.draw_text(16, 140, '(none)')
            else:
                for key_down in keys_down:
                    basic_io.draw_text(16+8*num_key_down, 140, '[' + key_down + ']')
                    num_key_down += len(key_down)+4
            mouse_coords = basic_io.get_current_mouse_position()
            basic_io.draw_text(16, 160, 'current mouse coordinates:')
            basic_io.draw_text(16, 180, '(x=' + str(mouse_coords[0]) + ', y='+str(mouse_coords[1]) + ')')

        if demo == 6:
            if key == 'i':
                answer = basic_io.input_string("type some text:")
                basic_io.draw_rectangle(10, 140, 1000, 1000, WHITE, None)
                basic_io.draw_text(10, 140, "Your answer was: ", BLACK, WHITE)
                basic_io.draw_text(10, 160, answer)
            if key == 'a':
                answer = basic_io.input_string("Filename of image to be added:")
                new_img_index: int = basic_io.load_image(answer)
                if new_img_index == -1:
                    basic_io.draw_text(10, 140, "Error - file not found!   ", BLACK, WHITE)
                else:
                    basic_io.draw_text(10, 140, "We've added the image file", BLACK, WHITE)
                    loaded_images.append(new_img_index)

        if key == 'q':
            break
        elif key == 'd':
            double_buffer = not double_buffer
        elif key == 's':
            slow_mode = not slow_mode
        elif key == '1' or key == '2' or key == '3':
            new_w = 320
            new_h = 240
            new_col = (200, 200, 255)
            if key == '2':
                new_w = 640
                new_h = 480
                new_col = (255, 255, 255)
            if key == '3':
                new_w = 1024
                new_h = 768
                new_col = (255, 255, 128)

            basic_io.set_active_image(0)
            basic_io.resize_image(new_w, new_h, new_col)
            basic_io.set_active_image(1)
            basic_io.resize_image(new_w, new_h, new_col)
            basic_io.set_active_image(db_active_buffer)
        elif key == 'n':
            basic_io.clear_image()
            demo += 1
            if demo == num_demos:
                demo = 0
        elif key == 'p':
            basic_io.clear_image()
            demo -= 1
            if demo < 0:
                demo = num_demos-1
        elif key == 'a':
            shape_index = (shape_index - 1) % num_shapes
        elif key == 'b':
            shape_index = (shape_index + 1) % num_shapes
        if slow_mode:
            sleep(0.05)

    basic_io.print_message("GOODBYE!")
    sleep(0.5)
    basic_io.close_and_exit()
