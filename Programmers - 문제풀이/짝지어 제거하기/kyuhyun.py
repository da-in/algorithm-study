def solution(s):
    res = []

    for i in range(len(s)):
        val = s[i]
        if not res:
            res.append(val)
        else:
            if res[-1] == val:
                res.pop()
                continue
            res.append(val)   
             
    if res:
        return 0
    return 1
        
