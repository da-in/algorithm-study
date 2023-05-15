# 백준 1406번: 에디터 (Silver 2)
# https://www.acmicpc.net/problem/1406

"""
접근 방법
- 처음에는, 문자열을 리스트로 변환해 pop, insert 연산 => 시간 초과가 계속 남 
    - insert, remove 함수는 O(n)만큼의 시간을 소요하는데, 최대 명령 수가 매우 커서 시간 초과가 난다고 함 
- 따라서 [블로그](https://seongonion.tistory.com/53)를 참고해 커서를 기준으로 문자열을 두 곳에 나누어 담음
    - pop, append 연산으로 시간 초과 해결 가능!
    - 또한 sys를 이용해 문자열을 입력 받아야 시간 초과가 나지 않음
"""

import sys

# 커서를 기준으로 왼쪽은 str1, 오른쪽은 str2
# 초기 커서 위치는 맨 뒤
str1 = list(sys.stdin.readline().rstrip())
str2 = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "L":
        if str1:
            str2.append(str1.pop())

    elif cmd[0] == "D":
        if str2:
            str1.append(str2.pop())

    elif cmd[0] == "B":
        if str1:
            str1.pop()

    elif cmd[0] == "P":
        str1.append(cmd[1])

# L 커맨드에서, str2에 문자가 앞으로 쌓여야 원래 순서에 맞지만,
# append 연산을 위해 계속 뒤에 쌓고 마지막에 순서를 뒤집어줌
str1.extend(reversed(str2))
print("".join(str1))
