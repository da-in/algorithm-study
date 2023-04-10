def solution(s):
    answer=0
    for j in range(len(s)):
        s_stack=[]
        for i in s:
            if len(s_stack)==0:
                s_stack.append(i)
            else:
                if s_stack[-1]=='(' and i==')':
                    s_stack.pop()
                elif s_stack[-1]=='{' and i=='}':
                    s_stack.pop()
                elif s_stack[-1]=='[' and i==']':
                    s_stack.pop()
                else:
                    s_stack.append(i)
                    
        if len(s_stack)==0:
            answer+=1
            
        s=s[1:]+s[0]
                
    return answer
    