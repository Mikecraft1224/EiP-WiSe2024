from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
from random import randint
import time

def recursiveUnpack(bars):
    if not isinstance(bars, iobj.HorizontalStack):
        return [bars]
    
    return recursiveUnpack(bars.objects[0]) + [bars.objects[1]]

def recursivePack(extracted_items):
    if len(extracted_items) == 1:
        return extracted_items[0]
    
    return iobj.HorizontalStack([extracted_items[0], recursivePack(extracted_items[1:])])

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
    time.sleep(1)

    # Entpacken der Liste
    extracted_items =  recursiveUnpack(bars)

    # Zurückpacken der Liste
    bars = recursivePack(extracted_items)

    basic_io.draw_object(bars, (640%len(list))//2, 50)
    time.sleep(5)
    basic_io.clear_image()
    time.sleep(1)

    basic_io.wait_close()