from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        final_list = list(dict(sorted(freq.items(), key=lambda x:x[1])).keys())
        return final_list[len(final_list)-k:]




        