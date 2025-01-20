def is_double_top(arr_part, tolerance=0.01):
    return arr_part[0] < arr_part[1] \
            and arr_part[1] > arr_part[2] \
            and arr_part[2] < arr_part[3] \
            and abs(arr_part[1] - arr_part[3]) < tolerance
    