answer = 0

def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer

def dfs(numbers, num, sum, target):
    global answer
    if sum == target and num == len(numbers):
        answer += 1
    if num >= len(numbers):
        return
    dfs(numbers, num+1, sum + numbers[num], target)
    dfs(numbers, num+1, sum - numbers[num], target)