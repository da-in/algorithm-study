def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()

    day = 0
    count = 0


    while progresses:
        if (progresses[-1] + day * speeds[-1]) >= 100:
            progresses.pop()
            speeds.pop()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer
