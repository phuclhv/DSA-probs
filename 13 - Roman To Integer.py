class Solution:

    def romanToInt(self, s: str) -> int:
        romanChar = {'M': 1000,
                     'D': 500,
                     'C': 100,
                     'L': 50,
                     'X': 10,
                     'V': 5,
                     'I': 1}
        numeralVal = 0
        prevCharVal, currCharVal = 1001, 0
        for char in s:
            currCharVal = romanChar[char]
            numeralVal += currCharVal
            if currCharVal > prevCharVal:
                numeralVal -= prevCharVal * 2
            prevCharVal = currCharVal
        return numeralVal