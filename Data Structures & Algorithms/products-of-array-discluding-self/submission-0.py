import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []


        for i, num in enumerate(nums):
            temp = num
            nums[i] = 1
            result.append(math.prod(nums))
            nums[i] = temp
        
        return result


        