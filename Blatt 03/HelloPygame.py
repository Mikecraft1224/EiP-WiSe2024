import pygame as pg


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Pygame Window")

    while True:
        # Auf Fenster schließen hören
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        # Bildschirm leeren
        screen.fill((255, 255, 255))

        # Rotes Rechteck
        pg.draw.rect(screen, (255, 0, 0), (150, 200, 500, 200), 5)

        # Hello World Text
        font = pg.font.Font(None, 64)
        text = font.render("Hello World!", True, (0, 0, 0))
        rect = text.get_rect(center=(400, 300))
        screen.blit(text, rect)

        # Bildschirm updaten
        pg.display.update()
