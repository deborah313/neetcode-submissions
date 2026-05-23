class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sortedlist = sorted(nums)

        left = 0
        right = len(sortedlist) - 1

        while (left < right):

            isum = sortedlist[left] + sortedlist[right]

            if target > isum:
                left = left + 1
                
            elif target < isum:
                right = right - 1
                
            else:
                break

        solution = []

        for i in range(len(nums)):
            if nums[i] == sortedlist[left]:
                solution.append(i)
            elif nums[i] == sortedlist[right]:
                solution.append(i)
        return solution