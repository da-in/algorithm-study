def time_to_num(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(plans):
    answer = []
    stack = []
    plans = list(map(lambda x: [time_to_num(x[1]), int(x[2]), x[0]], plans))
    plans.sort()
    cur = 0
    for plan in plans:
        start, playtime, name = plan
        gap = start - cur
        # 시간차 만큼 stack에서 과제 진행
        while stack and gap > 0:
            if stack[-1][1] > gap:
                stack[-1][1] -= gap
                break
            else:
                gap -= stack[-1][1]
                answer.append(stack.pop()[0])
        # stack에 과제 append
        stack.append([name, playtime])
        cur = start
    # stack에 남아있는 과제 더해주기
    while stack:
        answer.append(stack.pop()[0])
    return answer
