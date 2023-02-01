from itertools import permutations
def main():
    numbers="17"
    print(solution(numbers))

def solution(numbers):
    answer=0
    arr=[]
    
    for i in range(1,len(numbers)+1):
        arr.append(list(set(map(''.join,permutations(numbers,i)))))
    per = list(set(map(int,set(sum(arr,[])))))

    for i in per:
        if is_prime(i) : answer+=1
    return answer

def is_prime(n):
    if n < 2 : return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    main()
