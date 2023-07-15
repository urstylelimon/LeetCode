class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_list =""
        for i in digits:
            new_list += str(i)
        num = int(new_list) + 1
        result = []
        for i in str(num):
            result.append(int(i))
        return result