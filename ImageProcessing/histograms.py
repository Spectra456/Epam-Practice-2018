import cv2
import numpy as np


def equalize(filename):

    img = cv2.imread(filename, 0)
    equ = cv2.equalizeHist(img)

    return equ


def addMask(filename, x1, y1, x2, y2):

    img = cv2.imread(filename, 0)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[x1:y1, x2:y2] = 255

    masked_img = cv2.bitwise_and(img, img, mask=mask)
    imgshow = np.hstack((img, mask))
    masked_img = np.hstack((imgshow, masked_img))

    return masked_img
