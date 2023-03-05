from collections import defaultdict


def solution(genres, plays):
    genreCount = defaultdict(int)
    genrePlay = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        genreCount[genres[i]] += plays[i]
        genrePlay[genres[i]].append((plays[i], i))

    genreCount = sorted(genreCount.items(), key=lambda item: item[1], reverse=True)

    for genre, _ in genreCount:
        genrePlay[genre].sort(key=lambda x: (-x[0], x[1]))
        top2 = genrePlay[genre][0:2]
        for p in top2:
            answer.append(p[1])

    return answer
