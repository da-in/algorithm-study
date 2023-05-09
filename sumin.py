"""
전에 풀어봤던 문제였고, 처음 풀었을 때 풀이참조
이번에 다시 풀었을 때, 주석까지 세세하게 다는 데 1시간 정도 걸림
<solution>
1. 가장 먼 집부터 방문하기
2. 배달과 수거를 분리해서 생각(트럭이 실을 수 있는 최대용량)
-> 시간복잡도: O(n)

<input>
- cap: 최대 실을 수 있는 상자 개수(최대 50)
- n: 배달할 집의 개수(최대 10만) -> 최대 O(NlogN) 알고리즘
- deliveries: 배달할 재활용 택배 상자의 개수(최대 50)
- pickups: 수거할 빈 재활용 택배 상자의 개수(최대 50)
"""
def solution(cap, n, deliveries, pickups):
    answer = 0  # 물류창고까지 돌아올 수 있는 최소 이동 거리
    i, j = n-1, n-1 # 배달/수거할 가장 먼 곳
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    while j >= 0 and pickups[j] == 0:
        j -= 1

    while i >= 0 or j >= 0: # 배달 또는 수거해야할 집이 있으면 계속 반복
        answer += (max(i, j) + 1) * 2 # 물류창고까지 다시 돌아와야 하기 때문에 항상 왕복거리 계산
        # print(i, j)
        # 배달
        cur = cap # 항상 최대 용량 배달
        while i >= 0 and cur: # 배달해야할 집이 있는 경우 & 트럭 용량이 될 때
            # print(i, cur, deliveries)
            if deliveries[i] > cur: # 해당 집에 배달할 상자가 트럭 용량보다 더 큰 경우
                deliveries[i] -= cur
                cur = 0 # 트럭 용량 꽉 참
            else:
                cur -= deliveries[i]
                deliveries[i] = 0 # i번째 집 배달 완료
                while i >= 0 and deliveries[i] == 0:
                    i -= 1
        # 수거
        cur = cap # 항상 최대 용량 수거
        while j >= 0 and cur: # 수거해야할 집이 있는 경우 & 트럭 용량이 될 때
            # print(j, cur, pickups)
            if pickups[j] > cur:
                pickups[j] -= cur
                cur = 0
            else:
                cur -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1

    return answer


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))