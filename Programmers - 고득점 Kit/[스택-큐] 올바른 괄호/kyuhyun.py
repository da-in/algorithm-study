def solution(s):
    x = len(s)
    stack = []
    
    for i in range(x):
        key = s[i]
        
        if key == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(key)
               
    if len(stack) == 0:
        return True
    return False
    
