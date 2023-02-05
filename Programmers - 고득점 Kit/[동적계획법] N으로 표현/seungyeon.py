def main():
    N = 5
    number = 12
    print(solution(N,number))

def solution(N,number):
    dp = []

    for n in range(1,9):
        part = set()
        part.add(int(str(N)*n)) # 5,55,555,5555
        for i in range(n-1):
            for a in dp[i]:
                for b in dp[-i-1]:
                    part.add(a+b)
                    part.add(a-b)
                    part.add(a*b)
                    if b != 0: part.add(a//b)
        if number in part: return n
        dp.append(part)
    return -1

if __name__ == "__main__":
    main()