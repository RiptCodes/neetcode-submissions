class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in map1:
                map1[key] = []
            map1[key].append(word)
        return list(map1.values())

