# 771. Jewels and Stones 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1
        return count
    
jewels = "aA"
stones = "aAAbbbb"

solution = Solution()
print(solution.numJewelsInStones(jewels, stones))
