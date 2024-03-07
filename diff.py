import json
import itertools
import matplotlib.pyplot as plt

# JSON 파일 읽기
with open('color_codes_flat.json', 'r') as f:
    color_codes_flat =  json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)

# 각 리스트의 길이 확인
print(len(color_codes_flat)) # 59885568
print(len(gray_color_codes)) # 19961856

# 각 리스트의 첫 번째 요소의 타입 확인
print(type(color_codes_flat[0])) # <class 'int'>
print(type(gray_color_codes[0])) # <class 'int'>
