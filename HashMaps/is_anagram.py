#Leetcode 242: Valid Anagram
#Given two strings s and t, return true if t is an anagram
# of s, and false otherwise.
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#Constraints:
#1 <= s.length, t.length <= 5 * 104
#s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_ana = True #Initially set to True until proven otherwise
        my_hash = {}
        my_hashT = {}
        
 
        #Checks to make sure the lengths are the same before running the loops
        #If they are not then the inputs are not anagrams
        if(len(t) != len(s)):
            is_ana = False
        else:
            for char in s: #makes every character in s a key and the value the char count
                my_hash[char] = s.count(char)
            
            for char in t:  #makes every character in t a key and the value the char count
                my_hashT[char] = t.count(char)
                
                if char not in my_hash: #if t cointains a letter not in s its not a anagram
                    is_ana = False #since True is the original setting
                    break
                elif my_hash[char] != my_hashT[char]: #if the count doesnt match its not a anagram
                    is_ana = False
                    break
            
            

        return is_ana

#Solution Thought Process
#An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
#Things to account for that makes something not a anagram
# -Same string length
# -Same character count
# -Is same string length but contains different characters