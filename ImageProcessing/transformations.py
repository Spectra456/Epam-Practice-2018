import random
from PIL import Image, ImageDraw, ImageEnhance
import math
import numpy as np


def properities(file):
    image = Image.open(file)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pixel = image.load()

    return (image, draw, width, height, pixel)


def Negative(file):
    image, draw, width, height, pixel = properities(file)

    for i in range(width):
        for j in range(height):
            a = pixel[i, j][0]
            b = pixel[i, j][1]
            c = pixel[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))

    return image


def Gamma(file, factor):
    image, draw, width, height, pixel = properities(file)

    for i in range(width):
        for j in range(height):
            a = pixel[i, j][0] + factor
            b = pixel[i, j][1] + factor
            c = pixel[i, j][2] + factor

            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255

            draw.point((i, j), (a, b, c))

    return image


def Log(file):
    image, draw, width, height, pixel = properities(file)
    array = np.asarray(image)

    for i in range(width):
        for j in range(height):
            a = pixel[i, j][0]
            b = pixel[i, j][1]
            c = pixel[i, j][2]
            S = a * 0.2126 + b * 0.7152 + c * 0.0722

            draw.point((i, j), (
            int(255 * (math.log(2 + S, 100))), int(255 * (math.log(2 + S, 100))), int(255 * (math.log(2 + S, 100)))))

    return image


def Linear(file):
    image = Image.open(file)
    image = image.convert('L')
    contr = ImageEnhance.Contrast(image)
    image = contr.enhance(1.2)
    bright = ImageEnhance.Brightness(image)
    image = bright.enhance(1.7)
    # im.show()
    return image