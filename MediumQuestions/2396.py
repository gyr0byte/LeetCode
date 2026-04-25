class Solution(object):
    def isStrictlyPalindromic(self, n):
        def to_base_3(n):
            if n == 0:
                return '0'
            digits = []
            while n:
                digits.append(str(n % 3))
                n //= 3
            return ''.join(reversed(digits))
        base2 = bin(n)
        base3 = to_base_3(n)
        if n >= 4:
            return False
        return (base2 == base2[::-1]) and (base3 == base3[::-1])