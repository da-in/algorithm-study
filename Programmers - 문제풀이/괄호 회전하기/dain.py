def solution(s):
    answer = 0
    shift = [s]
    pair = [("{", "}"), ("[", "]"), ("(", ")")]
    # 왼쪽으로 한칸씩 이동시킨 문자열의 리스트 생성
    for _ in range(len(s) - 1):
        shift.append(shift[-1][1:] + shift[-1][0])
    shift = list(map(lambda x: list(reversed(x)), shift))
    # 각 문자열에 대해 올바른지 확인
    for i in range(len(s)):
        stack = []
        while shift[i]:
            if stack and (stack[-1], shift[i][-1]) in pair:
                stack.pop()
                shift[i].pop()
            else:
                stack.append(shift[i].pop())
        if not stack:
            answer += 1
    return answer
