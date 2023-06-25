class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lenght = len(nums)
        sum = 0
        list = []
        flag = False
        for i in range(0,lenght):

            for j in range(i+1,lenght):

                sum = nums[i] + nums[j]
                if(sum == target):
                    list +=[i,j]
                    flag = True
                    break
            if flag:
                break
                
        return list








