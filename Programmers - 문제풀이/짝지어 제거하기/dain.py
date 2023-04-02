def solution(s):
    s = list(reversed(s))
    stack = []
    while s:
        if stack and stack[-1] == s[-1]:
            s.pop()
            stack.pop()
        else:
            stack.append(s.pop())
    return 0 if (stack) else 1
