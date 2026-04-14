
def romanToInt(self, s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ss = " ".join(s).strip().split(" ")
    total = 0
    for i in range(len(ss) - 1):
        if roman_numerals[ss[i]] < roman_numerals[ss[i + 1]]:
            total -= roman_numerals[ss[i]]
        else:   
            total += roman_numerals[ss[i]]
    total += roman_numerals[ss[-1]]
    return total
    
print(romanToInt(None, "MCMXCIV"))