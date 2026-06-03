class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} 


        for i in range (0,len(nums)):
            differnce = target - nums[i]
            if differnce in prevmap :
                return [prevmap[differnce],i]

            prevmap[nums[i]] = i    





            
