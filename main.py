# 모듈 불러오기
import cv2
import json

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
with open('color_codes.json', 'w') as f:
    f.write(color_codes_json)