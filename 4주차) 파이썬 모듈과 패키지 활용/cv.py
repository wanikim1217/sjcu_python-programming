import cv2
import numpy as np

imageFile = './sjcu_python-programming/data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena color', img)

cv2.imwrite('./sjcu_python-programming/data/Lena.png', img)

imageFile = './data/Lena.png'
img = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Lena gray', img)

cv2.waitKey()
cv2.destroyAllWindows()
