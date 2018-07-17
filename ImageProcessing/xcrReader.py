import struct
import imageio
import numpy as np
from PIL import Image


def xcr_reader(file_path: str, col_num: int, row_num: int, offset: int = 0, reversed: bool = False) -> (
        int, int, int, np.ndarray, np.ndarray, Image):
    """
    Read XCR image
    :param file_path: path to XCR file
    :param col_num: number of columns in img
    :param row_num: number of rows in img
    :param offset: offset from begin (for header)
    :param reversed: if bytes are reversed in image
    :return: (columns_number, rows_number, depth, image_array)
    """
    with open(file_path, 'rb') as f:
        data = f.read()

    image_len = col_num * row_num

    depth = 16

    image_data = list(data[offset:(offset + image_len * 2)])

    if reversed:
        for i in range(0, len(image_data), 2):
            image_data[i], image_data[i + 1] = image_data[i + 1], image_data[i]

    image_data = list(struct.unpack(str(image_len) + "H", bytes(image_data)))
    image_data = np.array(image_data).reshape((col_num, row_num))

    image_data = np.flipud(image_data)

    min_el = float(image_data[0, 0])
    max_el = float(image_data[0, 0])

    for i in range(0, col_num, 1):
        for j in range(0, row_num, 1):
            value = float(image_data[i, j])
            if value < min_el:
                min_el = value
            if value > max_el:
                max_el = value

    if max_el == min_el:
        min_el = 0
        max_el = max_el if max_el > 0 else 1

    target_data = image_data
    for i in range(0, col_num, 1):
        for j in range(0, row_num, 1):
            value = image_data[i, j]
            value = int((float(value - min_el) / float(max_el - min_el)) * 255)
            target_data[i, j] = value

    img = Image.new('L', (col_num, row_num))
    imageio.imwrite('out_file.jpg', image_data)

    return image_data
