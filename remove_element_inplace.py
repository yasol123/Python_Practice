"""
input: nums = [2,3,3,4], val = 3
output: 2 nums = [2,4]
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[i],nums[res]=nums[res],nums[i] #swap
                res+=1
        return res 
