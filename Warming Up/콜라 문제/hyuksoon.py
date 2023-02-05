def solution(a, b, n):
    answer = 0
    while n>=a:
        plus=(n//a)*b
        temp=n%a
        answer+=plus
        n=plus+temp
        
    return answer