import PIL
import cv2


def zoom(filename, coefficient, type):
    file = cv2.imread(filename, 1)
    if type == 1:
        return cv2.resize(file, (0, 0), fx=coefficient, fy=coefficient, interpolation=cv2.INTER_NEAREST)
    if type == 2:
        return cv2.resize(file, (0, 0), fx=coefficient, fy=coefficient, interpolation=cv2.INTER_LINEAR)
