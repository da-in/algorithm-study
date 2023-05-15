
def solution(cards):
    groups = []
    answer = 0
    #시작 설정
    idx = cards[0] -1
    cards[0] = 0
    sum = 1
    
    for i in range(0,len(cards)):
        if cards[idx] != 0:
            pre_idx = idx
            idx = cards[idx] -1
            cards[pre_idx] = 0
            sum += 1
            
        else:   # 이미 연 상자일 경우 (cards[idx]==0)
            if sum == len(cards):   # 1번 상자 제외하고 남는 상자 없을 경우 게임 종료
                return 0
            groups.append(sum)  # group에 상자 수 저장
            sum = 0 # 상자 수 초기화
            for j in range(len(cards)): # 1번째 상자 이후 열 인덱스 정하기
                if cards[j]!=0:
                    idx = cards[j]-1
                    break
            if cards[idx] != 0:
                pre_idx = idx
                idx = cards[idx] -1
                cards[pre_idx] = 0
                sum += 1
                
    groups.sort(reverse=True)
    return groups[0]*groups[1]