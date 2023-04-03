def solution(n):
    answer = 0
    # 재료: 가로 2, 세로 1
    # 목표: 가로 n, 세로 3
    # 가로, 세로 배치 가능
    i=n//2
    x=1000000007
    if n%2==0:
        for a in range(len(x+1)):
            answer += b**(x-a)*(x-a+1)
        return answer%x
    else:
        return 0