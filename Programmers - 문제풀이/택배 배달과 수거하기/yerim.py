def solution(cap, n, deliveries, pickups):
    
    """
    - 가장 먼 집부터 배달 및 수거
        - 왕복으로 이동해야 햐므로, 배달과 수거를 동시에 해야 최소 이동 가능
        - 먼 집에서부터 배달해야 할 상자 개수(to_dlvr), 수거해야 할 상자 개수(to_pick)를 모두 센다.
    - 배달 및 수거를 할 때, 물류창고에 들릴 때마다 생기는 최대 수용치(cap)을 모두 쓴다고 가정하며 to_dlvr, to_pick 값을 cap 만큼 빼줌 
        - to_dlvr, to_pick을 갱신할 때마다 둘 다 0보다 같거나 작으면 트럭에 상자를 더 수용할 여력이 있는 것이므로, 
          물류창고에 들리지 않고 그 앞집으로 이동해 추가 배달 및 수거
        - 둘 중 한 값이라도 0보다 커지면 최대 수용 한계를 넘어선 것이므로 물류창고에 들림 => 이때 왕복 거리 계산해 answer에 더함
    
    참고: https://ddingmin00.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2023-KAKAO-BLIND-RECRUITMENT-%ED%83%9D%EB%B0%B0-%EB%B0%B0%EB%8B%AC%EA%B3%BC-%EC%88%98%EA%B1%B0%ED%95%98%EA%B8%B0?category=1331896
    """
    
    answer = 0
    to_dlvr = 0
    to_pick = 0
    
    for i in range(n - 1, -1, -1):
        to_dlvr += deliveries[i]
        to_pick += pickups[i]
        
        while to_dlvr > 0 or to_pick > 0:
            to_dlvr -= cap
            to_pick -= cap
            answer += (i + 1) * 2
    
    return answer