class Solution:
    def maximumSwap(self, num: int) -> int:
        list = str(num)
        list = [int(digit) for digit in list]
        i = 0
        while  i < len(list):
            max_digit = i
            new_max = i+1
            if new_max == len(list):
                break
            for j in range(i+1,len(list)):
                if list[new_max] <= list[j]:
                    new_max = j

            if list[new_max] > list[max_digit]:
                temp = list[new_max]
                list[new_max] = list[max_digit]
                list[max_digit] = temp
                break
            i += 1

        result = 0
        for digit in list:
            result = result * 10 + digit
            
        return result