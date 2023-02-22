from collections import deque
def solution(priorities, location):
    answer = 0
    priorities=deque(priorities)
    while priorities:
        if priorities[0]==max(priorities):
            priorities.popleft()
            answer+=1
            location-=1
            if location<0:
                return answer
        else:
            priorities.append(priorities.popleft())
            location-=1
            if location<0:
                location=len(priorities)-1
    

    return answer
