from collections import deque
def solution(s):

    s = deque(s)
    answer = 0

    for i in range(len(s)):
        s.rotate(-1)
        res = []
        for val in s:
            if val == '[' or val == '{' or val == '(':
                res.append(val)
            else:
                if res and val == ']' and res[-1] == '[':
                    res.pop()
                elif res and val == '}' and res[-1] == '{':
                    res.pop()   
                elif res and val == ')' and res[-1] == '(':
                    res.pop()
                else:
                    res.append(val)
        if not res:
            answer += 1
    return answer
