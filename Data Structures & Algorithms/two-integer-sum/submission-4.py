class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        my_map = {}
        for i in range (len(nums)):
            my_map[nums[i]] = i
        
        for i in range (len(nums)):
            temp = target - nums[i]
            temps = nums[i]
            nums[i] = 0
            if temp in nums:
                result.append(i)
                result.append(my_map[temp])
                result.sort()
                break
            nums[i] = temps
        return result
            

        

        