import cv2
import numpy as np

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena color', img)

cv2.imwrite('./data/Lena.png', img) # 위에서 읽은 lena.png 파일을 Lena.png로 새롭게 저장

imageFile = './data/Lena.png' # 위에서 새로 저장한 Lena.png파일을 변수에 넣어 불러옴
img = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE) # imread함수를 사용하여 imageFile 변수에 새롭게 넣은 Lena.png파일을 Grayscale 색상으로 읽어옴
cv2.imshow('Lena gray', img) # Grayscale 색상으로 가지고 온 Lena.png파일을 띄어달라는 명령어

cv2.waitKey() # 사용자가 어떤 키든 입력하기만을 기다려라
cv2.destroyAllWindows() # 어떤 키든 입력하기만 하면 모든 윈도우를 닫아라
