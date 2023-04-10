def solution(s):
    answer = []

    for i in range(1, len(s) // 2 + 1):
        pre = s[:i]
        result = ''
        count = 1

        for j in range(i, len(s), i):  # i 간격으로 j증가시킴
            cur = s[j:j + i]  # s[1:2]

            if cur == pre:
                count += 1
            else:
                if count == 1:
                    result += pre  # 1은 생략
                else:
                    result += str(count) + pre
                pre = cur  # pre 업데이트
                count = 1

        if count == 1:  #남은 문자들 처리
            result += pre
        else:
            result += str(count) + pre
            
        answer.append(len(result))

    answer.append(len(s))
    return min(answer)
