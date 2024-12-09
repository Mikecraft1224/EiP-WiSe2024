from jguvc_eip import basic_io as bio   


if __name__ == "__main__":
    bio.start()
    
    dvd = bio.load_image("Blatt 05/dvd_selfmade.png")
    bio.draw_image(295, 215, dvd)

    bio.wait_close()