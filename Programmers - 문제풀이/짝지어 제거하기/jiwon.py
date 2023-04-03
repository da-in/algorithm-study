def solution(s):
    # while s:
    #     for i in range(len(s)-1):
    #         if s[i]==s[i+1]:
    #             s = s[:i]+s[i+2:]
    #             break
    #         if i==len(s)-2:
    #             return 0
    s_stack=[]
    for i in s:
        if len(s_stack)==0:
            s_stack.append(i)
        else:
            if s_stack[-1]==i:
                s_stack.pop()
            else:
                s_stack.append(i)
                
    return 0 if s_stack else 1