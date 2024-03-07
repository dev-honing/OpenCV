# 모듈 불러오기
import cv2
import json
import numpy as np

# 원본 이미지 불러오기
img = cv2.imread('lake.jpg')

# 그레이스케일링
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  그레이스케일링된 이미지 저장
cv2.imwrite('gray_lake.jpg', gray_img)
