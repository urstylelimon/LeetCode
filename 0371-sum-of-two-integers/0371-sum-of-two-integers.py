class Solution:
    def getSum(self, a: int, b: int) -> int:
        import math 

        if a == 0 and b != 0:
            return b
        elif b == 0 and a != 0:
            return a
        else:
            result = int(math.log(math.exp(a) * math.exp(b)))
            return result