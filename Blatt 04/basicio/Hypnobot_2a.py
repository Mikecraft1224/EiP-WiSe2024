import math

def calc_fi(h, alpha):
    alpha = alpha + math.pi / 2
    f = math.cos(alpha) * h
    i = math.sin(alpha) * h

    return f, i