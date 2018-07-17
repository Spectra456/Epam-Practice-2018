from PIL import Image, ImageChops


def blurAuto(filename, size):
    defaultSize = 1
    defaultDiff = 1

    while True:

        if (defaultSize == size):
            border = defaultSize - defaultDiff
            break

        defaultSize = defaultSize + 2
        defaultDiff = defaultDiff + 1

    img = Image.open(filename)

    width = img.size[0]
    height = img.size[1]

    members = [(0, 0)] * size * size
    newimg = Image.new("L", (width, height), "white")

    for i in range(border, width - border):

        for j in range(border, height - border):

            counter = 0

            for first in range(-border, 0):

                for second in range(-border, 0):
                    members[counter] = img.getpixel((i + first, j + second))
                    counter = counter + 1

                members[counter] = img.getpixel((i + first, j))
                counter = counter + 1

                for second in range(-border, 0):
                    members[counter] = img.getpixel((i + first, j - second))
                    counter = counter + 1

            first = 0

            for second in range(-border, 0):
                members[counter] = img.getpixel((i - first, j + second))
                counter = counter + 1

            members[counter] = img.getpixel((i - first, j))
            counter = counter + 1

            for second in range(-border, 0):
                members[counter] = img.getpixel((i - first, j - second))
                counter = counter + 1

            for first in range(-border, 0):

                for second in range(-border, 0):
                    members[counter] = img.getpixel((i - first, j + second))
                    counter = counter + 1

                members[counter] = img.getpixel((i - first, j))
                counter = counter + 1

                for second in range(-border, 0):
                    members[counter] = img.getpixel((i - first, j - second))
                    counter = counter + 1

            members.sort()

            newimg.putpixel((i, j), (members[int((((size * size) - 1) / 2) + 1)]))

    return newimg
