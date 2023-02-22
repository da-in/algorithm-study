from collections import deque
def solution(priorities, location):
  
    q = deque()
    todo_list = []

    for idx, num in enumerate(priorities):
        q.append([idx, num])

    priorities.sort()

    while q:
        idx, num = q.popleft()
        if num < priorities[-1]:
            q.append([idx, num])
        else:
            todo_list.append(idx)
            priorities.pop()

    if location in todo_list:
        return todo_list.index(location) + 1
    
