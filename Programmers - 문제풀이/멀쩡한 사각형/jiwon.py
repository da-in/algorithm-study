import math

def solution(w,h):
    w,h = min(w,h), max(w,h)
    answer = w*h-(math.ceil(h/w))*w
    
    return answer