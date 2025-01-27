from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
from random import randint
import time

if __name__ == '__main__':
    basic_io.start()
    
    list = [randint(0,100) for i in range(100)]

    # Möglichkeit mit for-Schleife
    bars = []
    for number in list:
        bars.append(iobj.Rectangle(640//len(list), number))

    # Möglichkeit mit List Comprehension
    # bars = [iobj.Rectangle(640//len(list), num) for num in list]

    # Stacking
    bars = iobj.HorizontalStack(bars)

    basic_io.draw_object(bars, (640%len(list))//2, 50)

    time.sleep(5)
    
    basic_io.clear_image()
    basic_io.wait_close()