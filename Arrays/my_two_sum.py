'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        if len(nums) < 2:
            return

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    arr.append(i)
                    arr.append(j)
                
        
        return arr

#Can also sort the array and perform binary search of target which will 
#have a time complexity of O( n )...