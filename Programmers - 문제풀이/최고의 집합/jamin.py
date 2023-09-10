def solution(n, s):
    # n이 s보다 크면 최고의 집합이 존재하지 않으므로 -1 return
    if n>s:
        return [-1]
    
    # 몫으로 배열을 모두 채워준다
    answer = [s//n] * n
    
    # 나머지만큼 반복하며 뒤에서부터 1씩 더해준다
    for i in range(1, (s%n)+1):
        answer[-i] += 1
        
    return answer