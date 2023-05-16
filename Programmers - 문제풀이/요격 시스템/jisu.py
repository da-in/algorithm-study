def solution(targets):

    targets.sort(key = lambda x : (x[1], x[0])) # 미사일 범위 끝 기준으로 정렬 후 앞에서 부터 접근
    bullet = 0
    before_end = 0
    for target in targets:
        if target[0] < before_end:              # 현재 바라보고 있는 미사일의 시작 부분이 이전 미사일의 끝 부분보다 작다면 
            continue                            # 스플래쉬로 터짐
        else:                                   # 안겹치면
            before_end = target[1]              
            bullet += 1                         # 한 발 더 쏴야함
    return bullet
        
case1 = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]] # 3
case2 = [[0, 4], [1, 2], [1, 3], [3, 4]] # 2
case3 = [[0, 4], [0, 1], [2, 3]] # 2
print(solution(case1))
print(solution(case2))
print(solution(case3))