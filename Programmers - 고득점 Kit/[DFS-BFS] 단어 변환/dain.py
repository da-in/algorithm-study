from collections import defaultdict, deque

def isNext(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
    return count == 1


def solution(begin, target, words):
    word_dict = defaultdict(list)
    words.append(begin)
    words = list(set(words))

    for w1 in words:
        for w2 in words:
            if isNext(w1, w2):
                word_dict[w1].append(w2)

    visit = set([begin])
    q = deque([(begin, 0)])
    while q:
        cur_w, cur_i = q.popleft()
        if cur_w == target:
            return cur_i
        for n in word_dict[cur_w]:
            if n not in visit:
                visit.add(n)
                q.append((n, cur_i + 1))

    return 0
