class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        if target not in nums:
            if target > nums[-1] :
                return len(nums)

            else:
                for i in nums:
                    if target > i :
                        pass
                    if i > target :
                        return nums.index(i)
                        break


