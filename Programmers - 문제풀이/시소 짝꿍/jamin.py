from collections import Counter
import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def solution(weights):
    answer = 0
    
    check = [1/2, 2/3, 3/4] # 평형을 이루는 경우
    count = Counter(weights)
    count = sorted(count.items())   # 무게 오름차순 순으로 정렬

    for i in range(len(count)):
        for j in range(i+1,len(count)):
            if(count[i][0]/count[j][0]) in check:   # 평형을 이룬다면
                answer += count[i][1]*count[j][1]   # 평형을 이루는 무게를 가진 사람들의 조합 수를 더해준다
        if int(count[i][1]) >= 2:   # 만일 같은 무게를 가진 사람이 2명 이상이라면
            answer += nCr(int(count[i][1]),2)   # 조합 함수를 이용해 구해준다
            

    return answer