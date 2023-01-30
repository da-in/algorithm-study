def solution(nums):
    h={}
    for i in nums:
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    if len(h)<len(nums)//2:
        return len(h)
    else:
        return len(nums)//2

# def solution(nums):
#     if len(set(nums))<len(nums)//2:
#         return len(set(nums))
#     else:
#         return len(nums)//2