class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = []
        result = []
        if target in nums:

            for i in range(len(nums)):

                if nums[i] == target:
                    index.append(i)
            if len(index):
                result.append(index[0])
                result.append(index[-1])
                return (result)


        else:
            return ([-1,-1])