"""
풀이 시간 : 1시간
시간 초과가 계속 떠서 답안 확인

[접근 방법]
- 큰 원 안의 점 개수 - 작은 원 안의 점 개수
- 사분면에서 다 대칭이므로 한 면에서만 구하고 4를 곱해주면 됨
- 원의 반지름과 거리를 바탕으로 높이 계산
- 작은 원의 높이가 0이면 +1을 해주기 위해 반올림 후 +1 하는 방식 사용

[참고한 블로그](https://safetymo.tistory.com/13)
"""

import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        high1 = math.sqrt(r2 ** 2 - i ** 2)
        high2 = 0 if i > r1 else math.sqrt(r1 ** 2 - i ** 2)
        
        answer += math.floor(high1) - math.ceil(high2) + 1 # floor : 내림 / ceil : 올림

    return answer * 4

#     # 초기 접근 방법 (시간 초과)
#     for x in range(0, r2 + 1):
#         for y in range(1, r2 + 1):
#             r_squared = x ** 2 + y ** 2
#             if (r_squared >= r1 ** 2) and (r_squared <= r2 ** 2):
#                 answer += 1
    
#     return answer * 4