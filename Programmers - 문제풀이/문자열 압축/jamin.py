def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        prev_str = s[:i]
        compressed = ''
        count = 1

        for j in range(i, len(s), i):
            curr_str = s[j:j+i]

            if curr_str == prev_str:
                count += 1
            else:
                if count == 1:
                    compressed += prev_str
                else:
                    compressed += str(count) + prev_str
                prev_str = curr_str
                count = 1

        if count == 1:
            compressed += prev_str
        else:
            compressed += str(count) + prev_str

        answer = min(answer, len(compressed))

    return answer