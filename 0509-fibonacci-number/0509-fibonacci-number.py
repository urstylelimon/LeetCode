class Solution:
    def fib(self, n: int) -> int:
        list = []
        i = 0
        while i<= n :
            if i == 0 or i == 1:
                list.append(i)
            else:
                sum = ( list[-1] + list[-2] )
                list.append(sum)
            i += 1

        result = list[-1]
        return result
        