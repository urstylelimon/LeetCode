class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_num = []
        list = []
        length = len(nums)
        for i in range(length):
            new_num.append(i)

        j = 0
        while j < length:
            if new_num[j] not in nums:
                return new_num[j]

            j += 1
        return length
