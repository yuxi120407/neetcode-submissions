from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq_values = dict(sorted(freq.items(), key = lambda x: x[1], reverse=True))
        elements_list = list(sorted_freq_values.keys())
   

        return elements_list[:k]


        