from math import floor,ceil,sqrt
def solution(r1, r2):
    answer = 0
    # answer2=0
    # def isIn1(y,x):
    #     if (y**2)+(x**2)>=r1**2:
    #         return True
    #     return False
    # def isIn2(y,x):
    #     if (y**2)+(x**2)<=r2**2:
    #         return True
    #     return False
        
    
    for i in range(1,r2+1):
        y1 = floor(sqrt((r2**2)-(i**2)))
        y2=0
        if i<=r1:
            y2 =ceil(sqrt((r1**2)-(i**2)))
        answer += y1-y2+1
    return answer*4