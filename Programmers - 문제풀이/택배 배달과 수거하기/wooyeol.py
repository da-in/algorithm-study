"""
    택배 배달과 수거하기
    https://school.programmers.co.kr/learn/courses/30/lessons/150369
    
    50분 풀이 후 감을 잡지 못해서 풀이 참조

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 그리디
    
    - 두 리스트가 주어지고 cap 만큼 택배 상자를 제거해나가야한다.
    - 하나는 전달하면 사라지고 하나는 회수해야 사라진다.

    최소 경로 동선은 가장 먼 집부터 문제를 해결하였을 때 구할 수 있다.
    현재까지의 주소지에 택배 전달 + 가능한 수거 모두 하기
"""

def solution(cap, n, deliveries, pickups):
    # 역순으로 검사하기
    deliveries.reverse()
    pickups.reverse()
    
    answer,sum_of_current_delivery,sum_of_current_pickup = 0,0,0
    
    # 그리디 접근
    # 한 iter씩 검사하며 배송을 해야하는 갯수 + 픽업을 해야하는 갯수를 추가한다.
    for idx in range(n):
        # (현재 기준)마지막째 주소지의 배송과 픽업 갯수 갱신
        sum_of_current_delivery += deliveries[idx]
        sum_of_current_pickup += pickups[idx]
        
        # 만약 배송 혹은 픽업이 가능한 장소가 있다면 해당 위치까지 왕복 거리 수행
        while sum_of_current_delivery > 0 or sum_of_current_pickup > 0:
            sum_of_current_delivery -= cap
            sum_of_current_pickup -= cap
            answer += (n - idx) * 2
            
    return answer

#1 Case #1
cap,n,deliveries,pickups = 4,5,[1,0,3,1,2],[0,3,0,4,0]
print(solution(cap,n,deliveries,pickups))

#2 Case #2
cap,n,deliveries,pickups = 2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]
print(solution(cap,n,deliveries,pickups))