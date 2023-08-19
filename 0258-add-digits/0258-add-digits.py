class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        while True:
            num = list(str(num))
            for i in num:
                result += int(i)
            num = result
            result = 0
            if len(str(num)) == 1:
                break
        return num