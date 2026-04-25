class Solution(object):
    def letterCombinations(self, digits):
        result = []
        def backtrack(index, current):
            phn = {"2": "abc", "3":"def", "4":"ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
            if index == len(digits):
                return result.append(current)
            for letter in phn[digits[index]]:
                backtrack(index + 1, current + letter)
        backtrack(0, "")
        return result