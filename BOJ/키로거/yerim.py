# 백준 5397번: 키로거 (Silver 2)
# https://www.acmicpc.net/problem/5397
# 소요 시간 : 60분
from collections import deque

# IDEA: 커서 기준으로 left, right 분할
# for _ in range(int(input())):
#     keylog = deque(input())
#     left = deque()
#     right = deque()
#     for k in keylog:
#         if k == '<' and len(left) > 0: # 바 보 ? . . 여기서 초반에 left, right 모두 비어있을 때 걸리지 못해서 <이 자꾸 문자로 인식됨
#             right.append(left.pop())

#         elif k == '>' and len(right) > 0:
#             left.append(right.popleft())

#         elif k == '-' and len(left) > 0:
#             left.pop()

#         else: # 문자인 경우
#             left.append(k)

#         print(k, left, right)
#     print(''.join(left.extend(right)))


# 60 풀이 후 정답 확인 => 거의 다 풀었긴 했네요,,
for _ in range(int(input())):
    keylog = deque(input())
    left, right = deque(), deque()

    for k in keylog:
        if k == "<":
            if left:
                right.append(left.pop())

        elif k == ">":
            if right:
                left.append(right.popleft())

        elif k == "-":
            if left:
                left.pop()

        else:  # 문자인 경우
            left.append(k)

    left.extend(right)
    print("".join(left))
