def solution(s):
    stk=[]
    for i in s:
        if i=="(":
            stk.append(i)
        elif stk:
            stk.pop()
        else:
            return False
    if stk:
        return False
    else:
        return True

def solution(s):
    temp=0
    for i in s:
        if i=="(":
            temp+=1
        elif temp>0:
            temp-=1
        else:
            return False
    if temp>0:
        return False
    else:
        return True