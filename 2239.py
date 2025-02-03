from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in nums:
            if abs(closest) > abs(i):
              closest = i
        
        if abs(closest) in nums:
            return abs(closest)
        else: 
            return closest
        
nums = [2,1,-1]
solution = Solution()
print(solution.findClosestNumber(nums))