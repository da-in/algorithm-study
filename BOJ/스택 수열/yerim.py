"""
백준 1874번: 스택 수열 (Silver 2)
https://www.acmicpc.net/problem/1874

- 풀이 시간 : 1시간 15분

[첫 번째 접근]
1. 스택에 목표하는 숫자가 없다면(not in), 스택에 해당 숫자가 나올 때까지 push
2. 스택에 목표하는 숫자가 있다면(in) pop
3. pop 할 때 목표하는 숫자를 얻을 수 없다면 수열 만들기 불가능
=> 계속 시간 초과... in 연산 때문인 것 같음

[두 번째 접근]
1. 다음 숫자(target)가 현재 숫자(current_n)보다 작으면 스택에 target 숫자가 이미 있으므로 pop만으로 얻을 수 있음
2. 다음 숫자(target)가 현재 숫자(current_n)보다 크면 스택에 pop 하기 전 push 필요
3. pop 할 때 목표하는 숫자를 얻을 수 없다면 수열 만들기 불가능
=> 여전히 시간 초과... 하나하나 push, pop을 하면 안되는 건가?

도저히 시간 초과를 해결할 수 없어 답안 확인
Reference: https://hongcoding.tistory.com/39
[접근 방법]
- 느낌은 비슷하지만, 두 가지 디테일이 더 필요했다.
  - stack의 마지막 숫자가 목표 숫자와 같은지 확인하고 pop을 해줘야 함.
  - flag 사용. flag 미사용 시, NO가 출력된 이후 answer가 또 출력될 수 있음.
"""

from collections import deque

stack = deque()  # 시간 복잡도 최소화를 위해 덱 사용
answer = deque()  # 답 출력을 위해 push, pop 기록 저장
current_n = 1  # stack에 어느 숫자까지 push 했는지 기록
flag = False

for _ in range(int(input())):
    target = int(input())

    while current_n <= target:  # 목표 숫자가 나올 때까지 push
        stack.append(current_n)
        answer.append("+")
        current_n += 1

    if stack[-1] == target:  # 목표 숫자 pop
        stack.pop()
        answer.append("-")
    else:  # 수열 만들기 불가능
        print("NO")
        flag = True
        break

# 정답 출력
if not flag:
    for a in answer:
        print(a)


# # 초기 풀이 (두 번째 접근에 해당) => 시간 초과
# stack = deque()  # 시간 복잡도 최소화를 위해 덱 사용
# answer = deque()  # 답 출력을 위해 push, pop 기록 저장
# current_n = 0  # stack에 어느 숫자까지 push 했는지 기록

# for i in range(int(input())):
#     target = int(input())

#     if target > current_n:  # 스택에 목표 숫자가 없다면
#         for j in range(current_n, target):  # 목표 숫자가 나올 때까지 push
#             stack.append(j + 1)
#             answer.append("+")

#         current_n = target

#     # 목표 숫자를 pop
#     last = stack.pop()
#     answer.append("-")

#     if last != target:  # pop으로 얻은 숫자가 목표 숫자와 다르다면 수열 만들기 불가능
#         print("NO")
#         break

# for a in answer:
#     print(a)
