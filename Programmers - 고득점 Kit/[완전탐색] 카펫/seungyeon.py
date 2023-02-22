def main():
    print(solution(10,2))

def solution(brown,yellow):

    answer = [0,0]
    num = brown + yellow

    for i in range(1,num+1):
        row = i
        col = num //row

        if(row > col):
            continue

        if((row -2)*(col -2) == yellow):
            answer[0] = col
            answer[1] = row
            return answer

    return answer
if __name__ == "__main__":
    main()