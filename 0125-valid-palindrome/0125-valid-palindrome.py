class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for char in s:
            if char.isalnum():
                result += char.lower()
        str_x = str(result)
        reverse_x = str_x[::-1]
        print(reverse_x)
        if str_x == reverse_x:
            return True
        else:
            return False
        