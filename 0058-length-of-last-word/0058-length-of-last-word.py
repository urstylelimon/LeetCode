class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        length = len(word[-1])
        return length
