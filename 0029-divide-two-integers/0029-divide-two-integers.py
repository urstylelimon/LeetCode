class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def divide(num1, num2):
            if num2 == 0:
                return 0

            negative = (num1 < 0) ^ (num2 < 0)
            num1, num2 = abs(num1), abs(num2)

            result = 0
            while num1 >= num2:
                flag, count = num2, 1
                while num1 >= (flag << 1):
                    flag <<= 1
                    count <<= 1
                num1 -= flag
                result += count

            if negative:
                result = -result
            if result > 2**31 - 1:
                return 2**31 - 1
            elif result < -2**31:
                return -2**31
            else:
                return result

        return (divide(dividend,divisor))