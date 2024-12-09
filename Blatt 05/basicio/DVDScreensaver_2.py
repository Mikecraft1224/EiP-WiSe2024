from jguvc_eip import basic_io as bio 
import time


if __name__ == "__main__":
    bio.start()
    
    dvd = bio.load_image("Blatt 05/dvd_selfmade.png")
    x = 295

    while not "q" in bio.get_current_keys_down():
        bio.clear_image()

        bio.draw_image(x, 215, dvd)

        x += 5
        time.sleep(0.016)

    bio.wait_close()
