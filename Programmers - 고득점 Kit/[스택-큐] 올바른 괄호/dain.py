def solution(s):
    answer = []
    for c in s:
        if not answer:
            answer.append(c)
            continue
        if c == "(":
            answer.append(c)
        elif answer[-1] == "(":
            answer.pop()
    return not answer

# 중간에 break 조건을 걸면 더욱 효율적일듯
