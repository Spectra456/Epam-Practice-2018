from PIL import Image

import ImageProcessing.zoom as z
import ImageProcessing.transformations as t
import ImageProcessing.histograms as h
import ImageProcessing.operations as o
import ImageProcessing.blur as b
import ImageProcessing.sobel as s
import ImageProcessing.laplacian as l
import ImageProcessing.noise as n
import image_slicer as sl

import scipy

import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as P




# plt.imshow(t.Negative(FILE_NAME))
# plt.imshow(t.Gamma(FILE_NAME, 1.2))
# plt.imshow(t.Log(FILE_NAME))
# plt.imshow(t.Linear(FILE_NAME))
# plt.imshow(h.addMask(FILE_NAME), cmap="gray   ")
# plt.imsave("sobel/result.png",o.averaging("C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/sobel"))
# plt.imshow(o.difference('C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/assets/scene00769.png','C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/assets/scene00777.png'),cmap="gray")
# plt.imshow(z.zoom(FILE_NAME,2,2))
# plt.imsave("assets/noise/impulseNoiseExample.png",n.impulseNoise("assets/photo2.jpg", 0.2))
# plt.imsave("assets/noise/randomNoiseExample.png",n.randomNoise("assets/photo2.jpg",0.1))
# plt.imshow(n.impulseNoise("assets/HollywoodLC.jpg", 0.7))
# plt.imsave("assets/noise/impulseNoiseExampleFixed.png", (b.blurAuto("assets/noise/impulseNoiseExample.png", 3)))
# plt.imsave("assets/noise/randomNoiseExampleFixedMedian.png", (b.blurAuto("assets/noise/randomNoiseExample.png", 3)),cmap="gray")
# b = s.sobelOperator("assets/final/stones.jpg")
# a = l.laplacian("assets/photo2.jpg")
# A = np.array(a)
# A = A.reshape(A.shape + ())
# с = b.ga

img = z.zoom("assets/final/stones.jpg", 14, 2)
cv2.imwrite("assets/final/stonesZoomed.jpg", img)

imageLinear = t.Linear("assets/final/stonesZoomed.jpg")
imageLinear.save("assets/final/stonesLinear.jpg")

blurred = cv2.imread("assets/final/stonesLinear.jpg")
thresh = cv2.threshold(blurred, 250, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("assets/final/stonesTresh.jpg", thresh)

image = cv2.imread("assets/final/stonesTresh.jpg")
erosion = cv2.Canny(image, 250, 255)
cv2.imwrite("assets/final/stonesEdges.jpg", erosion)

#

original = cv2.imread("assets/final/stonesEdges.jpg", cv2.IMREAD_GRAYSCALE)
retval, image = cv2.threshold(original, 250, 255, cv2.THRESH_BINARY)

el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
image = cv2.dilate(image, el, iterations=6)

cv2.imwrite("assets/final/dilated.png", image)

wtf, contours, hierarchy = cv2.findContours(
    image,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_TC89_L1
)

drawing = cv2.imread("assets/final/stonesEdges.jpg")

centers = []
radii = []
for contour in contours:
    area = cv2.contourArea(contour)

    # there is one contour that contains all others, filter it out
    if (area > 2000 or area < 100):
        continue

    br = cv2.boundingRect(contour)
    radii.append(br[2])

    m = cv2.moments(contour)

    center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))
    print(center)

    centers.append(center)

print("There are {} circles".format(len(centers)))

radius = int(np.average(radii)) + 5

for center in centers:
    cv2.circle(drawing, center, 3, (255, 0, 0), -1)
    cv2.circle(drawing, center, radius, (0, 255, 0), 1)

cv2.imwrite("assets/final/drawing.jpg", drawing)
