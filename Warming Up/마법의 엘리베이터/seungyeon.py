answer = 1000000

def main():
    global answer

    dfs(16,0)
    print(answer)

def dfs(num,stone):
    global answer

    if(num < 10):
        stone += min(num,11-num) # 그냥 1*n || +10짜리 1개까지 합치고도 
        answer = min(answer,stone)
        return 

    res = num % 10 # 1##### ####에 해당하는 아이들
    num //= 10

    dfs(num,stone+res)  
    dfs(num+1,stone+(10-res))
    return 

if __name__ == "__main__":
    main()