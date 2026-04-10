class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10          # extract last digit
            reversed_num = reversed_num * 10 + digit  # build reversed number
            x //= 10                # remove last digit

        return original == reversed_num