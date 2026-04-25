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
    
    # you can just return False for n >= 4, 
    # since the problem states that n is strictly palindromic 
    # if it is palindromic in all bases from 2 to n - 2, a
    # nd for n >= 4, it will not be palindromic in base 2.