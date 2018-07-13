import cv2
from PIL import Image, ImageChops
import os


def averaging(dir):
    allfiles = os.listdir(dir)
    imlist = [filename for filename in allfiles if filename[-4:] in [".png", ".PNG"]]
    dir = dir + "/"
    N = len(imlist)
    avg = Image.open(dir + imlist[0])

    for im in imlist:
        img = Image.open(dir + im)
        avg = Image.blend(avg, img, 1 / N)

    return avg


def difference(im1, im2):
    im1 = Image.open(im1)
    im2 = Image.open(im2)

    return ImageChops.difference(im2, im1)
