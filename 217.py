# 217. Contains Duplicate
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in nums:
            if i in s:
                return False
            else: 
                s.add(i)

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))