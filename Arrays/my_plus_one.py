'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. The large 
integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Initial solution:
        #join and type cast value to int
        #add 1
        #split
        #return list
        # Convert integers to string, join, and convert back to integer
        result = int("".join(map(str, digits)))
        print(result)
        result += 1 #adds one to the integer
        # Splitting the integer into digits 
        new_digits = list(map(int, str(result)))

        return new_digits
        