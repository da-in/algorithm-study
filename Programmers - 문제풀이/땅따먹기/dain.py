def solution(land):
    acc = [0, 0, 0, 0]
    for l in land:
        for i in range(4):
            temp = acc[0:i] + acc[i + 1 :]
            l[i] += max(temp)
        acc = l
    return max(acc)
