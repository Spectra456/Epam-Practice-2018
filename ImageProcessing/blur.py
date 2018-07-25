from PIL import Image, ImageChops
import cv2
def blurAuto(filename, size):

    defaultSize = 1
    defaultDiff = 1

    border = findBorder(defaultDiff, defaultSize, size)

    height, img, pixel, newimg, width = init(filename, size)

    for i in range(border, width - border):

        for j in range(border, height - border):

            counter = 0

            '''''''''''''''''''''''''''''''''''''''''''''
            Getting values of pixels before central pixel.
            '''''''''''''''''''''''''''''''''''''''''''''
            for first in range(-border, 0):

                for second in range(-border, 0):
                    pixel[counter] = img.getpixel((i + first, j + second))
                    counter = counter + 1
                    pixel[counter] = img.getpixel((i + first, j - second))
                    counter = counter + 1

                pixel[counter] = img.getpixel((i + first, j))
                counter = counter + 1

            '''''''''''''''''''''''''''''''''''''''''''''
               Getting values of pixels central pixel.
            '''''''''''''''''''''''''''''''''''''''''''''

            first = 0

            for second in range(-border, 0):
                pixel[counter] = img.getpixel((i - first, j + second))
                counter = counter + 1

                pixel[counter] = img.getpixel((i - first, j - second))
                counter = counter + 1

            pixel[counter] = img.getpixel((i - first, j))
            counter = counter + 1

            '''''''''''''''''''''''''''''''''''''''''''''
            Getting values of pixels after central pixel.
            '''''''''''''''''''''''''''''''''''''''''''''

            for first in range(-border, 0):

                for second in range(-border, 0):
                    pixel[counter] = img.getpixel((i - first, j + second))
                    counter = counter + 1

                    pixel[counter] = img.getpixel((i - first, j - second))
                    counter = counter + 1

                pixel[counter] = img.getpixel((i - first, j))
                counter = counter + 1

            pixel.sort()

            newimg.putpixel((i, j), (pixel[int((((size * size) - 1) / 2) + 1)]))

    return newimg


def init(filename, size):
    img = Image.open(filename)
    width = img.size[0]
    height = img.size[1]

    members = [(0, 0)] * size * size
    newimg = Image.new("RGB", (width, height), "white")

    return height, img, members, newimg, width


def findBorder(defaultDiff, defaultSize, size):
    while True:

        if (defaultSize == size):
            border = defaultSize - defaultDiff
            break

        defaultSize = defaultSize + 2
        defaultDiff = defaultDiff + 1

    return border


def gaussianBlur(filename, size):
    img = cv2.imread(filename, 0)

    return cv2.GaussianBlur(img, (size, size), 0)
