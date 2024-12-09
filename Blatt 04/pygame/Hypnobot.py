import pygame
import math
import time

phimax = math.pi / 2
o = 1

def calc_fi(h, alpha):
    alpha = alpha + math.pi / 2
    
    f = math.cos(alpha) * h
    i = math.sin(alpha) * h

    return int(f), int(i)

def drawConcentricCircle(screen, t, circleCenter):
    for r, color in zip([100, 80, 60, 40, 20], [(0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 165, 0), (255, 0, 0)]):
        pygame.draw.circle(screen, color, circleCenter, (r - int(t*60))%101, 1)

def drawPendulum(screen, alpha, pendulumCenter, h, t):
    f, i = calc_fi(h, alpha)
    
    pygame.draw.line(screen, (0, 0, 0), pendulumCenter, (pendulumCenter[0] + f, pendulumCenter[1] + i))
    drawConcentricCircle(screen, t, (pendulumCenter[0] + f, pendulumCenter[1] + i))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))

        drawPendulum(screen, phimax * math.cos(o * t), (320, 240), 150, t)

        t += 0.016

        pygame.display.flip()
        time.sleep(0.016)


if __name__ == '__main__':
    main()