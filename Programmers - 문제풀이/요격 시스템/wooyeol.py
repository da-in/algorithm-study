"""
    요격 시스템
    https://school.programmers.co.kr/learn/courses/30/lessons/181188#
    
    50분 풀이 후 문제풀이를 하지 못해서 답안 확인
    하지만 첫 방식의 접근이 풀이가 가능한 방식이었음

    접근법
    하나의 총알을 소모하는 것은 하나의 그룹을 만드는 것과 동일하다.

    1. 범위 교집합 만들기
        첫 시도 후 실패했으나 구현된 다른 코드를 보며 코드를 재구성
        Start 지점을 기준으로 그림을 그려보았을 때 그룹 전체의 교집합과 현재 범위의 교집합이 존재한다면 하나의 그룹으로 묶을 수 있다.
        하나의 그룹을 묶을 수 없을 때 다시 새로운 그룹을 생성한다.
    
    2. End 좌표로 규칙성 찾기
        새로운 시각으로 규칙성을 찾아 접근
        End 지점을 기준으로 그림을 그려보면 그룹의 가장 작은 End 좌표보다 현재 Start 좌표가 같거나 크다면 하나의 그룹으로 묶을 수 있다.
        하나의 그룹으로 묶을 수 없을 때 다시 위의 방식으로 새로운 그룹을 만든다.
"""

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

def intersection(point1, point2):
    # p2의 시작점이 p1의 끝점보다 작을 때 교집합 발생
    if point1[1] > point2[0]:
        return (max(point1[0],point2[0]), min(point1[1],point2[1]))
    return ()
    

def solution1(targets):
    answer = 1
    
    # Start를 기준으로 정렬
    targets.sort(key=lambda x : x[0])
    
    # 첫 좌표를 기준으로 교집합이 가능한 좌표들을 검사
    target_itersection = targets[0]
    for target in targets[1:]:
        target_itersection = intersection(target_itersection,target)
        
        # 만약 교집합이 불가능한 좌표라면 새로운 교집합 범위를 계산하기 위해서 현재 좌표를 교집합 영역으로 설정 및 총알 갯수 추가
        if not target_itersection:
            target_itersection = target
            answer += 1
    
    return answer


"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (1.05ms, 10.3MB)
테스트 5 〉	통과 (6.75ms, 11.5MB)
테스트 6 〉	통과 (103.60ms, 26.1MB)
테스트 7 〉	통과 (631.79ms, 91.2MB)
테스트 8 〉	통과 (603.04ms, 91.1MB)
테스트 9 〉	통과 (321.49ms, 71.6MB)
테스트 10 〉통과 (480.14ms, 74.8MB)
테스트 11 〉통과 (0.00ms, 10.2MB)    
"""


def solution2(targets):
    answer = 0
    
    # End를 기준으로 정렬
    targets.sort(key=lambda x : (x[1] , x[0]))
    
    s,e = 0,0
    for target in targets:
        # 기준 End 좌표보다 Start 좌표가 같거나 더 큰 경우는 같은 그룹이 아니다.
        if target[0] >= e:
            # 총알 갯수를 추가하고
            answer += 1
            # 해당 End 좌표로 기준 End 좌표를 변경한다.
            e = target[1]
    
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.24ms, 10.3MB)
테스트 5 〉	통과 (4.71ms, 11.7MB)
테스트 6 〉	통과 (61.94ms, 26MB)
테스트 7 〉	통과 (346.64ms, 91MB)
테스트 8 〉	통과 (450.57ms, 91MB)
테스트 9 〉	통과 (300.12ms, 77.3MB)
테스트 10 〉통과 (60.26ms, 73.1MB)
테스트 11 〉통과 (0.01ms, 10.1MB)
"""

print(solution1(targets))
print(solution2(targets))
