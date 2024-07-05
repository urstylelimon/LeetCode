class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefix_length(str1, str2):
            length = 0
            for d1, d2 in zip(str1, str2):
                if d1 == d2:
                    length += 1
                else:
                    break
            return length


        prefixes = set()

        for num in arr2:
            s = str(num)
            for i in range(len(s)):
                prefixes.add(s[:i + 1])

        result = 0

        for num in arr1:
            s = str(num)
            for i in range(len(s)):
                if s[:i + 1] in prefixes:
                    result = max(result, i + 1)

        return result