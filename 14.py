# 14. Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         min_length = float('inf')

         for s in strs:
              if len(s) < min_length:
                   min_length = len(s)
                
         i = 0
        
         while i < min_length:
             for s in strs:
                  if s[i] != strs[0][i]:
                     return s[:i]

             i+=1

         return s[:i]

strs = ["flower", "flow", "flight"]

solution = Solution()
print(solution.longestCommonPrefix(strs))

strs = ["dog", "racecar", "car"]

print(solution.longestCommonPrefix(strs))