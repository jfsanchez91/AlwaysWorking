#!/usr/bin/env python3

import mouse
import sys
import time
import random

from screeninfo import get_monitors


def exit(status=0, message=""):
    if status != 0:
        print("[ERROR]:", message)
    sys.exit(status)


def main():
    monitors = get_monitors()
    monitors_length = len(monitors)
    if monitors_length <= 0:
        exit(-1, "Unable to find the monitors information.")

    width=monitors[0].width
    height=monitors[0].height

    if monitors_length > 1:
        for m in monitors[1:]:
            width = min(width, m.width)
            height = min(height, m.height)

    print("width:", width)
    print("height:", height)

    min_width = width / 4
    min_height = height / 4

    max_width = min_width * 3
    max_height = min_height * 3
    
    while True:
        next_width = random.randint(min_width, max_width)
        next_height = random.randint(min_height, max_height)
        mouse.move(next_width, next_height)
        time.sleep(1)


if __name__ == '__main__':
    main()
