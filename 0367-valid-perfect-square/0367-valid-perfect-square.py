class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        else:            
            for i in range(int(num**0.5) + 1):
                if i * i == num:
                    return True
                    break
            return False