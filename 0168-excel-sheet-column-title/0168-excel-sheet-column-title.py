class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber  >0:
            columnNumber  -= 1
            sum = columnNumber  % 26
            ch = chr(65+sum)
            result.append(ch)
            columnNumber  //= 26
        new_result = ''.join(result)
        rev = new_result[::-1]
        return rev
        