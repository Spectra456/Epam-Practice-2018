import struct


def fops(filename):
    with open(filename, 'rb') as file:
        num = file.read(4)
        i = 1
        array = []

        while num:
            array.append(struct.unpack(">f", num))
            num = file.read(4)
            i = i + 1

        return array
