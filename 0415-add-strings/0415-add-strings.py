class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        import sys
        sys.set_int_max_str_digits(10000)
        sum = int(num1) + int(num2)
        return str(sum)
        