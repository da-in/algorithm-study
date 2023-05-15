"""

풀이시간
- 약 30분 소요

접근법
- 리스트로 접근하는 것 보다는 문자열로 접근하는 것이 더 빠를 것이라고 생각했음
- 구현하는데에는 딱히 어려운 점은 없었음
- 하지만 시간초과 오류가 발생 (해당 문제가 시간제한이 조금 빡세다고 함)
- 시간초과 문제를 해결하지 못해서 결국 레퍼런스 참조
- append, pop 의 시간복잡도가 O(1) 인 것을 활용하여 스택 두 개를 사용하는 것이 핵심

회고
- 스택 자료구조에 대해서 조금 더 알아보자!

"""

### 기존 풀이
import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
cursur_loc = len(text)

for _ in range(n):
    command = sys.stdin.readline().strip()
    if (command[0] == 'L') & (cursur_loc != 0):
        cursur_loc -= 1
    elif (command[0] == 'D') & (cursur_loc != len(text)):
        cursur_loc += 1
    elif (command[0] == 'B') & (cursur_loc != 0):
        text = text[:cursur_loc-1] + text[cursur_loc:]
        cursur_loc -= 1
    elif (command[0] == 'P'):
        text = text[:cursur_loc] + command[2] + text[cursur_loc:]
        cursur_loc += 1

print(text)


### 레퍼런스 참고 풀이
import sys

left_stack = list(sys.stdin.readline().rstrip())
right_stack = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    
    if (command[0] == 'L') & (left_stack):
        right_stack.append(left_stack.pop())
    elif (command[0] == 'D') & (right_stack):
        left_stack.append(right_stack.pop())
    elif (command[0] == 'B') & (left_stack):
        left_stack.pop()
    elif (command[0] == 'P'):
        left_stack.append(command[1])

print("".join(left_stack + list(reversed(right_stack))))