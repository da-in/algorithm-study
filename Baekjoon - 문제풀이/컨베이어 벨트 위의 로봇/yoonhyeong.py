import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

belt = deque(map(int, sys.stdin.readline().split()))
robot = deque([0] * N)
result = 0

while belt.count(0) < K:

    result += 1

    belt.rotate()
    robot.rotate()
    robot[-1] = 0       # N번째 칸에서 로봇 내리기

    for i in range(N - 2, -1, -1): # 가장 먼저 올라간 로봇부터 이동(문제 조건)
        if robot[i] == 1 and belt[i + 1] >=1 and robot[i + 1] == 0: # 현재 칸에 로봇 O, 다음 칸 내구도 1이상, 다음 칸에 로봇 X일 경우 이동
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1

    robot[-1] = 0

    if belt[0] != 0 and robot[0] != 1: # 올리는 칸의 내구도 0이 X, 로봇이 없을 경우 로봇 올리기
        robot[0] = 1
        belt[0] -= 1


print(result)



# 파이썬에서 회전과 관련된 문제가 나오면 deque.rotate(int) 함수 사용.




