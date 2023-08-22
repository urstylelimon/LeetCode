class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            count = n
        else:

            step1 = 2
            step2 = 1


            for i in range(3, n + 1):
                current = step1 + step2
                step2 = step1
                step1 = current

            count = step1
            
        return count
