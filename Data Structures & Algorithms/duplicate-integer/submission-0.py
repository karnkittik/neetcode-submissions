class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        have = []
        for e in nums:
            if e in have:
                return True
            have.append(e)
        else:
            return False
        