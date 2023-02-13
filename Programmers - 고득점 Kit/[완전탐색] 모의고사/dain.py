def solution(answers):
    answer = []
    marks = [
        [1, 2, 3, 4, 5] * 2000,
        [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000,
    ]
    count = [0, 0, 0]

    for i in range(len(answers)):
        if marks[0][i] == answers[i]:
            count[0] += 1
        if marks[1][i] == answers[i]:
            count[1] += 1
        if marks[2][i] == answers[i]:
            count[2] += 1

    m = max(count)

    for i in range(3):
        if count[i] == m:
            answer.append(i + 1)

    return answer
