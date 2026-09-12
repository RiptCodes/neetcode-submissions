import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        knum = {}
        for i in nums:
            if i not in knum:
                knum[i] = 1
            else:
                knum[i] += 1
        
        highest_keys = heapq.nlargest(k, knum, key=knum.get)
        return highest_keys