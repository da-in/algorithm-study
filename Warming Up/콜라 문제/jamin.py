def solution(a, b, n):
    answer = 0

    while n>= a:
        m = n%a
        n = (n//a)*b
        answer += n
        n += m
    return answer