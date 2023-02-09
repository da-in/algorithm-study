import math

def solution(progresses, speeds):
    answer = []
    date = []
    stack = []
    for p, s in zip(progresses, speeds):
        date.append(math.ceil((100 - p) / s))

    for d in date:
        if not stack or stack[0] >= d:
            stack.append(d)
        else:
            answer.append(len(stack))
            stack = [d]

    answer.append(len(stack))
    return answer
