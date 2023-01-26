def solution(number):
    answer = pro(number)
    print(answer)
    return answer
            

def pro(number):
    cnt = 0
    for i in range(len(number)):
        for j in range(i,len(number)):
            for k in range(j,len(number)):
                if (number[i] + number[j] + number[k] == 0
                and not(i==j) and not(i==k) and not(j==k)):
                    cnt += 1
    return cnt;