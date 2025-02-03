def read_map(filename):
    m = []

    # einlesen der map aus textdatei
    with open(filename, 'r') as f:
        for line in f:
            m.append([char for char in line][:-1])
    return m


if __name__ == '__main__':
    labyrinth = read_map("Blatt 11\\maze_small.txt")