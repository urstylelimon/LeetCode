class Solution:
    def isHappy(self, n: int) -> bool:
        while n not in (2, 3, 4, 5, 6, 8, 9):
            num_list = list(str(n))
            result = 0
            for i in num_list:
                i = int(i)
                sum = i * i
                result += sum
            n = result
            if n == 1:
                break
        if n == 1:
            return True
        else:
            return False