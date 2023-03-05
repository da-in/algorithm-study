from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q=deque(people)
    while len(q)>1:
        if q[-1]+q[0]<=limit:
            q.popleft()
        q.pop()
        answer+=1
    return answer+1 if q else answer