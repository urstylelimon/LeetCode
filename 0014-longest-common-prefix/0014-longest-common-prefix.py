class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        i = 0

        min_index = 0
        min_length = len(strs[0])

        while i < length :
            index_length = len(strs[i])

            if index_length < min_length :
                min_index = i
                min_length = index_length

            i += 1
        common_prefix = ""
        for j in range(min_length):
            flag = True

            for k in strs:
                if(k[j] != strs[min_index][j]):
                    flag = False
                    break

            if flag:
                common_prefix += strs[min_index][j]
            else:
                break

        return common_prefix

        