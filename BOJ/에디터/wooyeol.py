"""
    에디터
    https://www.acmicpc.net/problem/1406
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순 구현 -> 시간복잡도 줄이기
    
    1. 단순 구현으로 코드를 작성하고 시간 복잡도를 줄이기 위해서 여러 기법을 사용
    2. 1번의 방식으로 계속 실패하여 찾아보니 2개의 스택을 사용하여 구현할 수 있는 방식이 있어서 확인 후 구현
        - cursur를 인덱스로 접근하지 않고 하나의 경계로 확인하고 연산의 내용을 커서 기준 왼쪽과 오른쪽으로 나눠 문제를 해결
    참고 : https://corin-e.tistory.com/entry/백준-1406-에디터-파이썬
    
"""
import sys
input = sys.stdin.readline

######################      1      ########################

# sentence = input().strip()
# N = len(sentence)           # N = 10만
# M = int(input().strip())    # M = 50만

# cursur = N
# for _ in range(M):
#     command = input().split()
#     if command[0] == 'L' and cursur > 0:
#         # L 방향으로 커서 이동
#         cursur -= 1
#     elif command[0] == 'D' and cursur < N:
#         cursur += 1
#         # R 방향으로 커서 이동
#     elif command[0] == 'B' and cursur > 0:
#         sentence = sentence[:cursur-1] + sentence[cursur:]
#         # sentence.pop(cursur-1)
#         cursur -= 1
#         N -= 1
#     elif command[0] == 'P':
#         sentence = sentence[:cursur] + command[1] + sentence[cursur:]
#         # sentence.insert(cursur, command[1])
#         N += 1
#         cursur += 1

# print("".join(sentence))

############################################################

left = list(input().strip())
right = []
M = int(input())    # M = 50만

for _ in range(M):
    command = list(input().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))