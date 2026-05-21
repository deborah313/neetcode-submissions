class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): # I initially compare the 2 lengths of the strings, if not equal then automatic false
            return False
        
        dict_a , dict_b = {},{}

        for i in range(len(s)):
            
            if s[i] not in dict_a:
                dict_a[s[i]] = 1
            else:
                dict_a[s[i]] += 1

            if t[i] not in dict_b:
                dict_b[t[i]] = 1
            else:
                dict_b[t[i]] += 1
    
        return dict_a == dict_b