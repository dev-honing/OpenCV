# 모듈 불러오기
import cv2
import json
import numpy as np

# 원본 이미지 불러오기
img = cv2.imread('lake.jpg')

# 그레이스케일링
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 그레이스케일링된 이미지 불러오기
gray_img = cv2.imread('gray_lake.jpg', cv2.IMREAD_GRAYSCALE)

# 빈 리스트 생성
color_codes = []

# 이미지의 모든 픽셀을 순회
for row in gray_img:
    for pixel in row:
        # 픽셀의 색상 코드를 리스트에 추가
        color_codes.append(int(pixel))
        
# 색상 코드 리스트를 JSON에 저장
color_codes_json = json.dumps(color_codes)

# JSON 파일로 저장
with open('gray_color_codes.json', 'w') as f:
    f.write(color_codes_json)