# This program calculates the volume of a cylinder given RADIUS and HEIGHT
# Cylinder volume = pi * radius ** 2 * height
# Source: https://www.youtube.com/watch?v=cdblJqEUDNo

import math
import argparse

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

parser = argparse.ArgumentParser(description="Calculate volume of a cylinder")
parser.add_argument("-r", "--radius", type=int, help="Radius of cylinder")
parser.add_argument("-H", "--height", type=int, help="Height of cylinder")
args = parser.parse_args()

if __name__ == "__main__":
    # print(cylinder_volume(2, 4)) # hard coded values
    print(cylinder_volume(args.radius, args.height)) # with argparser

# sample input
# python3 argparser-demo.py -r 2 -H 4
