'''
 파일명 :Ex02-1.py
 개요 : 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
 작성자 : 김지우
 최초 직성일 : 2023년 1월 28일
'''

import math

def get_area(radius):
    """반지름을 입력받아 원의 넓이를 반환하는 get_area()함수"""
    area=math.pi*math.pow(radius, 2)
    return area

radius = 1.5
area =get_area(radius)
print(area)

print(get_area.__doc__) # DocString
