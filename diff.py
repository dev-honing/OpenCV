import json

# JSON 파일 읽기
with open('color_codes.json', 'r') as f:
    color_codes = json.load(f)
    
with open('gray_color_codes.json', 'r') as f:
    gray_color_codes = json.load(f)
    
# 각 리스트를 비교
if color_codes == gray_color_codes:
    print("두 파일은 같다.")
else: 
    print("두 파일은 다르다.")