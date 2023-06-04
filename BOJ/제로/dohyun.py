"""

풀이시간
- 약 4분

접근법
- 제한시간 1초 + 입력 K 가 최대 10만번이기 때문에 시간 복잡도 보다는 빠르게 구현하는걸 연습해보자
- 익숙해지도록 deque 를 활용해서 풀이해보려고 했음, 근데 왜이렇게 쉽지??? 이게맞나??? 하면서 풀이

회고
- 몬가 참신한 다른 풀이가 보고싶다!

"""

import sys
from collections import deque

question = sys.stdin.readline       # 문자열 입력받음

K = int(question())                 # 반복 횟수 K 입력받음
total_money = deque()               # 장부 리스트 정의

for i in range(K):
    money = int(question())         # 돈 입력받음
    if money==0:                 
         total_money.pop()          # 가장 최근에 입력된 돈을 제거 -> pop
    else:
        total_money.append(money)   # 최근순으로 돈을 추가

print(sum(total_money))