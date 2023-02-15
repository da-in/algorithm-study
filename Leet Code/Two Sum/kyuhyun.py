class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rest = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == rest:
                    return [i, j]
