def solution(nums):
    answer = {}
    
    pokemon_num = len(nums) // 2
    
    for i in range(len(nums)) :
        answer[nums[i]] = "new pokemon!"
        if len(answer) == pokemon_num:
            return len(answer)
               
    return len(answer)
