def main():
    print(solution([1, 2, 3, 2, 3]))

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]: break

    return answer
    
if __name__ == "__main__":
    main()