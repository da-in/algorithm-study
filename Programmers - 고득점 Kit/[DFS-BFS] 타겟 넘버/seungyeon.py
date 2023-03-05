def main():
    numbers=[4, 1, 2, 1]	
    target=4
    solution(numbers,target)

def solution(numbers, target):
    answer = 0

    answer += dfs(0,numbers,0,target)
    print(answer)
    return answer

def dfs(depth, numbers ,num,target):

    answer = 0
    if depth == len(numbers):
        if target==num:
            return 1
        else : return 0
        
    else :
        answer += dfs(depth+1,numbers,num+numbers[depth],target) 
        answer += dfs(depth+1,numbers,num-numbers[depth],target)
        return answer
    
    
if __name__ == "__main__":
    main()
