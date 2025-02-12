from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
import time
from copy import deepcopy

best_path = None

def read_map(filename):
    lab = []
    entryPos = None

    # einlesen der map aus textdatei
    with open(filename, 'r') as f:
        for line in f:
            lineChars = []
            for char in line[:-1]:
                lineChars.append(char)

                if char == 'E':
                    entryPos = [len(lab), len(lineChars)-1]
            lab.append(lineChars)

    return lab, entryPos

def draw_map(lab, mapObjs, horizontalOffset=0, verticalOffset=0):
    labObjs = []

    for y in range(len(lab)):
        rowObjs = []
        for x in range(len(lab[y])):
            rowObjs.append(mapObjs[lab[y][x].upper()])
        labObjs.append(iobj.HorizontalStack(rowObjs))
    
    labObjs = iobj.VerticalStack(labObjs)

    basic_io.draw_object(labObjs, horizontalOffset, verticalOffset)

def find_way(lab, path:list):
    global best_path

    last = path[-1]

    if lab[last[0]][last[1]] == 'A':
        # Changed to swapping the best path with the current path
        best_path = deepcopy(path)
        return True
    elif best_path and len(path) >= len(best_path) - 1:
        # If the current path is longer or equal as long as the best path, we can stop searching
        return False
    
    for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next = [last[0] + dir[0], last[1] + dir[1]]

        if lab[next[0]][next[1]] == " " or lab[next[0]][next[1]] == "A" or lab[next[0]][next[1]] == "v":
            # Checking if the current path is shorter than the best path
            # The -1 is because the append only happens after the check
            if best_path == None or len(path) < len(best_path) - 1:
                path.append(next)

                if lab[next[0]][next[1]] != "A":
                    lab[next[0]][next[1]] = "V"

                find_way(lab, path)

                path.pop()
                if lab[next[0]][next[1]] != "A":
                    lab[next[0]][next[1]] = "v"

    return False

if __name__ == '__main__':
    basic_io.start()

    lab, entryPos = read_map("Blatt 12\\maze_big.txt")

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

    find_way(lab, [entryPos])
    
    draw_map(lab, mapObjs, horizontalOffset, verticalOffset)
    time.sleep(1)

    labCopy = [row[:] for row in lab]

    for pos in best_path:
        labCopy[pos[0]][pos[1]] = "E"
        draw_map(labCopy, mapObjs, horizontalOffset, verticalOffset)
        time.sleep(0.1)

    basic_io.wait_close()