def main():
    progresses=[93, 30, 55]
    speeds=[1, 30, 5]
    print(solution(progresses, speeds))

def solution(progresses, speeds):
    stack=[]
    progresses.reverse()

    for i in range(len(progresses)):
        stack.append(((100-progresses[i])//speeds[i])+(1 if 100-progresses[i] > 0 else 0))
    
    answer=[]

    while(stack):
        cnt = 1
        top=stack.pop()
        print(cnt, stack)
        while(stack and stack[-1] <= top): 
            print("here")
            cnt+=1
            stack.pop()
        answer.append(cnt)

    return answer

if __name__ == "__main__":
    main()
    