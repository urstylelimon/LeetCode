class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        else:
            while True:
                
                if n == 1:
                    return True
                    break
                
                if n<2 and n != 1:
                    return False
                    break
                n = n/2