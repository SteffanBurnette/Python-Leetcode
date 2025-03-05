class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def new_loc(loc, k, arrlen):
            return (loc + k)%arrlen

        hashbrown = {}
        ar_len = len(nums)

        for x in range(ar_len):
            hashbrown[new_loc(x, k, ar_len)] = nums[x]
        
        for key, val in hashbrown.items():
            nums[key] = val
        