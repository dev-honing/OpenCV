# 모듈 불러오기
import cv2
import json
import numpy as np

# 이미지 불러오기
img = cv2.imread('lake.jpg')

# 빈 리스트 생성
color_codes = []

# 이미지의 모든 픽셀을 순회
for row in img:
    for pixel in row:
        # 픽셀의 색상 코드를 리스트에 추가
        color_codes.append(tuple(map(int, pixel)))
        
# 색상 코드 리스트를 JSON에 저장
color_codes_json = json.dumps(color_codes)

# JSON 파일로 저장
# with open('color_codes.json', 'w') as f:
#     f.write(color_codes_json)
    
# # 이미지 크기 출력
# height, width, _ = img.shape
# print(f" 이미지 크기: {height} x {width}") # 이미지 크기: 3648 x 5472

# JSON 파일 읽기
with open('color_codes.json', 'r') as f:
    color_codes_json = f.read()

# 원본 이미지 크기로 새 이미지를 생성
height, width = 3648, 5472
new_img = np.zeros((height, width, 3), np.uint8)

# 색상 코드를 사용해 이미지의 각 픽셀을 설정
for i in range(height):
    for j in range(width):
        new_img[i, j] = color_codes[i * width + j]

# 재구현한 이미지를 저장
cv2.imwrite('new_img2.jpg', new_img)