from collections import deque
def solution(s):
    answer = -1

    if len(s)%2==1:
        return 0
    
    q=deque(list(s[1:]))

    data=[s[0]]
    while data or q:
        if data and q and q[0]==data[-1]:
            data.pop()
            q.popleft()
        elif q:
            data.append(q.popleft())
        else:
            break
    if data:
        return 0
    
    return 1
