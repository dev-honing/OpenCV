import json
import itertools
import matplotlib.pyplot as plt

# JSON 파일 읽기
with open('color_codes_flat.json', 'r') as f:
    color_codes_flat =  json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)

# 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(color_codes_flat, label='color_codes_flat')
plt.plot(gray_color_codes, label='gray_color_codes')
plt.title('Color Codes')
plt.xlabel('Pixel')
plt.ylabel('Color Code')
plt.legend()
plt.show()