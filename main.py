import cv2

# 이미지 불러오기
img = cv2.imread('lake.jpg')

# 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지 표시(새 창에서 이미지 열기)
cv2.imshow('Original image', img)
cv2.imshow('Gray image', gray)

# 키보드 입력으로 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()