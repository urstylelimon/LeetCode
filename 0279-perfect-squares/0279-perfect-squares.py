class Solution:
    def numSquares(self, n: int) -> int:
        count = [0] * (n + 1)
        for i in range(1, n + 1):
            count[i] = i
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                count[i] = min(count[i], count[i - j * j] + 1)
                j += 1
        return count[n]