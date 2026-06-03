class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [0]*n
        left = [0]*n
        l = 1
        r = 1

        for i,num in enumerate(nums):
            left[i] = l
            j = -i -1
            right[j]=r
            l *= nums[i]
            r *= nums[j]

        return[l*r for l,r in zip(left,right)]



        
        