# 작은 반지름보다 x값이 작으면 y값이 x값일 때 y값보다 크고 큰 원보단 작아야함
# x^2 + y^2 = r^2
# y = math.sqrt(r^2 - x^2)
# x=1 일 때, 1 + y^2 = 4, 
# x=0, y=0은 배제하고 생각

import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1,r2+1):     #x축, y축 위의 점이 1번만 세어지도록 범위 설정
        if x>r1:
            y1 = 0
        else:
            y1 = math.sqrt(r1*r1 -x*x)
        y2 = math.sqrt(r2*r2 -x*x)
        
        answer += math.floor(y2) - math.ceil(y1) +1     #여기가 핵심! y1과 y2를 각각 정수로 만들어준 뒤 사이값 계산
        
    return answer*4