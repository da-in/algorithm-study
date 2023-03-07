def solution(genres, plays):
    answer = []
    h={}
    musics={}
    
    for i,p in enumerate(genres):
        if p in h:
            h[p]+=plays[i]
        else:
            h[p]=plays[i]
        
        if p in musics:
            musics[p].append([i,plays[i]])
        else:
            musics[p]=[[i,plays[i]]]
            
    for i in musics:
        musics[i].sort(key=lambda x: (-x[1],x[0]))
        
    h=sorted(h.items(),key = lambda x: -x[1])
    
    for i in h:
        answer.append(musics[i[0]][0][0])
        if len(musics[i[0]])>1:
            answer.append(musics[i[0]][1][0])
        
    return answer
