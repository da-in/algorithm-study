from itertools import permutations

def solution(k, dungeons):
    answer = 0
    index = [i for i in range(len(dungeons))]
    orders = permutations(index)
    for order in orders:
        count = 0
        hp = k
        for idx in order:
            if hp >= dungeons[idx][0]:
                hp -= dungeons[idx][1]
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer
