from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *

if __name__ == '__main__':
    basic_io.start()

    obj = iobj.VerticalStack([
        iobj.Rectangle(40, 40, fill_color=BLACK),
        iobj.Rectangle(2, 300, fill_color=BLACK),
        iobj.Rectangle(40, 40, fill_color=BLACK)
    ])

    ball = iobj.Circle(40, fill_color=RED)
    ball = iobj.Translate(ball, 0, 300)

    basic_io.draw_object(iobj.Overlay([obj, ball]), 300, 50)

    basic_io.wait_close()