def solution(k, m, score):
    answer = 0
    
    // 예외처리
    if( len(score) < m) :
        return answer    
    
    leng = len(score)
    score.sort(reverse=True)
    
    for i in range(m-1, leng, m):
        answer += score[i] * m
        
    return answer
  
// 시간 복잡도는 sort 함수로 인해 O(NlogN),,

  
