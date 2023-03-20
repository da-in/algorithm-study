class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range (len(nums)): #0,1,2...
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                

            