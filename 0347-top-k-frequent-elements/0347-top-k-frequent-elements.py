class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            try:
                frequencies[num] += 1
            except KeyError:
                frequencies[num] = 1

        sort = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))

        return list(sort.keys())[:k]