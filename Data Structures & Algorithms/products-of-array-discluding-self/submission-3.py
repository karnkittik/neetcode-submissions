class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for num in nums:
            if num != 0: product *= num
            else: count_zero += 1
        if not count_zero:
            return [int(product/n) for n in nums]
        if count_zero==1:
            return [product if n==0 else 0 for n in nums]
        if count_zero>1:
            return [0 for n in nums]
        