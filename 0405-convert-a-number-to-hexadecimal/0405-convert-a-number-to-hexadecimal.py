class Solution:
    def toHex(self, num: int) -> str:
        def ConvertHex(num):
            if num == 0:
                return "0"
            if num < 0:
                num = 2 ** 32 + num
            return hex(num)[2:]

        return (ConvertHex(num))
        