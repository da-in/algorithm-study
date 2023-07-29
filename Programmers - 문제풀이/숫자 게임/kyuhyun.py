def solution(A, B):
    answer = 0
    if min(B) > max(A) :
        return len(B)

    st_a = 0
    st_b = 0

    A.sort()
    B.sort()

    while st_a < len(A) and st_b < len(B):
        if A[st_a] >= B[st_b]:
            st_b += 1
        else:
            answer += 1
            st_a += 1
            st_b += 1

    return answer