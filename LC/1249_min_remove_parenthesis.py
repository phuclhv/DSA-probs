'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count_opened_bracket = 0
        
        
        # Remove all closing bracket that don't have opening bracket before it
        # Start from the front
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == '(':
                count_opened_bracket += 1
            elif char == ')':
                count_opened_bracket -= 1
                
            if count_opened_bracket <0:
                count_opened_bracket = 0
                s = s[:idx] + s[idx+1:]
            else:
                idx +=1 
            
        # Remove all remained opening bracket that dont't have closing bracket after it
        # Start from the end
        idx = len(s) - 1
        while idx >= 0 and count_opened_bracket != 0:
            char = s[idx]
            if char == '(':
                count_opened_bracket -= 1 
                s = s[:idx] + s[idx+1:]
            idx -= 1
                
        return s
        