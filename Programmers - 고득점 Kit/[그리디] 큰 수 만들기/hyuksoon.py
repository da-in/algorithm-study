from collections import deque
def solution(number, k):
    answer = []
    number=deque(number)
    
    while number and k>0:
        if answer and answer[-1]<number[0]:
            while answer and number and answer[-1]<number[0] and k>0:
                answer.pop()
                k-=1
            answer.append(number.popleft())
        else:
            answer.append(number.popleft())
            
            
    answer+=list(number)
    for i in range(k):
        answer.pop()
    return ''.join(answer)