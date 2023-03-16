def solution(nums):
    hash = {}

    for i in nums:
        hash[i] =   1

    if len(hash) > len(nums)//2 :
        return len(nums)//2
    return len(hash)