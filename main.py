import cv2

# 이미지 불러오기
img = cv2.imread('lake.jpg')

# 이미지 회전
# 이미지 중심점 구하기
(height, width) = img.shape[:2]
center = (width / 2, height / 2)

# 180도 회전 매트릭스를 생성
M = cv2.getRotationMatrix2D(center, 180, 1.0)

# 회전 매트릭스를 이미지에 적용
rotated = cv2.warpAffine(img, M, (width, height))

# 회전된 이미지 저장
cv2.imwrite('rotated.jpg', rotated)