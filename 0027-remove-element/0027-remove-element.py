class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        new_list =0
        for i in nums:
            if i != val:
                nums[new_list] = i
                new_list += 1
        return new_list