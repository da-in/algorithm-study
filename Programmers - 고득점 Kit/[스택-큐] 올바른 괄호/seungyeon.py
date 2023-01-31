def solution(s):
    stack=[]
    for i in s:
        if(i == "("):
            stack.append(i)
        else:
            if(stack == []):
                return False
            else:
                stack.pop()
    return len(stack) == 0