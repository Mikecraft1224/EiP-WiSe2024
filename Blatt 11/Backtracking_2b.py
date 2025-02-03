from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
import time

def read_map(filename):
    lab = []

    # einlesen der map aus textdatei
    with open(filename, 'r') as f:
        for line in f:
            lab.append([char for char in line][:-1])
    return lab

def print_map(lab:list[list[str]], mapObjs, horizontalOffset=0, verticalOffset=0):
    labObjs = []

    for y in range(len(lab)):
        rowObjs = []
        for x in range(len(lab[y])):
            rowObjs.append(mapObjs[lab[y][x].upper()])
        labObjs.append(iobj.HorizontalStack(rowObjs))
    
    labObjs = iobj.VerticalStack(labObjs)

    basic_io.draw_object(labObjs, horizontalOffset, verticalOffset)

def find_way(lab, path: list):
    last = path[-1]

    if lab[last[0]][last[1]] == 'A':
        return path
    
    for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next = [last[0] + dir[0], last[1] + dir[1]]

        if lab[next[0]][next[1]] != " " and lab[next[0]][next[1]] != "A" and lab[next[0]][next[1]] != "v":
            continue
    
        path.append(next)

        if lab[next[0]][next[1]] != "A":
            lab[next[0]][next[1]] = "V"

        result = find_way(lab, path)
        if result:
            return result
        path.pop()

        lab[next[0]][next[1]] = "v"

    return False

if __name__ == '__main__':
    basic_io.start()

    lab = read_map("Blatt 11\\maze_small.txt")
    entryPos = None

    for y in range(len(lab)):
        for x in range(len(lab[y])):
            if lab[y][x] == 'E':
                entryPos = [y, x]
                break
        else:
            continue

        break

    # Calculating square size and offsets
    squareSize = 640//len(lab[0]) if 640//len(lab[0]) < 480//len(lab) else 480//len(lab)
    horizontalOffset = (640 - squareSize * len(lab[0])) // 2
    verticalOffset = (480 - squareSize * len(lab)) // 2

    # Creating map objects to use
    borderThickness = squareSize//10

    mapObjs = {
        ".": iobj.Rectangle(squareSize, squareSize, fill_color=BLACK),
        "E": iobj.Rectangle(squareSize, squareSize, fill_color=RED, border_color=BLACK, border_thickness=borderThickness),
        "A": iobj.Rectangle(squareSize, squareSize, fill_color=BLUE, border_color=BLACK, border_thickness=borderThickness),
        " ": iobj.Rectangle(squareSize, squareSize, fill_color=WHITE, border_color=BLACK, border_thickness=borderThickness),
        "V": iobj.Rectangle(squareSize, squareSize, fill_color=LIGHT_BLUE, border_color=BLACK, border_thickness=borderThickness)
    }

    path = find_way(lab, [entryPos])
    
    print_map(lab, mapObjs, horizontalOffset, verticalOffset)
    time.sleep(5)
    
    for pos in path:
        lab[pos[0]][pos[1]] = "E"
        print_map(lab, mapObjs, horizontalOffset, verticalOffset)
        time.sleep(0.1)

    basic_io.wait_close()