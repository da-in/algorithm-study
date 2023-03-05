def solution(numbers):
    x = len(numbers)
    answer = [-1] * x
    s = []
    
    for i in range(x):
        key = numbers[i]

        while s and s[-1][0] < key:
            answer[s[-1][1]] = key
            s.pop()

        s.append([key, i])
  
    return answer
  
  // 시간복잡도는,, O(N)이 아닐까,,,
