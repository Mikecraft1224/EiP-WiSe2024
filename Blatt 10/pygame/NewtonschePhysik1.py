import pygame
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    ballY = 40
    ballVelocity = 0
    ballAcceleration = 0.1
    ballMaxVelocity = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((255, 255, 255))

        # Drawing
        pygame.draw.rect(screen, (0, 0, 0), (300, 50, 40, 40))
        pygame.draw.rect(screen, (0, 0, 0), (320, 70, 2, 300))
        pygame.draw.rect(screen, (0, 0, 0), (300, 370, 40, 40))

        # Moving the ball
        if ballY < 280:
            # Changing velocity
            if ballVelocity < ballMaxVelocity:
                ballVelocity += ballAcceleration

            # Adjusting velocity
            if ballY + int(ballVelocity) > 300:
                ballVelocity = 300 - ballY

            ballY += int(ballVelocity)

        pygame.draw.circle(screen, (255, 0, 0), (320, 50 + ballY + 20), 20)

        pygame.display.flip()
        time.sleep(0.016)


if __name__ == '__main__':
    main()