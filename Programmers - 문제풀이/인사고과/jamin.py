# 두 점수가 모두 낮으면 인센티브 못받음 ㄷㄷㅜ
# 어케 판단하지....?
# 두 점수의 합이 높은 순으로 인센티브
# 동석차만큼 다음 석차 건너뜀
# 2등이 4명이라면 다음 석차는 6(2+4)등부터
# scores[[근태,동료평가]]

def solution(scores):
    answer = 0
    removeArr = []
    hoArr = scores[0]
    ho = sum(hoArr)

    scores = sorted(scores,key = lambda x : (x[0], -x[1]))
    #print(scores)
    for i in range(len(scores)-1):
        if scores[i][1]<scores[i+1][1]:
            if scores[i] == hoArr:
                return -1
            removeArr.append(scores[i])
        
    for i in removeArr:
        scores.remove(i)
        
    # print(removeArr)
    # print(scores)
    
    for i,score in enumerate(scores):
        scores[i] = sum(score)
        
    
    scores.sort(reverse=True)
    answer = scores.index(ho)+1
    
    return answer