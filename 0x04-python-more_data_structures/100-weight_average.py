#!/usr/bin/python3
def weight_average(my_list=[]):
    top = 0
    down = 0
    if not my_list or len(my_list) == 0:
        return 0
    for i in my_list:
        top = top + (i[0] * i[1])
        down = down + i[1]
    return top/down
