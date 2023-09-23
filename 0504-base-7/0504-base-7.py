class Solution:
    def convertToBase7(self, num: int) -> str:
        import math
        devider = 7
        result = ""
        reverse = ""
        if 7 > num >= 0:
            return str(num)
        elif 6 < num:
            while num >= devider:
                reminder = num % devider
                reminder = str(reminder)
                result += reminder
                num = math.floor(num / devider)
            if num < 7:
                result += str(num)
                for i in result:
                    reverse = i + reverse
                return reverse

        else:
            num = -num
            while num >= devider:
                reminder = num % devider
                reminder = str(reminder)
                result += reminder
                num = math.floor(num / devider)
            if num < 7:
                result += str(num)
            for i in result:
                reverse = i + reverse
            reverse = "-" + reverse
            return reverse