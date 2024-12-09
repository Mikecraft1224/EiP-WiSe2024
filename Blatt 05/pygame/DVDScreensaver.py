import pygame
import time

def check_boundary(coord, delta, maxSize, borderSize=25, size=50):
    if coord + size > maxSize - borderSize:
        delta = -delta
        coord = maxSize - borderSize - size
    elif coord < borderSize:
        delta = -delta
        coord = borderSize
    return coord, delta

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    dvd = pygame.image.load("Blatt 05/dvd_selfmade.png")
    x = 295
    y = 215

    dx = 5
    dy = 5

    corners = 0

    z = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))

        screen.blit(dvd, (x, y))

        x += dx
        y += dy

        x, ndx = check_boundary(x, dx, 640)
        y, ndy = check_boundary(y, dy, 480)

        if ndx != dx and ndy != dy:
            corners += 1
            print(f"Corner hit! ({corners})")

        dx = ndx
        dy = ndy

        pygame.display.flip()
        time.sleep(0.016)


if __name__ == "__main__":
    main()