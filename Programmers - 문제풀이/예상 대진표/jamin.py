import math
def solution(n,a,b):
    answer = 0
    
    # a<b가 되도록 정렬
    if b<a:
        a,b = b,a
        
    while True:
        if a%2==1 and (b-a)==1:
            break
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
    return answer+1