class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        import math
        if num == 1:
            return False
        else:
            result = 1
            for i in range(2, int(math.sqrt(num)) + 1):
              if num % i == 0:
                result += i + num // i
                if result > num:
                  break

            if result == num:
              return True
            else:
              return False
