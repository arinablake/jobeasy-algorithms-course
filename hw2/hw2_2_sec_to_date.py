# Use datetime library to solve problem Seconds to Date

from datetime import time


def convert(sec):
    sec = sec % (24 * 3600)
    h = sec // 3600
    sec = sec % 3600
    min = sec // 60
    sec = sec % 60
    return time(h, min, sec)


print(convert(8547))
