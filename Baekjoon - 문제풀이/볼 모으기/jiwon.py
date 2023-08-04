import sys
from collections import deque

N = int(sys.stdin.readline())
ball_list = [b for b in sys.stdin.readline().rstrip('\n')]

def move_ball(ball_list, move_ball):
    ball_stack = deque()
    temp = 0
    result = 0
    for new_b in ball_list:
        if not ball_stack:
            ball_stack.append(new_b)
            continue
        old_b = ball_stack.pop()
        if old_b==move_ball:
            temp+=1
        else:
            result+=temp
            temp=0
            ball_stack.append(old_b)
        ball_stack.append(new_b)
    return result if ball_stack.pop()==move_ball else result+temp

case1 = move_ball(ball_list, 'R')
case2 = move_ball(ball_list[::-1], 'R')
case3 = move_ball(ball_list, 'B')
case4 = move_ball(ball_list[::-1], 'B')

print(min(case1, case2, case3, case4))