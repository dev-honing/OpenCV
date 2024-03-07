import json
import matplotlib.pyplot as plt

# JSON 파일 읽기
with open('color_codes.json', 'r') as f:
    color_codes = json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)
    
# 리스트 길이 확인
print(len(color_codes))
print(len(gray_color_codes))
