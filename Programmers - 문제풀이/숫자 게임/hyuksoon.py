def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in A:
        while B:
            target=B.pop()
            if target>i:
                answer+=1
                break
    return answer