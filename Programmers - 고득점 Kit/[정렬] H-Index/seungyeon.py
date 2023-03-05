def main():
    print(solution(	[3, 0, 6, 1, 5])) # 6,5,3,1,0

def solution(citations):
    # citations.sort()
    # return citations[(len(citations)-1)//2]

    citations.sort()
    n = len(citations)
    for i in range (n):
        if citations[i] >= n-i:
            return n-i
    return 0
    
if __name__ == "__main__":
    main()