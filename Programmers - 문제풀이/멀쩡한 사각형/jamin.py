# y = -(h/w)*x + h

import math 
def solution(w,h):
    answer = w*h
    
    # 가로, 세로가 같다면 한 줄당 한 칸씩 사용 불가능
    if w==h:
        return w*h - w
    
    # 세로가 더 길도록 조정
    if w>h:
        w,h = h,w
    # 가로 길이만큼 반복하며 빠지는 사각형 갯수 계산
    for i in range(1,w+1):
        rec = math.ceil(h*i/w) - math.floor(h*(i-1)/w)
        answer -= rec
        
    return answer