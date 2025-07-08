from adafruit_circuitplayground import cp
import time
import random

def file_opener():
    pattern = []
    # Open
    with open('pattern.txt') as file:
        numbers_index = file.read()
        numbers = numbers_index.split(",")
# Close
    file.close()

    for individual in numbers:
        pattern.append(int(individual))
    return pattern

    # Random Color variations
def pixel_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Runs all the other programs
def main():
    pattern = file_opener()
    while True:
        for pixel in pattern:
            cp.pixels[pixel] = pixel_color()
            time.sleep(0.5)
            cp.pixels[pixel] = (0, 0, 0)

main()
