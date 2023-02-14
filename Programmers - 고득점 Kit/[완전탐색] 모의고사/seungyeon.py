def main():
    print(solution([1,3,2,4,2]))
def solution(answers):
    answer = [0,0,0]
    patterns=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    for i in range(len(answers)):
        if answers[i] == patterns[0][i%5]:
            answer[0]+=1
        if answers[i] == patterns[1][i%8]:
            answer[1]+=1
        if answers[i] == patterns[2][i%10]:
            answer[2]+=1
    max = 0
    result=[]
    for i in range(3):
        if answer[i] > max:
            max = answer[i]
    for i in range(3):
        if answer[i] == max:
            result.append(i+1)
    
    return result
    
if __name__ == "__main__":
    main()