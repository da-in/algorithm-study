from collections import deque

def check(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == "(" and i==")":
                stack.pop()
            elif stack[-1] == "{" and i=="}":
                stack.pop()
            elif stack[-1] == "[" and i=="]":
                stack.pop()
            else:
                stack.append(i)

    if len(stack)==0:
        return 1;
    else:
        return 0;


def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(s)):

        answer += check(q)
        q.rotate(-1)

    return answer