class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if abs(temp - target) < abs(sum - target):
                    sum = temp

                if temp < target:
                    left += 1
                else:
                    right -= 1

        return sum