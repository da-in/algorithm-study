def solution(s):
    answer = []
    for i in range(1, len(s) // 2 + 1):
        word = ""
        count = 1
        target = s[:i]
        for j in range(i, len(s) + i, i):
            if target == s[j : j + i]:
                count += 1
            else:
                if count != 1:
                    word += str(count)
                word += target
                target = s[j : j + i]
                count = 1
        answer.append(len(word))
    return min(answer)
