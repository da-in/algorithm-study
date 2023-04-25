from collections import Counter

def solution(want, number, discount):
    answer = 0
    num = 0
    wants = list(zip(want,number))  # 제품과 수량을 묶은 리스트 생성
    count = []
    
    for i,dc in enumerate(discount):
        num = 0
        if dc in want:  # 10개씩 끊어줄 시작점을 잡아줌. 할인하는 제품이 want에 포함되어있다면
            count = list(Counter(discount[i:i+10]).items()) # 그 인덱스부터 10개를 슬라이싱 해준 뒤 갯수를 세어 리스트로 만듦
            for j in count: 
                if j in wants:  # 10개 끊어서 만든 리스트가 제품과 수량을 묶은 리스트와 동일하다면
                    num +=1 # num에 1을 더해준다
                else: 
                    continue    
            if num==len(want):  # num이 제품의 종류의 수와 같다면 answer += 1
                answer += 1
            print(num)
            
    return answer
