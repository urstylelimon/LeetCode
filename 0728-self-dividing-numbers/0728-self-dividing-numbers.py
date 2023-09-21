class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        new_list = []
        flag = False
        while left <=right :

            zero = '0' in str(left)

            if zero:
                pass

            else:
                spilt = list(str(left))
                for i in spilt:
                    i = int(i)
                    if (left % i == 0 ):
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    new_list.append(left)

            left += 1

        return new_list