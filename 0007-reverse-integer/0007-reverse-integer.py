class Solution:
    def reverse(self, x: int) -> int:
        new_x = abs(x)
        str_x = str(new_x)
        reverse = str_x[::-1]
        
        if x < -2**31 or x > 2**31 - 1 :
            return 0
        elif x == 0 :
            return 0
        elif x < 0 :
            new_str = "-"
            new_list = [int(digit) for digit in reverse]
            if new_list[0] == 0:
                new_list.remove(0)
            for i in new_list:
                i = str(i)
                new_str += i
            if int(new_str) < -2147483648 or int(new_str) > 2147483647:
                return 0
            else:
                return (int(new_str))
        
        elif x > 0:
            new_str = ""
            new_list = [int(digit) for digit in reverse]

            if new_list[0] == 0:
                new_list.remove(0)
            for i in new_list:
                i = str(i)
                new_str += i

            if int(new_str) < -2147483648 or int(new_str) > 2147483647:
                return 0
            else:
                return (int(new_str))