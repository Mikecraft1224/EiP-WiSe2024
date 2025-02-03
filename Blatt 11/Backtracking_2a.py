from jguvc_eip import basic_io

def read_map(filename):
    lab = []

    # einlesen der map aus textdatei
    with open(filename, 'r') as f:
        for line in f:
            lab.append([char for char in line][:-1])
    return lab

def find_way(lab, path: list):
    last = path[-1]

    if lab[last[0]][last[1]] == 'A':
        return path
    
    for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next = [last[0] + dir[0], last[1] + dir[1]]

        if lab[next[0]][next[1]] != " " and lab[next[0]][next[1]] != "A":
            continue

        path.append(next)

        if lab[next[0]][next[1]] != "A":
            lab[next[0]][next[1]] = "X"

        result = find_way(lab, path)
        if result:
            return result
        path.pop()

        lab[next[0]][next[1]] = " "

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
    
    path = find_way(lab, [entryPos])
    basic_io.print_message("Path: " + str(path))

    basic_io.wait_close()