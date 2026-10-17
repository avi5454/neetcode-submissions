class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
    
        for keys in strs:
            key = "".join(sorted(keys))
            if key in group:
                group[key].append(keys)
            else:   
                group[key]=[keys]
        return list(group.values())