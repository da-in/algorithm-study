def solution(nums):
    choice = len(nums) / 2
    set_nums = set(nums)
    
    return choice if choice <= len(set_nums) else len(set_nums)