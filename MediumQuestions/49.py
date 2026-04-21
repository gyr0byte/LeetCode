class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) <= 1:
            return [strs]
        
        groups = {}
        
        for s in strs:                 
            count = [0] * 26
            for ch in s:                  
                count[ord(ch) - ord('a')] += 1

            key = ""
            for num in count:
                key += "#" + str(num)


            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values()) 