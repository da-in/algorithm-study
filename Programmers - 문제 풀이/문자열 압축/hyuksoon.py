def solution(s):
    answer = len(s)
    for i in range(2,3):
        answerTemp=""
        result=0
        cnt=1
        temp=""
        target=""
        for idx,sub in enumerate(s):
            
            temp+=sub
            cnt+=1
            print(cnt,i,target,temp,sub,result)
            if cnt>i:
                cnt=1
                if target=="":
                    target=temp
                    result=0
                    temp=""
                elif target==temp:
                    result+=1
                    temp=""
                else:
                    if result>1:
                        print("!")
                        answerTemp+=str(result)
                    answerTemp+=target
                    result=1
                    target=temp
                    temp=""
                    
            print(target,temp)
            print(answerTemp)
        print(result,target,temp)
        if result>1:
            answerTemp+=str(result)
            answerTemp+=target
        answerTemp+=temp
        print(answerTemp)
        answer=min(answer,len(answerTemp))
                        
                 
    return answer

print(solution("aaabbaccc"))