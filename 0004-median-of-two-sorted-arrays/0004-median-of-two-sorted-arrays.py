class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marged_array = sorted(nums1 + nums2)

        length = len(marged_array)

        if length % 2 == 0:
            median = int(length/2)
            pre_median = median -1

            result = (marged_array[pre_median] + marged_array[median]) /2

            return result

        else:
            median = int((length - 1)/2)

            result = marged_array[median]

            return result
