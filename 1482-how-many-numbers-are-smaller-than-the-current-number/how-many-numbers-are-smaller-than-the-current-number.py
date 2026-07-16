class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # Step 1: Sort a copy of nums
        sorted_nums = sorted(nums)
        
        # Step 2: Map each number to its first index in sorted array
        rank = {}
        for i, num in enumerate(sorted_nums):
            if num not in rank:   # store only first occurrence
                rank[num] = i
        
        # Step 3: Build result using rank
        return [rank[num] for num in nums]


# Example usage
nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))
# Output: [4,0,1,1,3]

nums = [6,5,4,8]
print(Solution().smallerNumbersThanCurrent(nums))
# Output: [2,1,0,3]

nums = [7,7,7,7]
print(Solution().smallerNumbersThanCurrent(nums))
# Output: [0,0,0,0]
