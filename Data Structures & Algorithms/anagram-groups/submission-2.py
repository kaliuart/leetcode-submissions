class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = list()    
        for str in strs:
            lst = [0] * 26
            for elem in str:
                lst[ord(elem) - 97] += 1
            a.append(lst)

        result = []
        visited = set()
        for i in range(len(a)):
            l = list()
            
            if strs[i] in visited:
                continue
            visited.add(strs[i])
            
            for j in range(i+1, len(a)):
                if a[i] == a[j]:
                    l.append(strs[j])
                    visited.add(strs[j])
            
            l.append(strs[i])
            result.append(l)
        
        return result         