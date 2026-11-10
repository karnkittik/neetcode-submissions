class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sorted_nums = sorted(nums)
        undup = sorted_nums
        lc = 1
        lt = 1
        for i in range(len(undup)-1):
            if undup[i+1] == undup[i]: continue
            elif undup[i+1] - undup[i] == 1: 
                lc += 1
                if lc > lt: lt = lc
            else:
                lc = 1
        return lt
        