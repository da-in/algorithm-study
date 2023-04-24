from collections import deque
def solution(want, number, discount):
    def ck():
        cnt=0
        for i in data:
            if data[i]>=0:
                cnt+=data[i]
        if cnt==0:
            return True
        else:
            return False
    answer = 0
    data={}
    for i in range(len(want)):
        data[want[i]]=number[i]
    q=deque()
    for i in range(sum(number)):
        if discount[i] in data:
                data[discount[i]]-=1
    if ck():
        answer+=1
    for i in range(0,len(discount)-sum(number)):
        if discount[i] in data:
            data[discount[i]]+=1
        if discount[i+sum(number)] in data:
                data[discount[i+sum(number)]]-=1
        if ck():
            answer+=1
    
    return answer
