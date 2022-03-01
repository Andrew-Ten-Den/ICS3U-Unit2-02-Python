#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: March 1 2022
# This program calculates the area and perimeter of a rectangle
# with length and width inputted from the user


def main():
    # This program calculates the area and the perimeter of a rectangle

    # input
    length = int(input("Enter length of the rectangle (cm): "))
    width = int(input("Enter width of the rectangle (cm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {} cm².".format(area))
    print("Perimeter is {} cm.".format(perimeter))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
