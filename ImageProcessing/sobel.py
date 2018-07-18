from PIL import Image
import math


def init(filename):
    img = Image.open(filename)
    width = img.size[0]
    height = img.size[1]

    newimg = Image.new("RGB", (width, height), "white")

    return height, img, newimg, width


def sobelOperator(filename):
    height, img, newimg, width = init(filename)

    for x in range(1, width - 1):

        for y in range(1, height - 1):
            Gx = 0
            Gy = 0

            '''''''''''''''''''''''''''''''''''''''''''''''
            Getting values of  pixels before central pixel.
            '''''''''''''''''''''''''''''''''''''''''''''''

            p = img.getpixel((x - 1, y - 1))
            r = p[0]
            g = p[1]
            b = p[2]

            intensity = r + g + b

            Gx += -intensity
            Gy += -intensity

            p = img.getpixel((x - 1, y))
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -2 * (r + g + b)

            p = img.getpixel((x - 1, y + 1))
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += -(r + g + b)
            Gy += (r + g + b)

            '''''''''''''''''''''''''''''''''''''''''''''
            Getting values of central pixels.
            '''''''''''''''''''''''''''''''''''''''''''''
            p = img.getpixel((x, y - 1))
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += -2 * (r + g + b)

            p = img.getpixel((x, y + 1))
            r = p[0]
            g = p[1]
            b = p[2]

            Gy += 2 * (r + g + b)

            '''''''''''''''''''''''''''''''''''''''''''''
            Getting values of pixels after central pixel.
            '''''''''''''''''''''''''''''''''''''''''''''

            p = img.getpixel((x + 1, y - 1))
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (r + g + b)
            Gy += -(r + g + b)

            p = img.getpixel((x + 1, y))
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += 2 * (r + g + b)

            p = img.getpixel((x + 1, y + 1))
            r = p[0]
            g = p[1]
            b = p[2]

            Gx += (r + g + b)
            Gy += (r + g + b)

            # calculate the length of the gradient (Pythagorean theorem)
            length = math.sqrt((Gx * Gx) + (Gy * Gy))

            length = length / 4328 * 255

            length = int(length)

            newimg.putpixel((x, y), (length, length, length))

    return newimg
