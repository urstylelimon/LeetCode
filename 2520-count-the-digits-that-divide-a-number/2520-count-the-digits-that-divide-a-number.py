class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        new_list = list(str(num))
        for i in new_list:
            i = int(i)
            if(num % i == 0):
                count +=1
        return count
        