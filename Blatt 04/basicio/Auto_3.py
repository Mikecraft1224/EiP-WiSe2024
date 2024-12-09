from jguvc_eip import basic_io
from jguvc_eip.colors import *    
import time

if __name__ == "__main__":
    basic_io.start()
    
    x = 0
    while True:
        basic_io.clear_image()

        basic_io.draw_rectangle(350, 300, 150, 150, fill_color=BLUE)
        basic_io.draw_polygon([(350, 300), (425, 225), (500, 300)], fill_color=BLUE)
        
        basic_io.draw_rectangle(x, 375, 150, 50, fill_color=RED)
        basic_io.draw_circle(x + 25, 425, 25, fill_color=BLACK)
        basic_io.draw_circle(x + 125, 425, 25, fill_color=BLACK)

        x += 1

        # x can also loop around with the following line:
        # x = (x + 1) % 640

        time.sleep(0.016)

    basic_io.wait_close()