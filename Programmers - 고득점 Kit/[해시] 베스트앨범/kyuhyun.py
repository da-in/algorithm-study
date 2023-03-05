def solution(genres, plays):
    answer = []
    total_play = {}
    dic = {}


    for i in range(len(genres)):
        if genres[i] in total_play:
            total_play[genres[i]] = total_play[genres[i]] + plays[i]
        else:
            total_play[genres[i]] = plays[i]
        if genres[i] in dic:
            dic[genres[i]].append([plays[i], i])
        else:
            dic[genres[i]] = [[plays[i], i]]

    total_rank = sorted(total_play.items(), key=lambda x: x[1], reverse=True)

    for key, _ in total_rank:
        rank = sorted(dic[key], key=lambda x: (-x[0], x[1]))

        if len(rank) == 1:
            answer.append(rank[0][1])
        else:    
            for i in range(2):
                answer.append(rank[i][1])
    return answer
