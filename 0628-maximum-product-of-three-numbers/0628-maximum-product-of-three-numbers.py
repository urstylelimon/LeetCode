class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        case1 = nums[-1] * nums[-2] * nums[-3]
        case2 = nums[0] * nums[1] * nums[-1]

        result = max(case1,case2)

        return result