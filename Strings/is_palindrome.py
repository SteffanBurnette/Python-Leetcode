#Leetcode 125: Valid Palindrome
'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and 
numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Removes all non-alphanumeric characters
        s2 = ''.join([char for char in s if char.isalnum()])
        #Reverses string and check if the string is empty or equals its inverse
        if s2.lower() == s2[::-1].lower():
            return True
        else:
            return False
        