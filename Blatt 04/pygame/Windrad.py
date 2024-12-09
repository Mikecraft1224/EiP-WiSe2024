import pygame
import math
import time

def rotatePoint(point, angle):
    xr = (point[0] - 320) * math.cos(angle) - (point[1] - 240) * math.sin(angle) + 320
    yr = (point[0] - 320) * math.sin(angle) + (point[1] - 240) * math.cos(angle) + 240

    return (int(xr), int(yr))

def drawRotRectangle(screen, angle):
    rect = [
        (270, 190),
        (370, 190),
        (370, 290),
        (270, 290)
    ]

    for i in range(len(rect)):
        rect[i] = rotatePoint(rect[i], angle)

    pygame.draw.polygon(screen, (0, 0, 0), rect)

def drawRotTriangle(screen, angle, tri_center, color):
    tri = [
        (tri_center[0] - 25, tri_center[1] - 50),
        (tri_center[0] + 25, tri_center[1] + 50),
        (tri_center[0] - 25, tri_center[1] + 50)
    ]

    for i in range(len(tri)):
        tri[i] = rotatePoint(tri[i], angle)

    pygame.draw.polygon(screen, color, tri)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))

        drawRotRectangle(screen, angle)
        drawRotTriangle(screen, angle, (345, 140), (255, 0, 0))
        drawRotTriangle(screen, angle + math.pi/2, (345, 140), (0, 255, 0))
        drawRotTriangle(screen, angle + math.pi, (345, 140), (255, 255, 0))
        drawRotTriangle(screen, angle + 3*math.pi/2, (345, 140), (0, 0, 255))

        angle += 0.05

        pygame.display.flip()
        time.sleep(0.016)


if __name__ == "__main__":
    main()