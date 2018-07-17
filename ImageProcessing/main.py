import ImageProcessing.zoom as z
import ImageProcessing.transformations as t
import ImageProcessing.histograms as h
import ImageProcessing.operations as o
import ImageProcessing.blur as b

import scipy

import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as P

FILE_NAME = "assets/example.png"

# plt.imshow(t.Negative(FILE_NAME))
# plt.imshow(t.Gamma(FILE_NAME, 1.2))
# plt.imshow(t.Log(FILE_NAME))
# plt.imshow(t.Linear(FILE_NAME))
# plt.imshow(h.equalize(FILE_NAME),cmap ="gray")
# plt.imshow(h.addMask(FILE_NAME), cmap="gray   ")
# plt.imshow(o.averaging("C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/assets/rails"))
# plt.imshow(o.difference('C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/assets/scene00769.png','C:/Users/Spectra/PycharmProjects/Epam-Practice-2018/ImageProcessing/assets/scene00777.png'),cmap="gray")
# plt.imshow(z.zoom(FILE_NAME,2,2))
b = b.blurAuto(FILE_NAME, 3)

P._show(b)
