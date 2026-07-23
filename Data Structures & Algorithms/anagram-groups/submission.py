class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        for word in strs:
            c = [0] * 26

            for char in word:
                c[ord(char) - 97] += 1
            
            key = tuple(c)
            if key not in group:
                group[key] = []
            
            group[key].append(word)
        
        return list(group.values())


"""       
d = dict()
        for i in range(len(strs)):
            s = tuple(sorted(strs[i]))
            if s not in d:
                d[s] = []
            d[s].append(strs[i])
        return list(d.values())
"""




