def solution(s):
    answer = 0
    data={"[":"]","{":"}","(":")"}
    
    def ck(string):
        if string[0] not in data:
            return False
        stk=[string[0]]
        for st in string[1:]:
            if st in data:
                stk.append(st)
            else:
                if stk and data[stk[-1]]==st:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True
    if ck(s):
        answer+=1
    s=list(s)
    for i in range(len(s)-1):
        s.append(s.pop(0))
        if ck(s):
            answer+=1
    return answer
