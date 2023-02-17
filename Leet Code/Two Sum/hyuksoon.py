class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l=0
        r=len(nums)-1
        temp=[]
        for i in range(len(nums)):
            temp.append([nums[i],i])
        temp.sort()

        while l<r:
            mid=temp[l][0]+temp[r][0]
            if mid<target:
                l+=1
            elif mid>target:
                r-=1
            else:
                return [temp[l][1],temp[r][1]]