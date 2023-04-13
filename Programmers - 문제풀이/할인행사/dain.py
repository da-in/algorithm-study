from collections import Counter

def solution(want, number, discount):
    # sliding window
    answer = 0
    target = {}
    for i in range(len(want)):
        target[want[i]] = number[i]

    window = {}
    for k in target.keys():
        window[k] = discount[:10].count(k)
    o = -1
    i = 9
    if window == target:
        answer += 1

    while i < len(discount) - 1:
        o += 1
        i += 1
        if discount[o] in window.keys():
            window[discount[o]] -= 1
        if discount[i] in window.keys():
            window[discount[i]] += 1
        if target == window:
            answer += 1

    return answer
