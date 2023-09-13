class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n==1:
            return True

        else:
            while True:
                n = n / 4
                if n == 1:
                    return True
                    break

                if n < 4 and n != 1:
                    return False
                    break