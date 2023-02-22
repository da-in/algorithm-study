def main():
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

def solution(clothes):
    arr = {}
    for c, type in clothes:
        arr[type] = arr.get(type, 0) + 1
        
    answer = 1
    for type in arr:   
        answer *= (arr[type] + 1)
    
    return answer - 1

if __name__ == "__main__":
    main()