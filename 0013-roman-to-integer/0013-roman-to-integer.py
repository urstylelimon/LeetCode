class Solution:
    def romanToInt(self, s: str) -> int:
        s
        roman_list = []

        for i in s:
            roman_list.append(i)
        values = {
        'I': 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        length = len(roman_list)
        sum = 0
        i = 0

        while i <length :

            if (i == (length-1)):
                sum += values.get(roman_list[i])
                break

            num1 = values.get(roman_list[i])
            num2 = values.get(roman_list[i+1])
            if (num1 < num2):
                sum += num2 - num1
                i += 2

            else:
                sum += values.get(roman_list[i])
                i += 1

        return sum

