import pygame
import time

def drawCar(screen, x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 150, 50))
    pygame.draw.circle(screen, (0, 0, 0), (x + 25, y + 50), 12.5)
    pygame.draw.circle(screen, (0, 0, 0), (x + 125, y + 50), 12.5)

def drawHouse(screen, x, y):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 150, 150))
    pygame.draw.polygon(screen, (0, 0, 255), [(x, y), (x + 75, y - 75), (x + 150, y)])

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    carX = 0
    carY = 375
    houseX = 350
    houseY = 300
    front = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))

        if front:
            drawHouse(screen, houseX, houseY)
            drawCar(screen, carX, carY)
        else:
            drawCar(screen, carX, carY)
            drawHouse(screen, houseX, houseY)

        carX += 1
        if carX > 640:
            carX = -150
            front = not front

        pygame.display.flip()
        time.sleep(0.016)


if __name__ == "__main__":
    main()