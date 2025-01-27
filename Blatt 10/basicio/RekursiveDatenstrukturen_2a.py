from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
from random import randint
import time

if __name__ == '__main__':
    basic_io.start()
    
    list = [randint(0,100) for i in range(100)]

    barWidth = 640//len(list)

    # Normal Version
    bars = []
    for number in list:
        bars.append(iobj.Rectangle(barWidth, number))

    bars = iobj.HorizontalStack(bars)

    basic_io.draw_object(bars, (640%len(list))//2, 50)
    time.sleep(5)
    basic_io.clear_image()
    time.sleep(1)

    # Recursive Version
    bars = iobj.Rectangle(barWidth, list[0])
    for i in range(1, len(list)):
        bars = iobj.HorizontalStack([
            bars,
            iobj.Rectangle(barWidth, list[i])
        ])

    basic_io.draw_object(bars, (640%len(list))//2, 50)
    time.sleep(5)
    
    basic_io.clear_image()
    basic_io.wait_close()