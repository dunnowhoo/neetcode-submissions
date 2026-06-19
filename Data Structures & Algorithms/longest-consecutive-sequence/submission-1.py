class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        curr_length = 0

        for i, num in enumerate(num_set):
            if (num - 1) not in num_set :
                current_num = num
                curr_length = 1
                while ((current_num + 1) in num_set):
                    curr_length += 1
                    current_num += 1
            
            longest = max(longest, curr_length)
        
        return longest

        