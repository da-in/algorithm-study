def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        for j in range(r2-1,0,-1):
            temp = (j**2)+(i**2)
            if temp<r1**2:
                break
            if temp<=r2**2:
                answer+=1
        
    return (answer+(r2-r1+1))*4