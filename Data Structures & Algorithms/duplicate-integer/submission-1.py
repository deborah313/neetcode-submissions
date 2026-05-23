class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


        # we have a hash set of the nums array
        # hashset basically removes duplicates from OG array and makes a new one
        # We are comparing their lengths, if hashset is shorter than OG, then there was dupes
        # and it returns true

        # wastes memory