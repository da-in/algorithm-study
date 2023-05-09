"""
    택배 배달과 수거하기
    https://school.programmers.co.kr/learn/courses/30/lessons/150369
    
    접근법
    - 물류창고에서 출발할 때 최대한 멀리가는 것이 좋을 것 같다고 생각
    - 어차피 멀리있는 집도 배달하러 가야하므로 돌아오는 길에 수거하기 편리
    - 즉 멀리 있는 집을 최대한 먼저 배달하고, 돌아올 때도 멀리있는 집 순으로 수거를 빨리 해야함 
    - 모든 집을 들린다고 코드를 설계한 후 실제로 배달 또는 수거가 있었을 경우에 answer 를 추가하는게 낫겠다!

    - 2시간 가까이 풀었는데 테스트 케이스에서 안 맞아서 레퍼런스 확인 ㅜㅜ
    - 역순으로 정렬하는 것보다 뒤에서부터 가는 것이 조금 더 직관적인 것 같아 해당 풀이로 선택
"""

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deli = 0
    pick = 0
    
    for i in range(n-1, -1, -1):
        deli += deliveries[i]
        pick += pickups[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (i + 1) * 2
    return answer