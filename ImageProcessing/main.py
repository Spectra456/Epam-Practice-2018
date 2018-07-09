import ImageProcessing.zoom as z
import ImageProcessing.transformations as t
import ImageProcessing.histograms as h

import cv2
import matplotlib.pyplot as plt

FILE_NAME = "assets/hills.jpg"


# plt.imshow(t.Negative(FILE_NAME))
# plt.imshow(t.Gamma(FILE_NAME, -50))
# plt.imshow(t.Log(FILE_NAME))
# plt.imshow(t.Linear(FILE_NAME))
# plt.imshow(h.equalize(FILE_NAME),cmap ="gray")
plt.imshow(h.addMask(FILE_NAME), cmap="gray")
# plt.imshow(z.zoom(FILE_NAME,2,2))
plt.show()
