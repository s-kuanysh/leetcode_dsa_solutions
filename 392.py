# 392. Is Subsequence 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)

        if s == '': return True
        if a > b: return False

        j = 0 

        for i in range(b):
            if t[i] == s[j]: 
                if j == a-1:
                    return True  
                j += 1
        return False

s = 'abc'
t = 'ahbgdc'

solution = Solution()
print(solution.isSubsequence(s,t))

s = 'axc'
t= 'ahbgdc'

print(solution.isSubsequence(s,t))
