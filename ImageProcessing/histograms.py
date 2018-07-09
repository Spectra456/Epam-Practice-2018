import cv2
import numpy as np


def equalize(filename):
    img = cv2.imread(filename, 0)
    equ = cv2.equalizeHist(img)
    equ = np.hstack((img, equ))  # ВАЖНО
    return equ


def addMask(filename):
    img = cv2.imread(filename, 0)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:200, 100:300] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    imgshow = np.hstack((img, mask))
    masked_img = np.hstack((imgshow, masked_img))
    return masked_img
