def solution(numbers):
    len_num = len(numbers) # numbers 길이
    answer = [-1] * len_num # 조건에 해당 안되는 경우를 위해 -1로 미리 초기화
    stack = [] # index값 저장용 스택(이거 생각해내는데 2시간 걸림)
    
    for i in range(len_num-1): # 어짜피 맨 마지막은 무조건 -1이라 한번 덜 반복
        stack.append(i)
        
        while stack and numbers[stack[-1]] < numbers[i+1]:
            answer[stack.pop()] = numbers[i+1]

    return answer

# 입력 예제 1번
# [index(1), index(3), index(3), -1] 
# 입력 예제 2번
# [-1, index(2), index(4), index(4), -1, -1] 
# 맨 마지막은 무조건 -1이네? 그럼 마지막 한번은 반복 안해도 될듯
# 이전 index의 값을 스택에 저장해놨다가 한번에 처리를 해주는게 이상적인데..
# 값을 입력했으면 stack.pop()을 해서 스택 비우기 + numbers[stack[-1]]을 지속적으로 비교해야함 while 돌면서
# 그 다음 numbers[i+1]의 값을 넣어줌 굳