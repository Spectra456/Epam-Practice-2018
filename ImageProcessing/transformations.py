from PIL import Image, ImageDraw, ImageEnhance
import math
import numpy as np


def rescale(r, g, b):
    return 0.2126 * r, 0.7152 * g, 0.0722 * b

def properities(filename):

    image = Image.open(filename)
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
            a = pixel[i, j][0]
            b = pixel[i, j][1]
            c = pixel[i, j][2]

            a, b, c = rescale(a, b, c)

            S = int(((a + b + c) / 255) ** (1 / factor) * 255)

            draw.point((i, j), (S, S, S))


    return image


def Log(file):
    image, draw, width, height, pixel = properities(file)
    array = np.asarray(image)

    for i in range(width):

        for j in range(height):
            a = pixel[i, j][0]
            b = pixel[i, j][1]
            c = pixel[i, j][2]
            a, b, c = rescale(a, b, c)
            S = a + b + c

            draw.point((i, j), (
                int(255 * (math.log(1 + S, 100))), int(255 * (math.log(1 + S, 100))),
                int(255 * (math.log(1 + S, 100)))))

    return image


def Linear(file):
    image = Image.open(file)
    image = image.convert('L')
    contr = ImageEnhance.Contrast(image)
    image = contr.enhance(1.2)
    bright = ImageEnhance.Brightness(image)
    image = bright.enhance(1.7)

    return image