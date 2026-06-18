class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = collections.Counter(nums)
        return[key for key, count in my_map.most_common(k)]
        