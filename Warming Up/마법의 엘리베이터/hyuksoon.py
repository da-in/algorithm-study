def solution(storey):
    answer = 0
    num=[int(i) for i in reversed(str(storey))]
    num+=[0]
    for i in range(len(num)-1):
        if num[i]>5 or (num[i]==5 and num[i+1]>=5):
            answer+=10-num[i]
            num[i+1]+=1
        else:
            answer+=num[i]
    answer+=num[-1]
    return answer