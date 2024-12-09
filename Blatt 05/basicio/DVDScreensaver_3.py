from jguvc_eip import basic_io as bio 
import time


if __name__ == "__main__":
    bio.start()
    
    dvd = bio.load_image("Blatt 05/dvd_selfmade.png")
    x = 295
    dx = 5

    while not "q" in bio.get_current_keys_down():
        bio.clear_image()

        bio.draw_image(x, 215, dvd)

        x += dx
        if x + 50 > 615:
            dx = -dx
            x = 565
        elif x < 25:
            dx = -dx
            x = 25

        time.sleep(0.016)

    bio.wait_close()
