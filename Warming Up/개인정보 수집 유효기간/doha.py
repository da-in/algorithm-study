def solution(today, terms, privacies):
    answer = []
    today_sum = day_cal(today)
    print(today_sum)
    term_dict = {}
    index = 1

    for term in terms:
        t, m = term.split()
        term_dict[t] = int(m) * 28

    for privacy in privacies:
        d, t = privacy.split()
        if day_cal(d) + term_dict[t] <= today_sum:
            answer.append(index)
        index += 1

    return answer

def day_cal(s):
    year, month, day = s.split('.')
    sum = int(day) + int(month) * 28 + int(year) * 12 * 28
    return sum