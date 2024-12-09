from jguvc_eip import basic_io as bio 
import time

def check_boundary(coord, delta, maxSize, borderSize=25, size=50):
    if coord + size > maxSize - borderSize:
        delta = -delta
        coord = maxSize - borderSize - size
    elif coord < borderSize:
        delta = -delta
        coord = borderSize
    return coord, delta

if __name__ == "__main__":
    bio.start()
    
    dvd = bio.load_image("Blatt 05/dvd_selfmade.png")
    x = 295
    y = 215

    dx = 5
    dy = 5

    corners = 0

    z = True

    while not "q" in bio.get_current_keys_down():
        bio.set_active_image(z)
        bio.set_visible_image(not z)

        bio.clear_image()

        bio.draw_image(x, y, dvd)

        x += dx
        y += dy

        x, ndx = check_boundary(x, dx, 640)
        y, ndy = check_boundary(y, dy, 480)

        if ndx != dx and ndy != dy:
            corners += 1
            bio.print_message(f"Corner hit! ({corners})")
        
        dx = ndx
        dy = ndy

        z = not z
        time.sleep(0.016)

    bio.wait_close()
