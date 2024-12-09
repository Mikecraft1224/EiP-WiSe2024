from jguvc_eip import basic_io
from jguvc_eip.colors import *

if __name__ == "__main__":
    basic_io.start()

    # Window size: 640x480
    basic_io.draw_rectangle(
        75, 195, 490, 75, 
        border_color=RED, fill_color=WHITE, 
        border_thickness=5
    )
    basic_io.draw_text(90, 200, "Hello World!", font_height=64)

    basic_io.wait_close()
