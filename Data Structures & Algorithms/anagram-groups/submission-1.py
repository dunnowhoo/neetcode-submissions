class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = collections.defaultdict(list)

        for i, word in enumerate(strs):
            my_map[''.join(sorted(word))].append(word)
        return list(my_map.values())
        
        