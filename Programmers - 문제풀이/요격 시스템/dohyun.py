def solution(targets):
    """
    
    풀이시간
    - 약 1시간 20분 소요

    접근법
    - 다음 미사일의 start point 가 현재 미사일의 end point 보다 멀리 있으면 따로 요격 시켜야 함
    - 따라서 다음 미사일의 start point 가 현재 미사일의 end point 보다 작으면 묶어서 요격 가능
    - 핵심은 end_point 를 기준으로 정렬해야 함 (예제를 통해 파악)

    회고
    - 왜인지 모르겠지만 풀이가 정돈 되지 않은 느낌..?
    - 원래는 리스트에서 인덱스로 접근하는 대신 요소를 제거하는 안 좋은 습관(?)이 있었는데 조금은 고쳐진것 같음
    
    """
    
    targets.sort(key = lambda x:x[1])
    answer = 1
    start_idx = 0
    
    while start_idx < len(targets)-1:
        step = 1
        
        while targets[start_idx][1] > targets[start_idx + step][0]:
            step += 1
            if start_idx + step >= len(targets):
                answer -= 1
                break
        
        start_idx += step
        answer += 1

    return answer