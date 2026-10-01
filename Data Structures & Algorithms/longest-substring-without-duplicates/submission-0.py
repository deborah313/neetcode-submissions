class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, mlen = 0, 0, 0
        cset = set()
        while r < len(s): # zxyzxyz
            if s[r] in cset:  # z -> cset = ()
                cset.remove(s[l])
                l += 1
                continue
            cset.add(s[r]) #cset = (z,x)
            r += 1
            mlen = max(mlen, r-l) # 3
        
        return mlen