import ImageProcessing.zoom as z
import ImageProcessing.transformations as t
import cv2
import matplotlib.pyplot as plt

FILE_NAME = "assets/star.jpg"

array = cv2.imread(FILE_NAME, 1)
# plt.imshow(t.Negative(FILE_NAME))
# plt.imshow(t.Gamma(FILE_NAME, -50))
plt.imshow(t.Log(FILE_NAME))
# plt.imshow(z.zoom(array,5,1))
plt.show()
