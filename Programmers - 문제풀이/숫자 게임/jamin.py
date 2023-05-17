# 사원 짝수
# A팀 출전 순서 정해짐

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    j = 0
    
    for i in A:
        if i<B[j]:
            answer += 1
            j+=1    # 이긴 경우에만 B 인덱스 늘림
            
    return answer