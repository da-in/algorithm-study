def main():
    print(solution("AAAAE"))

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    num = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += arr.index(word[i]) * num[i] + 1
    return answer

    
if __name__ == "__main__":
    main()

# AAAA와 AAAE의 차이는 1*5 + 1 = 6
# AAA와 AAE의 차이는 6*5 + 1 = 31.
# AA와 AE의 차이는 31*5 + 1 = 156.
# A와 E의 차이는 156*5 + 1 = 781.
