import math

def solution(n,a,b):
    answer = 1
    a,b = min(a,b), max(a,b)
    
    while True:
        if a%2==1 and a+1==b:
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer+=1

    return answer