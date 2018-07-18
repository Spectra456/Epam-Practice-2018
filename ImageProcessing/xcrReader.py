import struct
import imageio
import numpy as np
from PIL import Image


def xcr_reader(file_path: str, col_num: int, row_num: int, offset: int = 0, reversed: bool = False):

    with open(file_path, 'rb') as f:
        data = f.read()

    image_len = col_num * row_num

    image_data = list(data[offset:(offset + image_len * 2)])

    if reversed:

        for i in range(0, len(image_data), 2):
            image_data[i], image_data[i + 1] = image_data[i + 1], image_data[i]

    image_data = list(struct.unpack(str(image_len) + "H", bytes(image_data)))
    image_data = np.array(image_data).reshape((col_num, row_num))

    image_data = np.flipud(image_data)

    return image_data
