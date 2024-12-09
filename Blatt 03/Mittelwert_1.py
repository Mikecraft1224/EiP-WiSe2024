test_list = [7,20,5,-1,3,11,32,17,42]

def simple_mean(l):
    summed = 0

    for i in l:
        summed += i

    return summed / len(l)

def advanced_mean(l):
    return sum(l) / len(l)


if __name__ == '__main__':
    print(f"Einfacher Mittelwert: {simple_mean(test_list)}")
    print(f"Fortgeschrittener Mittelwert: {advanced_mean(test_list)}\n")

    print(f"Einfacher Mittelwert: {simple_mean([i for i in range(100000)])}")
    print(f"Fortgeschrittener Mittelwert: {advanced_mean([i for i in range(100000)])}")