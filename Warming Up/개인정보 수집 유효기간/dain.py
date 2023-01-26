def date_to_num(date):
    y, m, d = map(int, date.split("."))
    return ((y - 2000) * 12 * 28) + (m * 28) + d


def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    today = date_to_num(today)

    for term in terms:
        t, v = term.split()
        term_dict[t] = int(v) * 28

    for i in range(0, len(privacies)):
        d, t = privacies[i].split()
        if date_to_num(d) + term_dict[t] <= today:
            answer.append(i + 1)

    return answer
