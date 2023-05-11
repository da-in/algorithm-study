def solution(n):
    answer=''
    
    while n>0:
        rest = n%3
        if rest==0:
            answer+='4'
            n = (n-1)//3
        else:
            answer+=str(rest)
            n//=3
    
    return answer[::-1]