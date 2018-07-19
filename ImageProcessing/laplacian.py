import cv2 as cv


def laplacian(filename):

    depth = cv.CV_16S
    kernel_size = -1

    src = cv.imread(filename, 0)

    #src = cv.GaussianBlur(src, (3, 3), 0) # if you need to remove noises
    dst = cv.Laplacian(src, depth, kernel_size)
    abs_dst = cv.convertScaleAbs(dst)

    return abs_dst






