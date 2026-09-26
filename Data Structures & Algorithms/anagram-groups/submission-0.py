class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupedwords = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in groupedwords:
                groupedwords[sorted_word].append(word)
            else:
                groupedwords[sorted_word] = [word]
        
        return list(groupedwords.values())

             
