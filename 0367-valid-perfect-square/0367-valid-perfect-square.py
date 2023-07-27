class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = num ** 0.5
        if int(result) == result:
            return True
        return False