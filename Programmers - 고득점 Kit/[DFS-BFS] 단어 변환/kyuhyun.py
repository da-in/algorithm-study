def solution(begin, target, words):
    visit = [0] * len(words)
    st = []  
    answer = -1
    leng = len(begin)

    if target not in words:
        return 0

    st.append(begin)
    while st:
        wd = st.pop()
        answer += 1

        if wd == target :
            return answer

        for k in range(len(words)):
            word = words[k]
            count = 0
            if visit[k] == 1:
                continue
            for i in range(leng):
                if wd[i] == word[i]:
                    count += 1
            if count == leng - 1:
                st.append(word)
                visit[k] = 1
