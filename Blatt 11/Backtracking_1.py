from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *

def read_map(filename):
    lab = []

    # einlesen der map aus textdatei
    with open(filename, 'r') as f:
        for line in f:
            lab.append([char for char in line][:-1])
    return lab

def print_map(lab, mapObjs, horizontalOffset=0, verticalOffset=0):
    labObjs = []

    for y in range(len(lab)):
        rowObjs = []
        for x in range(len(lab[y])):
            rowObjs.append(mapObjs[lab[y][x]])
        labObjs.append(iobj.HorizontalStack(rowObjs))
    
    labObjs = iobj.VerticalStack(labObjs)

    basic_io.draw_object(labObjs, horizontalOffset, verticalOffset)

if __name__ == '__main__':
    basic_io.start()

    labyrinth = read_map("Blatt 11\\maze_small.txt")
    # Calculating square size and offsets
    squareSize = width if (width := 640//len(labyrinth[0])) < (height := 480//len(labyrinth)) else height
    horizontalOffset = (640 - squareSize * len(labyrinth[0])) // 2
    verticalOffset = (480 - squareSize * len(labyrinth)) // 2

    # Creating map objects to use
    borderThickness = squareSize//10

    mapObjs = {
        ".": iobj.Rectangle(squareSize, squareSize, fill_color=BLACK),
        "E": iobj.Rectangle(squareSize, squareSize, fill_color=RED, border_color=BLACK, border_thickness=borderThickness),
        "A": iobj.Rectangle(squareSize, squareSize, fill_color=BLUE, border_color=BLACK, border_thickness=borderThickness),
        " ": iobj.Rectangle(squareSize, squareSize, fill_color=WHITE, border_color=BLACK, border_thickness=borderThickness)
    }

    # Drawing
    print_map(labyrinth, mapObjs, horizontalOffset, verticalOffset)


    basic_io.wait_close()