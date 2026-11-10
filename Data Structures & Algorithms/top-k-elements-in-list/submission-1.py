class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts: counts[num] += 1
            else: counts[num] = 1
        sorted_counts = sorted([(v,k) for k,v in counts.items()],reverse=True)
        return [v[1] for v in sorted_counts[:k]]