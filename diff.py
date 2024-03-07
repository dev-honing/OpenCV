import json
import itertools
import matplotlib.pyplot as plt

# JSON 파일 읽기
with open('color_codes.json', 'r') as f:
    color_codes = json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)
    
# 평탄화 작업
color_codes_flat = list(itertools.chain.from_iterable(color_codes))

# 평탄화된 리스트를 새로운 JSON 파일로 저장
with open('color_codes_flat.json', 'w') as f:
    json.dump(color_codes_flat, f)