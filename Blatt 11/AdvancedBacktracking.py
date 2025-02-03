from jguvc_eip import basic_io, image_objects as iobj
from jguvc_eip.colors import *
import time

class Map:
    def __init__(self, filename):
        self.read_map(filename)

        # Calculating square size and offsets
        self.squareSize = 640//len(self.lab[0]) if 640//len(self.lab[0]) < 480//len(self.lab) else 480//len(self.lab)
        self.horizontalOffset = (640 - self.squareSize * len(self.lab[0])) // 2
        self.verticalOffset = (480 - self.squareSize * len(self.lab)) // 2

        # Creating map objects to use
        self.borderThickness = self.squareSize//10

        self.mapObjs = {
            ".": iobj.Rectangle(self.squareSize, self.squareSize, fill_color=BLACK),
            "E": iobj.Rectangle(self.squareSize, self.squareSize, fill_color=RED, 
                                border_color=BLACK, border_thickness=self.borderThickness),
            "A": iobj.Rectangle(self.squareSize, self.squareSize, fill_color=BLUE, 
                                border_color=BLACK, border_thickness=self.borderThickness),
            " ": iobj.Rectangle(self.squareSize, self.squareSize, fill_color=WHITE, 
                                border_color=BLACK, border_thickness=self.borderThickness),
            "V": iobj.Rectangle(self.squareSize, self.squareSize, fill_color=LIGHT_BLUE, 
                                border_color=BLACK, border_thickness=self.borderThickness)
        }

        self.print_map()

    def read_map(self, filename):
        self.lab = []

        # einlesen der map aus textdatei
        with open(filename, 'r') as f:
            for line in f:
                row = []
                for char in line[:-1]:
                    row.append(char)

                    if char == 'E':
                        self.entryPos = [len(self.lab), len(row)-1]
                self.lab.append(row)

    def print_map(self):
        labObjs = []

        for y in range(len(self.lab)):
            rowObjs = []
            for x in range(len(self.lab[y])):
                rowObjs.append(self.mapObjs[self.lab[y][x]])
            labObjs.append(iobj.HorizontalStack(rowObjs))
        
        labObjs = iobj.VerticalStack(labObjs)

        basic_io.draw_object(labObjs, self.horizontalOffset, self.verticalOffset)

    def find_way(self, path=[]):
        if len(path) == 0:
            path.append(self.entryPos)

        last = path[-1]

        if self.lab[last[0]][last[1]] == 'A':
            for pos in path:
                self.lab[pos[0]][pos[1]] = "E"
                self.print_map()
                time.sleep(0.1)

            return path
        
        for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next = [last[0] + dir[0], last[1] + dir[1]]

            if self.lab[next[0]][next[1]] == " " or self.lab[next[0]][next[1]] == "A":
                path.append(next)

                if self.lab[next[0]][next[1]] != "A":
                    self.lab[next[0]][next[1]] = "V"
                    self.print_map()
                    time.sleep(0.1)

                result = self.find_way(path)
                if result:
                    return result
                path.pop()

                self.lab[next[0]][next[1]] = " "
                self.print_map()
                time.sleep(0.1)

        return False

if __name__ == '__main__':
    basic_io.start()

    labMap = Map("Blatt 11\\maze_small.txt")
    basic_io.input_string("")
    labMap.find_way()

    basic_io.wait_close()