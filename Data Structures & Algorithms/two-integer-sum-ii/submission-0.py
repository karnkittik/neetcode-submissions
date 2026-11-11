class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        pointer1 = 0
        pointer2 = n-1
        while pointer2 > pointer1:
            diff = target - numbers[pointer1]
            if diff == numbers[pointer2]:
                return [pointer1+1,pointer2+1]
            if diff > numbers[pointer2]:
                pointer1 += 1
            elif diff < numbers[pointer2]:
                pointer2 -= 1

        