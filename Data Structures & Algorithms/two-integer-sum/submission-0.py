class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i want to subtract the target from an index to receive a remainder and search for the remainder with the additional numbers in the list
        count = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in count:
                return [count[need], i]     
            count[n] = i                    