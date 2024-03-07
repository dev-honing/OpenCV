import json
import matplotlib.pyplot as plt

# JSON 파일 읽기
with open('color_codes.json', 'r') as f:
    color_codes = json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)
    
#  두 리스트의 차이 계산
diff = [i - j for i, j in zip(color_codes, gray_color_codes)]

# 차이를 그래프로 표현
plt.figure(figsize=(10, 5))
plt.plot(diff)
plt.title("Color Codes Difference")
plt.xlabel("Pixel")
plt.ylabel("Difference")
plt.show()