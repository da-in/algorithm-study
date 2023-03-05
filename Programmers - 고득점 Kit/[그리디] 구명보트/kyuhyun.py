from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()  
    save = deque(people)

    while len(save) > 1:
        if save[0] + save[-1] <= limit:
            save.popleft()
        save.pop()
        answer += 1

    if save:
        answer += 1
    return answer
