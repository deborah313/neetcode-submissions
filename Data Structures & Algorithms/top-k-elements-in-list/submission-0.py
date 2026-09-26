from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we have an array of numbers
        # we also have k
        # we want to return the k most frequent elements
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sorted_freq = sorted(freq.items(), key=lambda pair:pair[1], reverse = True)

        ans = []

        for num in range(k):
            ans.append(sorted_freq[num][0])
        
        return ans